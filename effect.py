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







im = Image.open('cat.jpg')
pix = im.load()
border(pix, 10, (234, 567, 123), 'cat2.jpg')