import vk_api
from vk_api.bot_longpoll import VkBotLongPoll
from settings import club, token

class Bot:
    def __init__(self, club, token):
        self.group_id = club
        self.token = token

        self.vk = vk_api.VkApi(token=token)
        self.long_poller = VkBotLongPoll(self.vk, self.group_id)

    def run(self):
        for event in self.long_poller.listen():
            print('получено событие')
            try:
                self.on_event(event)
            except Exception as exc:
                print(exc)

    def on_event(self, event):
        if event.type == vk_api.bot_longpoll.VkBotEventType.MESSAGE_EVENT:
            print(event.message.text)
        else:
            print('hgjhg ghghfgfdf hjjk', event.type)

if __name__ == '__main__':
    bot = Bot(club=club, token=token)
    bot.run()
