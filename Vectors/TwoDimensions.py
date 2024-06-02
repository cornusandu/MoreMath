class Vector2:
    __slots__ = {'x', 'y', 'pos', 'weakref'}

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
        self.pos: tuple = x, y

    def __repr__(self):
        return f"Vector2(x: {self.x}, y: {self.y})"

    def __eq__(self, other):
        return self.pos == other.pos

    def __gt__(self, other):
        return self.pos > other.pos

    def __ge__(self, other):
        return self.pos >= other.pos

    @classmethod
    def get_absolute(cls):
        return Vector2(0, 0)
def main(*_) -> None:
    MyVector: Vector2 = Vector2.get_absolute()
    print(MyVector)

if __name__ == '__main__':
    main()
