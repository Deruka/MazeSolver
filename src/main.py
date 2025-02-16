from window import Window
from drawing import Point, Line
from cell import Cell
from maze import Maze

def main():
    # Create window
    win = Window(800, 600)
    # Create Maze
    m = Maze(10, 10, 6, 6, 40, 40, win)
    # break entrance and exit
    m._break_entrance_and_exit()
    # wait to close the window
    win.wait_for_close()

main()


def old_main_for_save():
    win = Window(800, 600)
    # Create Points
    p1 = Point(50, 50)
    p2 = Point(200, 200)
    p3 = Point(200, 50)
    p4 = Point(350, 200)
    p5 = Point(350, 50)
    p6 = Point(500, 200)
    # Create Cells
    c1 = Cell(p1, p2, win)
    c2 = Cell(p3, p4, win)
    c3 = Cell(p5, p6, win)
    c1.has_right_wall = False
    c2.has_left_wall = False
    c2.has_right_wall = False
    c3.has_left_wall = False
    c3.has_bottom_wall = False
    # Draw Cells
    c1.draw(p1, p2)
    c2.draw(p3, p4)
    c3.draw(p5, p6)
    # move through cells
    c1.draw_move(c2)
    c2.draw_move(c3)
    # wait to close the window
    win.wait_for_close()