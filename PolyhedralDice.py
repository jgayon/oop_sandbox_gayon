import abc
import random
class Die(abc.ABC):
    def __init__(self) -> None:
        self.face: int
        self.roll()

    def __repr__(self) -> str:
        return f"{self.face}"

@abc.abstractmethod
def roll(self) -> None:
    ...

class D4(Die):
    def roll(self)->None:
        self.face = random.choice((1,2,3,4))
class D6(Die):
    def roll(self) -> None:
        self.face = random.randint(1, 6)
class D8(Die):
    def roll(self)->None:
        self.face = int(random.random()*8)

d4 =D4()
print(d4.face)
d6 = D6()
print(d6.face)
d8 =D8()
print(d8.face)