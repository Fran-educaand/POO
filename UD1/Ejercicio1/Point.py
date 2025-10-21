class Point: 
    def __init__(self, x, y, constante):
        self.x = x
        self.y = y
        self.constante = constante

    def to_string(self):
        return f'({self.x}, {self.y}, {self.constante})'
    
p = Point(2, 3, 5)
print(p.to_string())

      