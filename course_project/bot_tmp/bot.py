## python version 3.12

import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType, VkBotEvent
import handlers
from course_project.models import Registration

try:
    import settings
except ImportError:
    exit('You should use settings.py file to configure settings')


class UserState:
    def __init__(self, scenario_name, step_name, context=None):
        self.scenario_name = scenario_name
        self.step_name = step_name
        self.context = context or {}


class Bot:
    def __init__(self, club, token):
        self.group_id = club
        self.token = token
        self.vk = vk_api.VkApi(token=token)
        self.long_poller = VkBotLongPoll(self.vk, self.group_id)
        self.api = self.vk.get_api()
        self.user_states = dict()  # user_id -> UserState

    def run(self):
        """
        Run the function to listen for events and handle them by calling the on_event method.
        """
        # Слушаем longpoll
        for event in self.long_poller.listen():
            try:
                self.on_event(event)
            except Exception as exc:
                print(exc)

    def on_event(self, event: VkBotEvent):
        if event.type != VkBotEventType.MESSAGE_NEW:
            return

        user_id = event.object.message['from_id']  # event.object.peer_id  # .message.peer_id
        text = event.object.message['text']  #event.object.text #event.message.text
        if user_id in self.user_states:
            text_to_send = self.continue_scenario(user_id, text)
        else:
            for intent in settings.INTENTS:
                if any(token in text.lower() for token in intent['tokens']):
                    if intent['answer']:
                        text_to_send = intent['answer']
                    else:
                        text_to_send = self.start_scenario(user_id, intent['scenario'])
                    break
            else:
                text_to_send = settings.DEFAULT_ANSWER

        self.api.messages.send(message=text_to_send,
                               random_id=0,
                               peer_id=user_id)

    def start_scenario(self, user_id, scenario_name):
        scenario = settings.SCENARIOS[scenario_name]
        first_step = scenario['first_step']
        step = scenario['steps'][first_step]
        text_to_send = step['text']
        self.user_states[user_id] = UserState(scenario_name=scenario_name, step_name=first_step)
        return text_to_send

    def continue_scenario(self, user_id, text):
        state = self.user_states[user_id]
        steps = settings.SCENARIOS[state.scenario_name]['steps']
        step = steps[state.step_name]

        handler = getattr(handlers, step['handler'])
        if handler(text=text, context=state.context):
            next_step = steps[step['next_step']]
            text_to_send = next_step['text'].format(**state.context)
            if next_step['next_step']:
                state.step_name = next_step['next_step']
            else:
                self.user_states.pop(user_id)
                Registration(name=state.context['name'], email=state.context['email'])
                state.delete()
        else:
            text_to_send = step['failure_text'].format(**state.context)
        return text_to_send


if __name__ == '__main__':
    bot = Bot(club=settings.club, token=settings.token)
    bot.run()
