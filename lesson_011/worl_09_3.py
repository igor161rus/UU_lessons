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

    def make(self, resize=False, out_path=None):
        im = Image.open("postcard.jpg")
        w, h = im.size
        font_size = 32
        if resize:
            im = im.resize((w // 2, h // 2))
            font_size = font_size // 2
        draw = ImageDraw.Draw(im)
        font = ImageFont.truetype(self.font_path, font_size)
        y = im.size[1] - 340 - font.size
        x = im.size[0] // 20
        message = f'Привет, {self.name}!'
        draw.text((x, y), message, font=font, fill=ImageColor.colormap['red'])

        y = im.size[1] - 305 - font.size
        message = f'С Праздником!!!'
        draw.text((x, y), message, font=font, fill=ImageColor.colormap['red'])
        im.show()
        out_path = out_path if out_path else 'postcard_edit.jpg'
        im.save(out_path)
        print(f'Post card saved az {out_path}')


if __name__ == '__main__':
    maker = PostCardMaker(name='Настя')
    maker.make()
