from abc import ABC, abstractmethod


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
    @abstractmethod
    def visualize(self):
        pass


class Algae(Lsystem):
    start = "A"
    productions = {"A": "AB", "B": "A"}


class Dragon(VisualLSystem):
    start = "F"
    productions = {"F": "F+G", "G": "F-G"}

    def visualize(self):
        print("TBD!")
