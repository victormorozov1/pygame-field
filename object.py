import pygame


class Object(pygame.sprite.Sprite):
    def __init__(self, id, picture, x, y, group):
        super().__init__(group)
        self.id = id
        self.picture = picture
        self.rect = self.picture.get_rect()
        self.image = picture
        self.rect.x = x
        self.rect.y = y
