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
    def init_turtle(self, show_drawing, speed_multiplier=1) -> turtle.Turtle:
        turt = turtle.Turtle()
        turt.screen.title("L System Visualizer")
        turt.speed(0)
        n = speed_multiplier if show_drawing else 0
        turtle.tracer(n, 0)  # needs tweaking
        return turt

    @abstractmethod
    def visualize(self):
        pass
