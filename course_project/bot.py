## python version 3.12

import vk_api
import logging
import logging.config
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType, VkBotEvent
import handlers
from course_project.models import Registration

# from course_project import handlers
# from settings import club, token
from log_settings import log_config

try:
    import settings
except ImportError:
    exit('You should use settings.py file to configure settings')

logging.config.dictConfig(log_config)

# Configure logger
logger = logging.getLogger('bot')


# def conf_logger():
#     """
#        Configure logger with stream and file handlers, setting formatter and log levels.
#     """
#
#     stream_handler = logging.StreamHandler()
#     file_handler = logging.FileHandler('bot.log')
#     stream_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
#     file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
#     logger.addHandler(stream_handler)
#     logger.addHandler(file_handler)
#     stream_handler.setLevel(logging.INFO)
#     logger.setLevel(logging.DEBUG)

class UserState:
    def __init__(self, scenario_name, step_name, context=None):
        self.scenario_name = scenario_name
        self.step_name = step_name
        self.context = context or {}


class Bot:
    """
    echo bot для ВК
    """

    def __init__(self, club, token):
        """
        Initializes the class with the given club ID and token.

        :param group_id: id группы ВК
        :param token: секретный токен
        """
        # Set the group_id and token
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
                logger.exception('Ошибка в обработчике событий Exception %s', exc)

    def on_event(self, event: VkBotEvent):
        """
            Обработка событий от бота

            Args:
            :param event : VkBotMessageEvent object
                The event to be handled
            return: None
            """
        # Check if the event is a new message
        # global text_to_send
        if event.type != VkBotEventType.MESSAGE_NEW:
            log = logging.getLogger('info')
            log.info('New message %s', event)
            log.info('We received an event %s', event.type)
            # logger.info('New message %s', event)
            # logger.info('We received an event %s', event.type)
            return

        user_id = event.message.peer_id # event.object.peer_id  # .message.peer_id
        text = event.message.text #event.object.text #event.message.text
        if user_id in self.user_states:
            # Continue the scenario
            text_to_send = self.continue_scenario(user_id, text)

        else:
            # search intent
            log_d = logging.getLogger('debug')
            log_d.debug("We don't know how to handle event with type %s", event.type)
            for intent in settings.INTENTS:
                log_d.debug(f'User gets {intent}')
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

        # logger.debug("'We don't know how to handle event with type %s", event.type)
        # raise ValueError("We don't know how to handle event with type", event.type)
        # if event.type == VkBotEventType.WALL_POST_NEW:
        #     print(event.type)
        #     print(event)
        #     print(event.message)

    # def get_api(self):
    #     """
    #     Get the API instance
    #     """
    #     return self.api
    def start_scenario(self, user_id, scenario_name):
        """
        Start the scenario
        """
        scenario = settings.SCENARIOS[scenario_name]
        first_step = scenario['first_step']
        step = scenario['steps'][first_step]
        text_to_send = step['text']
        self.user_states[user_id] = UserState(scenario_name=scenario_name, step_name=first_step)
        return text_to_send

    def continue_scenario(self, user_id, text):
        """
        Continue the scenario
        """
        state = self.user_states[user_id]
        steps = settings.SCENARIOS[state.scenario_name]['steps']
        step = steps[state.step_name]

        handler = getattr(handlers, step['handler'])
        if handler(text=text, context=state.context):
            # Go to the next step
            next_step = steps[step['next_step']]
            text_to_send = next_step['text'].format(**state.context)
            if next_step['next_step']:
                # switch to next step
                state.step_name = next_step['next_step']
            else:
                # Finish the scenario
                self.user_states.pop(user_id)
                log_i = logging.getLogger('info')
                log_i.info('Зврегистрирован: {name} {email}'.format(**state.context))
                Registration(name=state.context['name'], email=state.context['email'])
                state.delete()
        else:
            # return current step
            text_to_send = step['failure_text'].format(**state.context)
        return text_to_send


if __name__ == '__main__':
    # conf_logger()
    bot = Bot(club=settings.club, token=settings.token)
    log = logging.getLogger('info')
    log.info('Bot run %s')
    bot.run()
