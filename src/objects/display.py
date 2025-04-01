from board import SCL, SDA
import busio
import adafruit_ssd1306

class Display: 

    def __init__(self, width, height):
        self.i2c = busio.I2C(SCL, SDA)
        self.set_dimensions(width, height)
        self.clear()
        self.show()

    def set_dimensions(self, width, height):
        self.display = adafruit_ssd1306.SSD1306_I2C(width, height, self.i2c)

    def clear(self):
        self.display.fill(0)

    def set_pixel(self, x, y, value):
        self.display.pixel(x, y, value)

    def draw_cirle():
        pass
    
    def draw_text(self, x, y, message, col): # not working yet
        self.display.text(message, x, y, color=col)
    
    def fill(self, color):
        self.display.fill(color)

    def show(self):
        self.display.show()
