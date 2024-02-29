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
        pass

if __name__ == '__main__':
    bot = Bot(club=club, token=token)
    bot.run()
