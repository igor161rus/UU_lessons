from PIL import Image, ImageFont, ImageDraw


im = Image.open("postcard.JPG")
print(im.format, im.size, im.mode)

w, h = im.size
resized_im = im.resize((w//2, h//2))

print(resized_im.format, resized_im.size, resized_im.mode)

draw = ImageDraw.Draw(resized_im)
font = ImageFont.truetype('miamanueva.ttf', 16)

draw.text((50, 110), 'Привет!', font=font, fill=(0, 0, 0, 0))

resized_im.save('postcard_edit.jpg')
