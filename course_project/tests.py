from unittest import TestCase
from unittest.mock import patch, Mock, ANY
from vk_api.bot_longpoll import VkBotMessageEvent
from bot import Bot


class Test1(TestCase):
    RAW_EVENT = {
        'group_id': 224905513,
        'type': 'message_new',
        'event_id': 'ecf9016c59c5df8617bb9a9c05d862c6e29838d1',
        'v': '5.199',
        'object': {'message':
                       {'date': 1709725647, 'from_id': 467598913, 'id': 0, 'out': 0, 'version': 10000123,
                        'attachments': [], 'conversation_message_id': 33, 'fwd_messages': [], 'important': False,
                        'is_hidden': False, 'peer_id': 2000000001, 'random_id': 0, 'text': 'hello bot',
                        'is_unavailable': True},
                   'client_info':
                       {'button_actions': ['text', 'vkpay', 'open_app', 'location', 'open_link', 'open_photo',
                                           'callback', 'intent_subscribe', 'intent_unsubscribe'], 'keyboard': True,
                        'inline_keyboard': True, 'carousel': True, 'lang_id': 0}
                   }
    }

    def test_1(self):
        count = 5
        obj = {'a': 1}
        events = [obj] * count
        long_poller_mock = Mock(return_value=events)
        long_poller_listen_mock = Mock()
        long_poller_listen_mock.listen = long_poller_mock
        with patch('bot.vk_api.VkApi'):
            with patch('bot.VkBotLongPoll', return_value=long_poller_listen_mock):
                bot = Bot(club='', token='')
                bot.on_event = Mock()
                bot.run()

                bot.on_event.assert_called()
                bot.on_event.assert_any_call(obj)
                assert bot.on_event.call_count == count

    def test_on_event(self):
        event = VkBotMessageEvent(raw=self.RAW_EVENT)

        send_mock = Mock()

        with patch('bot.vk_api.VkApi'):
            with patch('bot.VkBotLongPoll'):
                bot = Bot(club='', token='')
                bot.api = Mock()
                bot.api.messages.send = send_mock

                bot.on_event(event)

        send_mock.assert_called_once_with(
            message=self.RAW_EVENT['object']['message']['text'],
            random_id=ANY,
            peer_id=self.RAW_EVENT['object']['message']['peer_id'],
        )

