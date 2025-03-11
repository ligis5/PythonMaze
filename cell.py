import pygame

class Cell():
    def __init__(self, s_width, s_height, pos_in_list_x, pos_in_list_y):
        self.SCREEN_WIDTH = s_width
        self.SCREEN_HEIGHT = s_height
        self.pos_in_list_x = pos_in_list_x
        self.pos_in_list_y = pos_in_list_y
        self.left_wall = True
        self.top_wall = True
        self.right_wall = True
        self.bottom_wall = True

    def give_position(self):

        pass


