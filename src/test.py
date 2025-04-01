import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)  
piezo_pin = 32  # PWM pin connected to buzzer
GPIO.setup(piezo_pin, GPIO.OUT)

pi_pwm = GPIO.PWM(piezo_pin, 1000)  
pi_pwm.start(0)  

DURATION = {2: 0.5, 4: 0.25, 8: 0.125, 16: 0.0625}

NOTES = {
    'A4': 440.00, 'B4': 493.88, 'C4': 261.63, 'CS4': 277.18, 'D4': 293.66,
    'DS4': 311.13, 'E4': 329.63, 'F4': 349.23, 'FS4': 369.99, 'G4': 392.00,
    'GS4': 415.30, 'A5': 880.00, 'AS5': 932.33, 'B5': 987.77, 'C5': 1046.50,
    'CS5': 1108.73, 'D5': 587.33, 'DS5': 622.25, 'E5': 659.26, 'F5': 698.46,
    'FS5': 739.99, 'G5': 783.99, 'GS5': 830.61
}

melody = [
    ('D5', 4), ('E5', 4), ('A4', 4), ('E5', -4), ('FS5', -4),
    ('A5', 16), ('G5', 16), ('FS5', 8), ('D5', -4), ('E5', -4), ('A4', 2),
]

try:
        for note, duration in melody:
            if note == 'REST':
                time.sleep(DURATION[abs(duration)])
            else:
                freq = NOTES[note]
                pi_pwm.ChangeFrequency(freq)  
                pi_pwm.ChangeDutyCycle(50)  
                time.sleep(DURATION[abs(duration)] * (1.5 if duration < 0 else 1))  

            time.sleep(0.01)

finally:
    pi_pwm.stop()
    GPIO.cleanup()