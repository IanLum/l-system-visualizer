from lsystem import *
import turtle


class Algae(Lsystem):
    start = "A"
    productions = {"A": "AB", "B": "A"}


class Dragon(VisualLSystem):
    start = "F"
    productions = {"F": "F+G", "G": "F-G"}

    def visualize(self, steps, size=3, show_drawing=True):
        turt = self.init_turtle(show_drawing)

        for char in self.generate(steps):
            match char:
                case "F" | "G":
                    turt.forward(size)
                case "+":
                    turt.left(90)
                case "-":
                    turt.right(90)

        turtle.mainloop()
        turtle.update()


class Sierpinski(VisualLSystem):
    start = "A"
    productions = {"A": "B-A-B", "B": "A+B+A"}

    def visualize(self, steps, size=3, show_drawing=True):
        turt = self.init_turtle(show_drawing)
        turt.pu()
        turt.goto((-200, -200 * (-1) ** steps))
        turt.pd()

        for char in self.generate(steps):
            match char:
                case "A" | "B":
                    turt.forward(size)
                case "+":
                    turt.left(60)
                case "-":
                    turt.right(60)

        turtle.mainloop()
        turtle.update()


class Koch(VisualLSystem):
    start = "F++F++F"
    productions = {"F": "F-F++F-F"}

    def visualize(self, steps, size=3, show_drawing=True):
        turt = self.init_turtle(show_drawing)

        for char in self.generate(steps):
            match char:
                case "F":
                    turt.forward(size)
                case "+":
                    turt.left(60)
                case "-":
                    turt.right(60)

        turtle.mainloop()
        turtle.update()


class Plant(VisualLSystem):
    start = "X"
    productions = {"X": "F+[[X]-X]-F[-FX]+X", "F": "FF"}

    def visualize(self, steps, size=3, show_drawing=True):
        turt = self.init_turtle(show_drawing, speed_multiplier=100)
        turt.pu()
        turt.goto((0, -200))
        turt.setheading(90)
        turt.pd()
        stack = []
        for char in self.generate(steps):
            match char:
                case "F":
                    turt.forward(size)
                case "+":
                    turt.left(25)
                case "-":
                    turt.right(25)
                case "[":
                    stack.append((turt.position(), turt.heading()))
                case "]":
                    turt.pu()  # pen up, stop drawing
                    position, heading = stack.pop()
                    turt.goto(position)
                    turt.setheading(heading)
                    turt.pd()

        turtle.mainloop()
        turtle.update()


class QuadGosper(VisualLSystem):
    start = "-YF"
    productions = {
        "X": "XFX-YF-YF+FX+FX-YF-YFFX+YF+FXFXYF-FX+YF+FXFX+YF-FXYF-YF-FX+FX+YFYF-",
        "Y": "+FXFX-YF-YF+FX+FXYF+FX-YFYF-FX-YF+FXYFYF-FX-YFFX+FX+YF-YF-FX+FX+YFY",
    }

    def visualize(self, steps, size=3, show_drawing=True):
        turt = self.init_turtle(show_drawing, speed_multiplier=100)
        turt.pu()
        turt.goto((0, -200))
        turt.setheading(90)
        turt.pd()
        stack = []
        for char in self.generate(steps):
            match char:
                case "F":
                    turt.forward(size)
                case "+":
                    turt.left(90)
                case "-":
                    turt.right(90)
                case "[":
                    stack.append((turt.position(), turt.heading()))
                case "]":
                    turt.pu()  # pen up, stop drawing
                    position, heading = stack.pop()
                    turt.goto(position)
                    turt.setheading(heading)
                    turt.pd()

        turtle.mainloop()
        turtle.update()


class Weed(VisualLSystem):
    start = "F"
    productions = {"F": "FF-[XY]+[XY]", "X": "+FY", "Y": "-FX"}

    def visualize(self, steps, size=3, show_drawing=True):
        turt = self.init_turtle(show_drawing, speed_multiplier=100)
        turt.pu()
        turt.goto((0, -200))
        turt.setheading(90)
        turt.pd()
        stack = []
        for char in self.generate(steps):
            match char:
                case "F":
                    turt.forward(size)
                case "+":
                    turt.left(22.5)
                case "-":
                    turt.right(22.5)
                case "[":
                    stack.append((turt.position(), turt.heading()))
                case "]":
                    turt.pu()  # pen up, stop drawing
                    position, heading = stack.pop()
                    turt.goto(position)
                    turt.setheading(heading)
                    turt.pd()

        turtle.mainloop()
        turtle.update()
