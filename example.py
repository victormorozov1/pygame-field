from game import Game
import pygame
import threading


class MyGame(Game):
    def handle_event(self, ev):
        if ev.type == pygame.KEYDOWN:
            if not len(self.field.objects):
                pict = pygame.image.load('r.png')
                my_game.field.add_object(pict, 1, 1)

    def handle_pressed(self, key):
        if key == pygame.K_RIGHT:
            my_game.field.move_object_on(my_game.field.objects[0].id, 1, 0)
        elif key == pygame.K_LEFT:
            my_game.field.move_object_on(my_game.field.objects[0].id, -1, 0)
        elif key == pygame.K_UP:
            my_game.field.move_object_on(my_game.field.objects[0].id, 0, -1)
        elif key == pygame.K_DOWN:
            my_game.field.move_object_on(my_game.field.objects[0].id, 0, 1)


if __name__ == '__main__':
    my_game = MyGame(500, 500, sleep=0.001, bg=(122, 233, 111))
    my_game.run()
