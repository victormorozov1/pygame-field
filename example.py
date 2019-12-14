from game import Game
import pygame
import threading


class MyGame(Game):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pict_id = 0

    def handle_event(self, ev):
        if ev.type == pygame.KEYDOWN:
            if not len(self.field.objects):
                pict = pygame.image.load('r.png')
                self.pict_id = my_game.field.add_object(pict, 1, 1)

    def move_pict(self, move_x, move_y):
        my_game.field.move_object_on(self.pict_id, move_x, move_y)

    def handle_pressed(self, key):
        if key == pygame.K_RIGHT:
            self.move_pict(1, 0)
        elif key == pygame.K_LEFT:
            self.move_pict(-1, 0)
        elif key == pygame.K_UP:
            self.move_pict(0, -1)
        elif key == pygame.K_DOWN:
            self.move_pict(0, 1)


if __name__ == '__main__':
    my_game = MyGame(500, 500, sleep=0.001, bg=(122, 233, 111))
    my_game.run()
