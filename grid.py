import numpy as np
from cell import Cell
import random

class Grid():
    def __init__(self, screen, width, height, cell_size):
        self.screen = screen
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.grid = []
        self.cells = []

    # Creating 2D array
    def grid_array(self):
        outer_wall_zone = self.cell_size / 2
        i = outer_wall_zone
        x = []
        while i < self.width - outer_wall_zone:
            x.append(i)
            i += self.cell_size
        j = outer_wall_zone
        y = []
        while j < self.height - outer_wall_zone:
            y.append(j)
            j += self.cell_size

        x_array = np.array(x)
        y_array = np.array(y)
        self.grid = np.meshgrid(x_array, y_array)

    def create_cells(self):
        for i in range(len(self.grid[0])):
            for j in range(len(self.grid[1])):
                self.cells.append(Cell(self.screen, self.grid[0][i][j], self.grid[1][i][j], self.cell_size))

    def find_neighbours(self):
        # finding neighbours and assigning neighbouring cells.
        # i for number in row, j for number in column and multiply by row or column to get correct cell, because cells are in 1D array
        r = len(self.grid[0][0])
        c = len(self.grid[1][0])
        for i in range(r):
            for j in range(c):
                neighbours = {"top": None, "left": None, "bottom": None, "right": None}
                if i < 0 or i >= r or j < 0 or j >= c:
                    neighbours.update({"top": None, "left": None, "bottom": None, "right": None})
                if i > 0 and i < r - 1:
                    neighbours.update({"left": (self.cells[(i - 1) + j * c]), "right": (self.cells[(i + 1) + j * c])})
                if j > 0 and j < c - 1:
                    neighbours.update({"top": (self.cells[i + (j - 1) * r]), "bottom": (self.cells[i + (j + 1) * r])})
                self.cells[i + j * r].set_neighbours(neighbours)

    def cells_change_status(self):
        i = 0
        while i < len(self.cells):
            self.cells[i].draw_cell()
            r = random.randint(0, 10)
            if r > 7:
                self.cells[i].set_wall_status(random.choice([True, False]), random.choice([True, False]),
                                         random.choice([True, False]), random.choice([True, False]))
            i += 1
    def change_cell_color(self):
        self.cells[10].set_color((0,100,0))
        self.cells[10].neighbours["right"].set_color((100, 100 ,100))

