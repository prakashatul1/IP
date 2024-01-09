from abc import abstractmethod, ABC


class GraphicShape(ABC):

    def __int__(self):
        super().__init__()

    @abstractmethod
    def calcarea(self):
        pass


class Circle(GraphicShape):

    def __init__(self, radius):
        self.radius = radius

    def calcarea(self):
        return 3.14 * (self.radius ** 2)


c1 = Circle(radius=10)
print(c1.calcarea())
