from lsystem import Lsystem

algae = Lsystem(start="A", productions={"A": "AB", "B": "A"})
print(algae.generate(6))
