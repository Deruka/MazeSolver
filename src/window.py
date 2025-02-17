from tkinter import Tk, BOTH, Canvas, Button
from drawing import Line

class Window:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(master=self.__root, width=self.__width, height= self.__height)
        self.__canvas.pack(fill=BOTH)
        self.__winactive = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__restart_callback = None

    def add_restart_button(self, callback):
        # Add a restart button to the window
        self.__restart_callback = callback  # Store the callback
        restart_button = Button(self.__root, text="Restart Maze", command=self.__restart_callback)
        restart_button.pack(side="bottom", anchor="n", pady=10)
        # for button at the left, use this:
        #restart_button.pack(side="bottom", anchor="w", pady=10, padx=10)
        # for button at the right, use this:
        #restart_button.pack(side="bottom", anchor="e", pady=10, padx=10)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__winactive = True
        while self.__winactive:
            self.redraw()

    def close(self):
        self.__winactive = False
        self.__root.destroy() # Properly close the window
    
    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)