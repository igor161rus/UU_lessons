## python version 3.12

import vk_api
import logging
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType, VkBotEvent
from settings import club, token

logger = logging.getLogger('bot')
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(stream_handler)
stream_handler.setLevel(logging.INFO)
logger.setLevel(logging.DEBUG)


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

        # Initialize VK API and long poller
        self.vk = vk_api.VkApi(token=token)
        self.long_poller = VkBotLongPoll(self.vk, self.group_id)

        self.api = self.vk.get_api()

    def run(self):
        """
        Run the function to listen for events and handle them by calling the on_event method.
        """
        # Слушаем longpoll
        for event in self.long_poller.listen():
            try:
                self.on_event(event)
            except Exception as exc:
                logger.exception('Exception %s', exc)

    def on_event(self, event: VkBotEvent):
        """
            Обработка событий от бота

            Args:
            event : Event
                The event to be handled
            return: None
            """
        # Check if the event is a new message
        if event.type == VkBotEventType.MESSAGE_NEW:
            logger.info('New message %s', event)
            logger.info('We received an event %s', event.type)
            peer_id = event.message.peer_id
            text_message = event.message.text
            self.api.messages.send(message=text_message,
                                   random_id=0,
                                   peer_id=peer_id)
        else:
            logger.debug('We don\'t know how to handle event with type %s', event.type)
            raise ValueError('We don\'t know how to handle event with type', event.type)
        if event.type == VkBotEventType.WALL_POST_NEW:
            print(event.type)
            print(event)
            print(event.message)

    def get_api(self):
        """
        Get the API instance
        """
        return self.api


if __name__ == '__main__':
    bot = Bot(club=club, token=token)
    bot.run()
