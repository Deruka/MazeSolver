from window import Window
from drawing import Point, Line
from cell import Cell

def main():
    win = Window(800, 600)
    # Create Points
    p1 = Point(50, 50)
    p2 = Point(200, 200)
    p3 = Point(200, 200)
    p4 = Point(350, 350)
    p5 = Point(350, 350)
    p6 = Point(500, 500)
    # Create Lines
    line1 = Line(p1, p2)
    line2 = Line(p3, p4)
    line3 = Line(p5, p6)
    # Draw the Lines
    win.draw_line(line1, "red")
    win.draw_line(line2, "blue")
    win.draw_line(line3, "green")
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
    c1.draw(Point(50, 50), Point(200, 200))
    c2.draw(Point(200, 50), Point(350, 200))
    c3.draw(Point(350, 50), Point(500, 200))
    # wait to close the window
    win.wait_for_close()

main()