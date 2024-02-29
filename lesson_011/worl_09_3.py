import os.path

from PIL import Image, ImageFont, ImageDraw, ImageColor


class PostCardMaker:
    def __init__(self, name, template=None, font_path=None):
        self.name = name
        self.template = "postcard.jpg" if template is None else template
        if font_path is None:
            self.font_path = os.path.join('fonts', 'miamanueva.ttf')
        else:
            self.font_path = font_path

    def make(self):
        im = Image.open("postcard.jpg")

        w, h = im.size
        resized_im = im.resize((w // 2, h // 2))

        draw = ImageDraw.Draw(resized_im)

        font = ImageFont.truetype(self.font_path, 16)

        message = f'Привет, {self.name}!'
        draw.text((15, 110), message, font=font, fill=ImageColor.colormap['red'])

        resized_im.show()
        # resized_im.save('postcard_edit.jpg')


if __name__ == '__main__':
    maker = PostCardMaker(name='Настя')
    maker.make()
