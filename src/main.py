from window import Window
from drawing import Point, Line
from cell import Cell
from maze import Maze

def main():
    # Create window
    win = Window(1280, 920)
    # Create Maze
    m = Maze(10, 60, 17, 28, 45, 45, win)
    # break entrance and exit
    m._break_entrance_and_exit()
    # break the walls down randomly according to the seed
    m._break_walls_r(0, 0)
    # Revert all cells to not be visited
    m._reset_cells_visited()
    # Solve the maze
    m.solve()
    # wait to close the window
    win.wait_for_close()

main()