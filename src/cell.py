from drawing import Line, Point

class Cell:
    def __init__(self, point1, point2, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = point1.x
        self.__y1 = point1.y
        self.__x2 = point2.x
        self.__y2 = point2.y
        self.__win = window

    def draw(self, tlcorner, brcorner):
        if self.has_left_wall:
            x1 = tlcorner.x
            y1 = tlcorner.y
            x2 = tlcorner.x
            y2 = brcorner.y
            p1 = Point(x1, y1)
            p2 = Point(x2, y2)
            lw = Line(p1, p2)
            self.__win.draw_line(lw, "black")

        if self.has_right_wall:
            x1 = brcorner.x
            y1 = tlcorner.y
            x2 = brcorner.x
            y2 = brcorner.y
            p1 = Point(x1, y1)
            p2 = Point(x2, y2)
            rw = Line(p1, p2)
            self.__win.draw_line(rw, "black")

        if self.has_top_wall:
            x1 = tlcorner.x
            y1 = tlcorner.y
            x2 = brcorner.x
            y2 = tlcorner.y
            p1 = Point(x1, y1)
            p2 = Point(x2, y2)
            tw = Line(p1, p2)
            self.__win.draw_line(tw, "black")

        if self.has_bottom_wall:
            x1 = tlcorner.x
            y1 = brcorner.y
            x2 = brcorner.x
            y2 = brcorner.y
            p1 = Point(x1, y1)
            p2 = Point(x2, y2)
            bw = Line(p1, p2)
            self.__win.draw_line(bw, "black")