class Shape():
    def __init__(self):
        self._area = 0
        self._volume = 0
        self._is_3d = False

class Rectangle(Shape):
    def __init__(self, length, width):
        self._area = length * width
        self._length = length
        self._width = width
    

