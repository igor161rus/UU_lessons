import pygame as pg
from player import Minion

screen = pg.display.set_mode((800, 600))
player = Minion()

fps = pg.time.Clock()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

    screen.fill('black')
    fps.tick(60)
    player.update(screen)
    pg.display.update()


