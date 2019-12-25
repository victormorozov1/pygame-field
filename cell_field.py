import pygame
from field import Field
from random import randrange as rd
from functions import *


class CellField(Field):
    def __init__(self, szx, szy, field_arr, field_dict, cell_sz=64, bg=(255, 255, 255)):
        super().__init__(szx, szy, bg=bg)
        self.field_arr = field_arr
        self.field_dict = field_dict
        self.cell_sz = cell_sz
        self.n = szx // cell_sz
        self.m = szy // cell_sz

    def draw_field(self, win, start=(0, 0)):
        for i in range(len(self.field_arr)):
            for j in range(len(self.field_arr[i])):
                for pos in camera_coords(i * self.cell_sz, j * self.cell_sz, self.szx, self.szy, start):
                    win.blit(self.field_dict[self.field_arr[i][j]], pos)

    def draw_objects(self, win, start=(0, 0)):
        for i in self.objects:
            for pos in camera_coords(i.rect.x, i.rect.y, self.szx, self.szy, start):
                win.blit(i.image, pos)

    def show(self, win, start=(0, 0)):
        win.fill(self.bg)
        self.draw_field(win, start=start)
        self.draw_objects(self.win, start=start)
        pygame.display.update()
