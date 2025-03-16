import pygame

class Cell():
    def __init__(self, screen, cell_pos_x, cell_pos_y, cell_size):
        self.pos_x = cell_pos_x
        self.pos_y = cell_pos_y
        self.cell_size = cell_size
        self.screen = screen
        self.color = (100, 60, 80)
        self.walls = {"top": True, "left": True, "bottom": True, "right": True}
        self.neighbours = {}


    def draw_cell(self):
        #top
        if self.walls["top"]:
            pygame.draw.line(self.screen, self.color, (self.pos_x, self.pos_y), (self.pos_x + self.cell_size, self.pos_y), 2)
        # left
        if self.walls["left"]:
            pygame.draw.line(self.screen, self.color, (self.pos_x, self.pos_y), (self.pos_x, self.pos_y + self.cell_size),
                         2)
        # bottom
        if self.walls["bottom"]:
            pygame.draw.line(self.screen, self.color, (self.pos_x + self.cell_size, self.pos_y  + self.cell_size), (self.pos_x, self.pos_y  + self.cell_size),
                         2)
        # right
        if self.walls["right"]:
            pygame.draw.line(self.screen, self.color, (self.pos_x + self.cell_size, self.pos_y),
                         (self.pos_x + self.cell_size, self.pos_y + self.cell_size),
                         2)
    def set_wall_status(self, top, left, bottom, right):
        self.top = top
        self.left = left
        self. bottom = bottom
        self.right = right

    def set_neighbours(self, neighbours):
        self.neighbours = neighbours

    def set_color(self, color):
        self.color = color






