from urllib import parse
from PIL import Image

"""У каждого изображения есть какая либо ориентация сторон, например 16:9, и что бы определить то, какой
    формы изображение мы узнаем коэфицент сторон, если он больше 1.3 то это горизонтальное изображение, если
    меньше 0.7 то это вертикальное изображение, а между ними квадратное, таким образом мы подбираем наилучший
    шаблон под конкретное изображение с помощью данной функции"""\


def find_pattern(widthheight):
    if widthheight >= 1.3:
        return Image.open('patterns/pattern_horizontal.png')
    elif widthheight <= 0.7:
        return Image.open('patterns/pattern_vertical.png')
    elif  0.7 < widthheight < 1.3:
        return Image.open('patterns/pattern_square.png')


def refactor_img(list_images, directory_exit):
    for name_img in list_images: #Получает все ссылки изображений
        image = Image.open(name_img) #Открывает изображение
        width, height = image.size  #Узнает его высоту и ширину

        widthheight = width/height #высчитывает коэфицент высоты на ширину
        pattern = find_pattern(widthheight=widthheight) #Получает подходящий паттерн
        image.paste(pattern.resize((width, height)), (0, 0), pattern.resize((width, height))) #Накладывает одно изображение на другое
        unquoted_url = parse.unquote(name_img)
        path = parse.urlparse(unquoted_url).path
        name_cart = path.rstrip("/").split("/")[-1] #Получает имя файла
        image.save(directory_exit + name_cart[:name_cart.find('.')] + '-wt.png') #Сохраняет файл






