group_id = '224905513'
token = 'vk1.a.q0-pDFS607MAIU6Uu_MAEX_zPldE7nP0wYU5QZF5Jtxdz1YDr-V4voj3-lC9XnN1EkbtM_43QTesAer6j4pTAZsBJ12pqPxs1wZa3X65p05rtco7kuiE_kPrq_KrxKf7rewquayKaYoj-DwIrqelFwxAXe9JPmY5nNJT9WyTheqrPIMVhoyjkWD81d1cgjRTeDb8WdTTe66f1GHJdh6n2w'

INTENTS = [
    {
        'name': 'Дата проведения',
        'tokens': ('когда', 'сколько', 'дата', 'дату'),
        'scenario': None,
        'answer': 'Конференция проводится 10 мая, регистрация открыта до 10 утра'
    },
    {
        'name': 'Место проведения',
        'tokens': ('где', 'место', 'локация', 'адрес', 'метро'),
        'scenario': None,
        'answer': 'Конференция провйдет в павильоне 18Г в Экспоцентре'
    },
    {
        'name': 'Регистрация',
        'tokens': ('зарегистрироваться', 'регистр', 'добав'),
        'scenario': 'registration',
        'answer': None
    }
]

SCENARIOS = {
    'registration': {
        'first_step': 'step1',
        'steps': {
            'step1': {
                'text': 'Чтобы заренистрироваться, введите ваше имя. Оно будет написано на бэйдже',
                'failure_text': 'Имя должно состоять из 3-30 букв и дефиса. Попробуйте еще раз',
                'handler': 'handle_name',
                'next_step': 'step2'
            },
            'step2': {
                'text': 'Введите email. Мы отпрвим на него все данные',
                'failure_text': 'Во введенном адресе ошибка. Попробуйте еще раз',
                'handler': 'handle_email',
                'next_step': 'step3'
            },
            'step3': {
                'text': 'Спасибо за регистрацию, {name}! Мы отправили на {email} билет, распечатайте его.',
                'image': 'generate_ticket_handler',
                'failure_text': None,
                'handler': None,
                'next_step': None
            }
        }
    }
}

DEFAULT_ANSWER = 'Не знаю как на это ответить. ' \
                 'Могу сказать когда и где пройдет конференция, а также зарегистрировать вас. Просто спросите'

DB_CONFIG = dict(
    provider='postgres',
    user='postgres',
    password='Az123456',
    host='localhost',
    database='vk_chat_bot',
    port='5432'
)
