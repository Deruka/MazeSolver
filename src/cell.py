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
        self.__x1 = tlcorner.x
        self.__y1 = tlcorner.y
        self.__x2 = brcorner.x
        self.__y2 = brcorner.y
        if self.has_left_wall:
            p1 = Point(self.__x1, self.__y1)
            p2 = Point(self.__x1, self.__y2)
            lw = Line(p1, p2)
            self.__win.draw_line(lw, "black")

        if self.has_right_wall:
            p1 = Point(self.__x2, self.__y1)
            p2 = Point(self.__x2, self.__y2)
            rw = Line(p1, p2)
            self.__win.draw_line(rw, "black")

        if self.has_top_wall:
            p1 = Point(self.__x1, self.__y1)
            p2 = Point(self.__x2, self.__y1)
            tw = Line(p1, p2)
            self.__win.draw_line(tw, "black")

        if self.has_bottom_wall:
            p1 = Point(self.__x1, self.__y2)
            p2 = Point(self.__x2, self.__y2)
            bw = Line(p1, p2)
            self.__win.draw_line(bw, "black")
    
    def get_center_point(self):
        center_x = (self.__x1 + self.__x2) / 2
        center_y = (self.__y1 + self.__y2) / 2
        return Point(center_x, center_y)

    def draw_move(self, to_cell, undo=False):
        selfcenter = self.get_center_point()
        cellcenter = to_cell.get_center_point()

        linemove = Line(selfcenter, cellcenter)
        if undo:
            self.__win.draw_line(linemove, "gray")
        else:
            self.__win.draw_line(linemove, "red")
