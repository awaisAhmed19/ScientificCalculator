import pygame as py
py.init()

WIDTH = 520
HEIGHT = 700
SIZE = (WIDTH, HEIGHT)

screen = py.display.set_mode(SIZE)
clock = py.time.Clock()

BLACK = (0, 0, 0, 0)

while True:
    for e in py.event.get():
        if e.type == py.QUIT:
            exit()

    screen.fill(BLACK)
    py.draw.circle(screen, (0, 255, 0), (WIDTH/2, HEIGHT/2), 30)

    py.display.flip()
    clock.tick(30)

py.quit()
