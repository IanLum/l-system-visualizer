from abc import ABC, abstractmethod
import turtle


class Lsystem(ABC):
    _start: str
    _productions: dict

    def __init__(self):
        pass

    @property
    @abstractmethod
    def start(self):
        pass

    @property
    @abstractmethod
    def productions(self):
        pass

    def generate(self, steps):
        if steps == 0:
            return self.start

        res = ""
        for char in self.generate(steps - 1):
            res += self.productions.get(char, char)
        return res


class VisualLSystem(Lsystem):
    def init_turtle(self, show_drawing) -> turtle.Turtle:
        turt = turtle.Turtle()
        turt.screen.title("L System Visualizer")
        turt.speed(0)
        n = 1 if show_drawing else 0
        turtle.tracer(n, 0)  # needs tweaking
        return turt

    @abstractmethod
    def visualize(self):
        pass


class Algae(Lsystem):
    start = "A"
    productions = {"A": "AB", "B": "A"}


class Dragon(VisualLSystem):
    start = "F"
    productions = {"F": "F+G", "G": "F-G"}

    def visualize(self, steps, show_drawing=True):
        turt = self.init_turtle(show_drawing)

        for char in self.generate(steps):
            match char:
                case "F" | "G":
                    turt.forward(3)
                case "+":
                    turt.left(90)
                case "-":
                    turt.right(90)

        turtle.mainloop()
        turtle.update()


class Sierpinski(VisualLSystem):
    start = "A"
    productions = {"A": "B-A-B", "B": "A+B+A"}

    def visualize(self, steps, show_drawing=True):
        turt = self.init_turtle(show_drawing)

        for char in self.generate(steps):
            match char:
                case "A" | "B":
                    turt.forward(3)
                case "+":
                    turt.left(60)
                case "-":
                    turt.right(60)

        turtle.mainloop()
        turtle.update()
