from PIL import Image


def refactor_img(list_images):
    for name_img in list_images:
        image = Image.open(name_img)
        width, height = image.size
        if width/height >= 1.3:
            pattern = Image.open('patterns/pattern_horizontal.png')
            image.paste(pattern.resize((width, height)), (0, 0), pattern.resize((width, height)))
            image.save(name_img[:name_img.find('.')] + '_paste.png')

        if width/height <= 0.7:
            pattern = Image.open('patterns/pattern_vertical.png')
            image.paste(pattern.resize((width, height)), (0, 0), pattern.resize((width, height)))
            image.save(name_img[:name_img.find('.')] + '_paste.png')

        if 0.7 < width/height < 1.3:
            pattern = Image.open('patterns/pattern_square.png')
            image.paste(pattern.resize((width, height)), (0, 0), pattern.resize((width, height)))
            image.save(name_img[:name_img.find('.')] + '_paste.png')
