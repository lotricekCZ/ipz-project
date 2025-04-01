import RPi.GPIO as GPIO

class Wheel:
    def __init__(self, _forward_pin_num, _back_pin_num):
        self.forward_pin_num = _forward_pin_num
        self.back_pin_num = _back_pin_num
        GPIO.setup(self.forward_pin_num, GPIO.OUT)
        GPIO.setup(self.back_pin_num, GPIO.OUT)

    def stop(self):
        GPIO.output(self.forward_pin_num, GPIO.LOW)
        GPIO.output(self.back_pin_num, GPIO.LOW)
    
    def forward(self):
        GPIO.output(self.forward_pin_num, GPIO.HIGH)
        GPIO.output(self.back_pin_num, GPIO.LOW)

    def backward(self):
        GPIO.output(self.forward_pin_num, GPIO.LOW)
        GPIO.output(self.back_pin_num, GPIO.HIGH)