from drawing import Line, Point

class Cell:
    def __init__(self, point1, point2, window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = point1.x
        self.__y1 = point1.y
        self.__x2 = point2.x
        self.__y2 = point2.y
        self.__win = window
        self.visited = False

    def draw(self, tlcorner, brcorner):
        self.__x1 = tlcorner.x
        self.__y1 = tlcorner.y
        self.__x2 = brcorner.x
        self.__y2 = brcorner.y

        if self.__win is None:
            return

        p1 = Point(self.__x1, self.__y1) # top left point
        p2 = Point(self.__x1, self.__y2) # top right point
        p3 = Point(self.__x2, self.__y1) # bottom left point
        p4 = Point(self.__x2, self.__y2) # bottom right point

        lw = Line(p1, p2) # left wall
        rw = Line(p3, p4) # right wall
        tw = Line(p1, p3) # top wall
        bw = Line(p2, p4) # bottom wall
        
        color = "black" if self.has_left_wall else "#d9d9d9"
        self.__win.draw_line(lw, color)

        color = "black" if self.has_right_wall else "#d9d9d9"
        self.__win.draw_line(rw, color)

        color = "black" if self.has_top_wall else "#d9d9d9"
        self.__win.draw_line(tw, color)

        color = "black" if self.has_bottom_wall else "#d9d9d9"
        self.__win.draw_line(bw, color)
    
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
