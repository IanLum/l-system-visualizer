class Lsystem:
    _start: str
    _productions: dict

    def __init__(self, start: str, productions: dict):
        self._start = start
        self._productions = productions

    def generate(self, steps):
        if steps == 0:
            return self._start

        res = ""
        for char in self.generate(steps - 1):
            res += self._productions[char]
        return res
