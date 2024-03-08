import pygame as pg
import logging

logger1 = logging.getLogger('MovingLoader')
logging.basicConfig(
    level=logging.INFO,
    # handlers=[logging.FileHandler('moving_loader.log', mode='w', encoding='utf-8')],
)
logger1.setLevel(logging.INFO)


class Minion(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.transform.scale(pg.image.load('../images/kevin.png'),
                                        (50, 62.5))
        self.rect = self.image.get_rect()

    def move(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_s]:
            self.rect.y += 1
        if keys[pg.K_w]:
            self.rect.y -= 1
        if keys[pg.K_d]:
            self.rect.x += 1
        if keys[pg.K_a]:
            self.rect.x -= 1

    def moving_loader(self):
        keys = pg.key.get_pressed()
        if any([keys[pg.K_s], keys[pg.K_w], keys[pg.K_d], keys[pg.K_a]]):
            logger1.info(f'Произошло движение: {self.rect.x}, {self.rect.y}')

    def update(self, screen):
        self.move()
        self.moving_loader()
        pg.draw.rect(screen, 'red', self.rect, 1)
        screen.blit(self.image, self.rect)
