from cell import Cell
from drawing import Point
import time

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
        if num_rows <= 0 or num_cols <= 0:
            raise ValueError("Number of rows and columns must be positive")
        if cell_size_x <= 0 or cell_size_y <= 0:
            raise ValueError("Cell sizes must be positive")
        if x1 < 0 or y1 < 0:
            raise ValueError("Starting positions must be non-negative")
        
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
        
        if self.__win is not None:
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

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        if self.__win is not None:
            self._draw_cell(0, 0)

        self._cells[self.__num_cols - 1][self.__num_rows- 1].has_bottom_wall = False
        if self.__win is not None:
            self._draw_cell(self.__num_cols - 1, self.__num_rows - 1)
