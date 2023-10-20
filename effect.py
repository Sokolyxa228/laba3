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








im = Image.open('cat.jpg')
pix = im.load()
border(pix, 10, (234, 567, 123), 'cat2.jpg')