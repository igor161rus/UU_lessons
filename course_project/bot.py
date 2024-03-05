## python version 3.12

import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from settings import club, token


class Bot:
    """
    echo bot для ВК
    """
    def __init__(self, club, token):
        """
        :param group_id: id группы ВК
        :param token: секретный токен
        """
        self.group_id = club
        self.token = token

        self.vk = vk_api.VkApi(token=token)
        self.long_poller = VkBotLongPoll(self.vk, self.group_id)

        self.api = self.vk.get_api()

    def run(self):
        for event in self.long_poller.listen():
            print('получено событие')
            try:
                self.on_event(event)
            except Exception as exc:
                print(exc)

    def on_event(self, event):
        if event.type == VkBotEventType.MESSAGE_NEW:
            print(event.message.text)
            self.api.messages.send(message=event.message.text,
                                   random_id=0,
                                   peer_id=event.message.peer_id)
        else:
            print('hgjhg ghghfgfdf hjjk', event.type)


if __name__ == '__main__':
    bot = Bot(club=club, token=token)
    bot.run()
