import RPi.GPIO as GPIO

import smbus2
import bme280
import time
import curses
from objects.wheel import Wheel

MOVE = 0
METEO = 1
port = 1
address = 0x76
bus = smbus2.SMBus(port)
calibration_params = bme280.load_calibration_params(bus, address)

def main(stdscr):
    stdscr.nodelay(True)  # Non-blocking input
    stdscr.clear()
    stdscr.addstr("Press UP/DOWN arrow keys to control (Press 'q' to quit)\n")

    GPIO.setmode(GPIO.BOARD)  # Use BOARD numbering (not BCM)

    

    # Define motor control pins

    right_wheel = Wheel(24, 26)
    left_wheel = Wheel(16, 18)

    right_wheel.stop()

    try:
        while True:
            key = stdscr.getch()  # Get key press
            data = bme280.sample(bus, address, calibration_params)
            stdscr.addstr(2, 0, f"Temperature: {data.temperature} C")
            stdscr.addstr(3, 0, f"Pressure: {data.pressure} Pa")
            stdscr.addstr(4, 0, f"Humidity: {data.humidity} %")
            stdscr.refresh()  # ✅ Update the terminal output

            if key == -1:  # No key pressed (fix non-blocking issue)
                left_wheel.stop()
                right_wheel.stop()
                continue

            if key == curses.KEY_UP:
                stdscr.addstr(1, 0, "Moving Forward     ")  # Extra spaces to clear text
                right_wheel.forward()
                left_wheel.forward()
            elif key == curses.KEY_DOWN:
                stdscr.addstr(1, 0, "Moving Backward    ")
                right_wheel.backward()
                left_wheel.backward()
            elif key == curses.KEY_LEFT:
                stdscr.addstr(1, 0, "Turning Left       ")
                right_wheel.forward()
                left_wheel.backward()
            elif key == curses.KEY_RIGHT:
                stdscr.addstr(1, 0, "Turning Right      ")
                right_wheel.backward()
                left_wheel.forward()

            if key == ord('q'):  # Press 'q' to quit
                break

            
            time.sleep(0.1)

    except KeyboardInterrupt:
        print("Exiting program...")

    finally:
        GPIO.cleanup()  # ✅ Proper cleanup on exit


if __name__ == "__main__": 
    curses.wrapper(main) # called with curses to get user input