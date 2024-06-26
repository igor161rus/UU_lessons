## python version 3.12
import random

import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType, VkBotEvent
import logging
import handlers
from models import Registration

try:
    from practice_03 import settings
except ImportError:
    exit('You should use settings.py file to configure settings')

logger = logging.getLogger('bot')


def configure_logger():
    stream_handler = logging.StreamHandler()
    file_handler = logging.FileHandler('bot.log')
    stream_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s %(message)s'))
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s %(message)s'))
    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)
    stream_handler.setLevel(logging.INFO)
    logger.setLevel(logging.DEBUG)


configure_logger()


class UserState:
    def __init__(self, scenario_name, step_name, user_id, context=None):
        self.scenario_name = scenario_name
        self.step_name = step_name
        self.context = context or {}
        self.user_id = user_id

    def get(self, user_id):
        return UserState(user_id=self.user_id, scenario_name=self.scenario_name, step_name=self.step_name,
                         context=self.context)


class Bot:
    def __init__(self, group_id, token):
        self.group_id = group_id
        self.token = token
        self.vk = vk_api.VkApi(token=token)
        self.long_poller = VkBotLongPoll(self.vk, self.group_id)
        self.api = self.vk.get_api()
        # self.user_states = dict()  # user_id -> UserState

    def run(self):
        for event in self.long_poller.listen():
            try:
                self.on_event(event)
            except Exception as exc:
                pass

    def on_event(self, event: VkBotEvent):
        if event.type != VkBotEventType.MESSAGE_NEW:
            return

        user_id = event.object.message['from_id']
        text = event.object.message['text']
        state = UserState.get(user_id=str(user_id))

        if state is not None:
            self.continue_scenario(user_id, state, text)
        else:
            for intent in settings.INTENTS:
                if any(token in text.lower() for token in intent['tokens']):
                    if intent['answer']:
                        self.send_text(intent['answer'], user_id)
                    else:
                        self.start_scenario(user_id, intent['scenario'], text)
                    break
            else:
                self.send_text(settings.DEFAULT_ANSWER, user_id)

    def send_text(self, text_to_send, user_id):
        self.api.messages.send(
            message=text_to_send,
            random_id=random.randint(0, 2 ** 20),
            peer_id=user_id,
        )

    def send_image(self, image, user_id):
        pass  # TODO

    def send_step(self, step, user_id, text, context):
        if 'text' in step:
            self.send_text(step['text'].format(**context), user_id)
        if 'image' in step:
            handler = getattr(handlers, step['image'])
            image = handler(text, context)
            self.send_image(image, user_id)

    def start_scenario(self, user_id, scenario_name, text):
        scenario = settings.SCENARIOS[scenario_name]
        first_step = scenario['first_step']
        step = scenario['steps'][first_step]
        self.send_step(step, user_id, text, context={})
        UserState(user_id=str(user_id), scenario_name=scenario_name, step_name=first_step)

    def continue_scenario(self, user_id, text, state):
        # state = self.user_states[user_id]
        steps = settings.SCENARIOS[state.scenario_name]['steps']
        step = steps[state.step_name]

        try:
            handler = getattr(handlers, step['handler'])
            if handler(text=text, context=state.context):
                # Go to the next step
                next_step = steps[step['next_step']]
                self.send_step(next_step, user_id, text, state.context)
                if next_step['next_step']:
                    state.step_name = next_step['next_step']
                else:
                    # self.user_states.pop(user_id)
                    logger.info(f'User {user_id} completed the scenario')
                    Registration(name=state.context['name'], email=state.context['email'])
                    state.delete()
            else:
                text_to_send = step['failure_text'].format(**state.context)
                self.send_text(text_to_send, user_id)

        except TypeError:
            # logger.exception(exc)
            text_to_send = step['text']
            # text_to_send = step['text'].format(**state.context)
            Registration(name=state.context['name'], email=state.context['email'])
            state.delete()
            return text_to_send




if __name__ == '__main__':
    # conf_logger()
    bot = Bot(group_id=settings.group_id, token=settings.token)
    bot.run()
