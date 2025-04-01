from objects.Line import Line
from objects.display import Display

class Segment(Line):
    def __init__(self, p1, p2):
        super().__init__(p1, p2)
    
    def rasterize(self, disp):
        for i in range(self.p1.x, self.p2.x):
            for j in range(self.p1.y, self.p2.y):
                disp.set_pixel(i, j)