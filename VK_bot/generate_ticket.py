from io import BytesIO

import requests
from PIL import Image, ImageDraw, ImageFont

TEMPLATE_PATH = ''
FONT_PATH = ''
FONT_SIZE = 20

BLACK = (0, 0, 0, 255)
NAME_OFFSET = (295, 240)
EMAIL_OFFSET = (295, 280)

AVATAR_SIZE = 100
AVATAR_OFFSET = (100, 200)


def generate_ticket(name, email):
    base = Image.open('').convert('RGBA')
    font = ImageFont.truetype(FONT_PATH, FONT_SIZE)

    draw = ImageDraw.Draw(base)
    draw.text(NAME_OFFSET, name, fill=BLACK, font=font)
    draw.text(EMAIL_OFFSET, email, fill=BLACK, font=font)

    response = requests.get(url=f'https://api.adorable.io/avatars/{AVATAR_SIZE}/{email}')
    avatar_file = BytesIO(response.content)
    avatar = Image.open(avatar_file)

    base.paste(avatar, AVATAR_OFFSET)

    base.show()
    temp_file = BytesIO()
    base.save(temp_file, 'PNG')
    temp_file.seek(0)

    return temp_file
    # with open('files/ticket.png', 'wb') as file:
    #     base.save(file, 'PNG')