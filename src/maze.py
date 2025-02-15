from cell import Cell
from drawing import Point, Line
import time

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self._cells = []
        self._create_cells()

    def _create_cells(self):
        for i in range(self.__num_cols):
            cell_list = []
            x1 = self.__x1 + (i * self.__cell_size_x)
            x2 = x1 + self.__cell_size_x

            for j in range(self.__num_rows):
                y1 = self.__y1 + (j * self.__cell_size_y)
                y2 = y1 + self.__cell_size_y
                p1 = Point(x1, y1)
                p2 = Point(x2, y2)
                new_cell = Cell(p1, p2, self.__win)
                cell_list.append(new_cell)

            self._cells.append(cell_list)
        
        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self._draw_cell(i, j)
    
    def _draw_cell(self, i, j):
        x1 = self.__x1 + (i * self.__cell_size_x)
        x2 = x1 + self.__cell_size_x
        y1 = self.__y1 + (j * self.__cell_size_y)
        y2 = y1 + self.__cell_size_y
        p1 = Point(x1, y1)
        p2 = Point(x2, y2)
        self._cells[i][j].draw(p1, p2)
        self._animate()

    def _animate(self):
        self.__win.redraw()
        time.sleep(0.05)