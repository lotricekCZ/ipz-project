from objects.Point import Point

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p1.diff(p2)
    