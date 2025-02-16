from cell import Cell
from drawing import Point
import time
import random

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
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

        if not seed:
            self._seed = random.seed(seed)
        else:
            self._seed = seed

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

    def _is_valid_position(self, i, j):
        return (
            i >= 0 and 
            i < self.__num_cols and 
            j >= 0 and 
            j < self.__num_rows
        )

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            possible_directions = []
            # left cell
            if self._is_valid_position(i- 1, j) and not self._cells[i - 1][j].visited:
                possible_directions.append((i - 1, j))
            # right cell
            if self._is_valid_position(i + 1, j) and not self._cells[i + 1][j].visited:
                possible_directions.append((i + 1, j))
            # top cell
            if self._is_valid_position(i, j - 1) and not self._cells[i][j - 1].visited:
                possible_directions.append((i, j - 1))
            # bottom cell
            if self._is_valid_position(i, j + 1) and not self._cells[i][j + 1].visited:
                possible_directions.append((i, j + 1))
            if len(possible_directions) == 0:
                if self.__win is not None:
                    self._draw_cell(i, j)
                return
            # choose new direction
            direction = random.choice(possible_directions)
            new_i, new_j = direction
            # If new_i is less than i, we moved left
            if new_i < i:
                self._cells[i][j].has_left_wall = False
                self._cells[new_i][new_j].has_right_wall = False
            # If new_i is greater than i, we moved right
            elif new_i > i:
                self._cells[i][j].has_right_wall = False
                self._cells[new_i][new_j].has_left_wall = False
            # If new_j is less than j, we moved up
            elif new_j < j:
                self._cells[i][j].has_top_wall = False
                self._cells[new_i][new_j].has_bottom_wall = False
            # If new_j is greater than j, we moved down
            elif new_j > j:
                self._cells[i][j].has_bottom_wall = False
                self._cells[new_i][new_j].has_top_wall = False
            self._break_walls_r(new_i, new_j)

    def _reset_cells_visited(self):
        for list in self._cells:
            for cell in list:
                cell.visited = False
    
    def solve(self):
        return self._solve_r(0, 0)
    
    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if self._cells[i][j] == self._cells[self.__num_cols - 1][self.__num_rows- 1]:
            return True
        # Moving into each direction to solve the randomized Maze
        # Moving down:
        if (
            self._is_valid_position(i, j + 1) and 
            not self._cells[i][j + 1].visited and 
            not self._cells[i][j].has_bottom_wall and 
            not self._cells[i][j + 1].has_top_wall
        ):
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            valid = self._solve_r(i, j + 1)
            if valid:
                return valid
            self._cells[i][j + 1].draw_move(self._cells[i][j], undo=True)
        # Moving up:
        if (
            self._is_valid_position(i, j - 1) and 
            not self._cells[i][j - 1].visited and 
            not self._cells[i][j].has_top_wall and 
            not self._cells[i][j - 1].has_bottom_wall
        ):
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            valid = self._solve_r(i, j - 1)
            if valid:
                return valid
            self._cells[i][j - 1].draw_move(self._cells[i][j], undo=True)
        # Moving left:
        if (
            self._is_valid_position(i - 1, j) and 
            not self._cells[i - 1][j].visited and 
            not self._cells[i][j].has_left_wall and 
            not self._cells[i - 1][j].has_right_wall
        ):
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            valid = self._solve_r(i - 1, j)
            if valid:
                return valid
            self._cells[i - 1][j].draw_move(self._cells[i][j], undo=True)
        # Moving right:
        if (
            self._is_valid_position(i + 1, j) and 
            not self._cells[i + 1][j].visited and 
            not self._cells[i][j].has_right_wall and 
            not self._cells[i + 1][j].has_left_wall
        ):
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            valid = self._solve_r(i + 1, j)
            if valid:
                return valid
            self._cells[i + 1][j].draw_move(self._cells[i][j], undo=True)
        # no path worked
        return False