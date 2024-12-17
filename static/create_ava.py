from PIL import Image
from random import randint
from json import load, dump

def create_image(count, HEIGHT=16, WIDTH=16):
    color = [(255, 50, 50), (50, 255, 50), (50, 50, 255)][randint(0, 2)]
    l = [[0 for j in '_' * WIDTH] for i in '_' * HEIGHT]

    for i in range(HEIGHT):
        if HEIGHT // 2 > i:
            for j in range(WIDTH):
                    l[i][j] = randint(0, 1)
        else:
            for j in range(WIDTH):
                l[i][j] = l[HEIGHT - 1 - i][j]

    HEIGHT2 = HEIGHT**2
    WIDTH2 = WIDTH**2
    img = Image.new('RGB', (WIDTH2, HEIGHT2))
    for i in range(HEIGHT2):
        for j in range(WIDTH2):
            img.putpixel((i, j), [(255, 255, 255), color][l[i//HEIGHT][j//WIDTH]])
    img.show()
    img.save(f'static/images/{count}.png')
    return f'{count}.png'