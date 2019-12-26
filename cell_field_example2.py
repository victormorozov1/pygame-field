from game import Game
import pygame
from random import randrange as rd
from functions import *

SPEED = 4


def not_zero(p):
    if p > 0:
        return 1
    return 0


class MyGame(Game):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _move_pict(self, move_x, move_y):
        mario = my_game.field.get_object_by_id(mar_id)
        x, y = mario.rect.x + move_x, mario.rect.y + move_y

        arr1 = [x // self.field.cell_sz, x // self.field.cell_sz + not_zero(x % self.field.cell_sz)]
        arr2 = [y // self.field.cell_sz, y // self.field.cell_sz + not_zero(y % self.field.cell_sz)]

        for i in arr1:
            for j in arr2:
                if self.field.field_arr[i % self.field.n][j % self.field.m] == '#':
                    return

        mario.rect.x = (mario.rect.x + move_x) % self.field.szx
        mario.rect.y = (mario.rect.y + move_y) % self.field.szy

    def move_pict(self, move_x, move_y):
        x, y = 0, 0
        while x < abs(move_x) or y < abs(move_y):
            if x < abs(move_x):
                self._move_pict(sign(move_x), 0)
                x += 1
            if y < abs(move_y):
                self._move_pict(0, sign(move_y))
                y += 1

    def handle_pressed(self, key):
        if key == pygame.K_RIGHT:
            self.move_pict(SPEED, 0)
        elif key == pygame.K_LEFT:
            self.move_pict(-SPEED, 0)
        elif key == pygame.K_UP:
            self.move_pict(0, -SPEED)
        elif key == pygame.K_DOWN:
            self.move_pict(0, SPEED)

    def free_cell(self):
        x, y = rd(0, self.field.n), rd(0, self.field.m)
        while self.field.field_arr[x][y] == '#':
            x, y = rd(0, self.field.n), rd(0, self.field.m)
        return x * self.field.cell_sz, y * self.field.cell_sz

    def game_iteration(self):
        mario = my_game.field.get_object_by_id(mar_id)
        self.field.show(self.field.win)


if __name__ == '__main__':
    global mar_id

    field_arr = load_level(int(input('choose level from 1 to 4')))

    field_dict = dict()
    field_dict['.'] = pygame.image.load('data/pictures/grass.png')
    field_dict['#'] = pygame.image.load('data/pictures/box.png')

    my_game = MyGame(550, 550, sleep=0.001, cell_field_sz=50, bg=(122, 233, 111), field='cell field',
                     field_arr=field_arr,
                     field_dict=field_dict)

    mar_id = my_game.field.add_object(pygame.transform.scale(pygame.image.load('data/pictures/mar.png'), (50, 50)), *my_game.free_cell())

    my_game.run()
