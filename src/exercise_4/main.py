from board import SCL, SDA
import busio

# Import the SSD1306 module.
import adafruit_ssd1306

i2c = busio.I2C(SCL, SDA)
display = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

from objects.Point import Point
import math
import time
base_y = 39
amplitude = 25
coef = math.pi/64
points = [0 for i in range(128)]

# display = Display(128, 64)
index = 0

while True:
    display.fill(0)
    points = [math.sin(index * coef)*amplitude + base_y] + points
    points = points[0:128]
    for i in range(128):
        display.pixel(i, int(points[i]), 1)
    for i in range(0, 128, 2):
        display.pixel(i, base_y, 1)
    index += 2
    display.show()
    # time.sleep(0.05)
# display.draw_text("Hello, World!", 0, 0, 1)