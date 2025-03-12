import pygame

class Cell():
    def __init__(self, screen, cell_pos, cell_size):
        self.pos_x = cell_pos["x"]
        self.pos_y = cell_pos["y"]
        self.cell_size = cell_size
        self.screen = screen
        self.color = (100, 60, 80)
        self.top = True
        self.left = True
        self.bottom = True
        self.right = True

    def draw_cell(self):
        #top
        pygame.draw.line(self.screen, self.color, (self.pos_x, self.pos_y), (self.pos_x + self.cell_size, self.pos_y), 2)
        # left
        pygame.draw.line(self.screen, self.color, (self.pos_x, self.pos_y), (self.pos_x, self.pos_y + self.cell_size),
                         2)
        # bottom
        pygame.draw.line(self.screen, self.color, (self.pos_x + self.cell_size, self.pos_y  + self.cell_size), (self.pos_x, self.pos_y  + self.cell_size),
                         2)
        # right
        pygame.draw.line(self.screen, self.color, (self.pos_x + self.cell_size, self.pos_y),
                         (self.pos_x + self.cell_size, self.pos_y + self.cell_size),
                         2)
