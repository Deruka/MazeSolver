from window import Window
from drawing import Point, Line

def main():
    win = Window(800, 600)
    # Create Points
    p1 = Point(50, 50)
    p2 = Point(200, 200)
    p3 = Point(600, 450)
    p4 = Point(400, 300)
    p5 = Point(325, 550)
    p6 = Point(275, 480)
    # Create Lines
    line1 = Line(p1, p2)
    line2 = Line(p3, p4)
    line3 = Line(p5, p6)
    # Draw the Lines
    win.draw_line(line1, "red")
    win.draw_line(line2, "blue")
    win.draw_line(line3, "green")
    win.wait_for_close()

main()