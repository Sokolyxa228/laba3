from PIL import Image


def border(pix, thickness, color, name):
    # Функция рисует рамку вокруг изображения выбранной толщины и цвета
    x, y = im.size
    for i in range(thickness):
        for j in range(y):
            pix[i, j] = color[0], color[1], color[2]
            pix[x - i - 1, y - j - 1] = color[0], color[1], color[2]
    for i in range(x):
        for j in range(thickness):
            pix[i, j] = color[0], color[1], color[2]
            pix[x - i - 1, y - j - 1] = color[0], color[1], color[2]
    im.save(f'{name}')
def color_reduct(pix, name):
    from math import log2, ceil
    # Уменьшает количество различных цветов до 9
    x, y = im.size
    for i in range(x):
        for j in range(y):
            r, g, b = pix[i, j]
            if r != 0 and b != 0 and g != 0:
                pix[i, j] = ceil(log2(r)) * 32, int(log2(g)) * 32, int(log2(b)) * 32
    im.save(f'{name}')
def white(name):
    # Негатив в черно-белом формате
    x, y = im.size
    for i in range(x):
        for j in range(y):
            r, g, b = pix[i, j]
            sr = (r + g + b) // 3
            pix[i, j] = 255 - sr, 255 - sr, 255 - sr
    im.save(f'{name}')
def collage(name):
    # Создает коллаж, разрезая изображение на 4 части и меняя их местами
    x, y = im.size
    im1 = Image.new('RGB', (x // 2, y // 2), (0, 0, 0))
    im2 = Image.new('RGB', (x // 2, y // 2), (0, 0, 0))
    im3 = Image.new('RGB', (x // 2, y // 2), (0, 0, 0))
    im4 = Image.new('RGB', (x // 2, y // 2), (0, 0, 0))
    pict1, pict2, pict3, pict4 = im1.load(), im2.load(), im3.load(), im4.load()
    for i in range(x // 2):
        for j in range(y // 2):
            r, g, b = pix[i, j]
            pict1[i, j] = r, g, b
    for i in range(x // 2, x):
        for j in range(y // 2):
            r, g, b = pix[i, j]
            pict2[i - 1 - x // 2, j] = r, g, b
    for i in range(x // 2):
        for j in range(y // 2, y):
            r, g, b = pix[i, j]
            pict3[i, j - y // 2 - 1] = r, g, b
    for i in range(x // 2, x):
        for j in range(y // 2, y):
            r, g, b = pix[i, j]
            pict4[i - 1 - x // 2, j - y // 2 - 1] = r, g, b
    im.paste(im4, (0, 0))
    im.paste(im1, (x // 2, y // 2))
    im.paste(im3, (x // 2, 0))
    im.paste(im2, (0, y // 2))
    im.save(f'{name}')
def delet(start, n, name):
    # Функция сохраняет каждый n символ, начиная со start
    x, y = im.size
    im1 = Image.new('RGB', (x, y), (0, 0, 0))
    pict = im1.load()
    im2 = Image.new('RGB', (start, y), (0, 0, 0))
    pict2 = im2.load()
    x1, y1 = im2.size
    for i in range(x1):
        for j in range(y1):
            r, g, b = pix[i, j]
            pict2[i, j] = r, g, b
    for i in range(start, x, n):
        for j in range(0, y, 2):
            r, g, b = pix[i, j]
            pict[i, j] = r, g, b
    im1.paste(im2, (0, 0))
    im1.save(f'{name}')







im = Image.open('cat.jpg')
pix = im.load()
border(pix, 10, (234, 567, 123), 'cat2.jpg')