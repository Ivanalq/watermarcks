from urllib import parse
from PIL import Image

def refactor_img(list_images, directory_exit):
    for name_img in list_images:
        image = Image.open(name_img)
        width, height = image.size
        if width/height >= 1.3:
            pattern = Image.open('patterns/pattern_horizontal.png')
            image.paste(pattern.resize((width, height)), (0, 0), pattern.resize((width, height)))
            unquoted_url = parse.unquote(name_img)
            path = parse.urlparse(unquoted_url).path
            name_cart = path.rstrip("/").split("/")[-1]
            image.save(directory_exit + name_cart[:name_cart.find('.')] + '-wt.png')

        if width/height <= 0.7:
            pattern = Image.open('patterns/pattern_vertical.png')
            image.paste(pattern.resize((width, height)), (0, 0), pattern.resize((width, height)))
            unquoted_url = parse.unquote(name_img)
            path = parse.urlparse(unquoted_url).path
            name_cart = path.rstrip("/").split("/")[-1]
            image.save(directory_exit + name_cart[:name_cart.find('.')] + '-wt.png')

        if 0.7 < width/height < 1.3:
            pattern = Image.open('patterns/pattern_square.png')
            image.paste(pattern.resize((width, height)), (0, 0), pattern.resize((width, height)))
            unquoted_url = parse.unquote(name_img)
            path = parse.urlparse(unquoted_url).path
            name_cart = path.rstrip("/").split("/")[-1]
            image.save(directory_exit + name_cart[:name_cart.find('.')] + '-wt.png')



