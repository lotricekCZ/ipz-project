from picamzero import Camera
import RPi.GPIO as GPIO
import time
import curses
from objects.wheel import Wheel

GPIO.setmode(GPIO.BOARD)  # Use BOARD numbering (not BCM)
# GPIO.setwarnings(False)
GPIO.setup(10, GPIO.IN)
cam = Camera()
cam.video_size = (640, 480)
def main(stdscr):
    recording = False
    alarm = False
    stdscr.nodelay(True)  # Non-blocking input
    stdscr.clear()
    stdscr.addstr("Press UP/DOWN arrow keys to control (Press 'q' to quit)\n")


    

    # Define motor control pins

    right_wheel = Wheel(24, 26)
    left_wheel = Wheel(16, 18)

    right_wheel.stop()

    try:
        while True:
            key = stdscr.getch()  # Get key press
            if key == -1:  # No key pressed (fix non-blocking issue)
                left_wheel.stop()
                right_wheel.stop()
                
                continue
            if key == ord('a'):
                stdscr.addstr(1, 0, "Alarm         ")  # Extra spaces to clear text
                recording = False
                alarm = True
            if key == curses.KEY_UP:
                stdscr.addstr(1, 0, "Moving Forward     ")  # Extra spaces to clear text
                cam.stop_recording()
                recording = False
                alarm = False
                right_wheel.forward()
                left_wheel.forward()
            elif key == curses.KEY_DOWN:
                stdscr.addstr(1, 0, "Moving Backward    ")
                cam.stop_recording()
                recording = False
                alarm = False
                right_wheel.backward()
                left_wheel.backward()
            elif key == curses.KEY_LEFT:
                stdscr.addstr(1, 0, "Turning Left       ")
                cam.stop_recording()
                recording = False
                alarm = False
                right_wheel.forward()
                left_wheel.backward()
            elif key == curses.KEY_RIGHT:
                stdscr.addstr(1, 0, "Turning Right      ")
                cam.stop_recording()
                recording = False
                alarm = False
                right_wheel.backward()
                left_wheel.forward()

            if key == ord('q'):  # Press 'q' to quit
                break
            stdscr.addstr(2, 0, "                     ")
            
            if GPIO.input(10):
                stdscr.addstr(2, 0, "TRIGGER              ")
                if(alarm == True and recording == False):
                    cam.start_recording(f"alarm_{time.strftime('%Y-%m-%dT%H:%M:%S')}.mp4")
                    stdscr.addstr(1, 0, "Record              ")
                    recording = True
            time.sleep(0.1)

    except KeyboardInterrupt:
        print("Exiting program...")

    finally:
        cam.stop_recording()
        GPIO.cleanup()  # ✅ Proper cleanup on exit


if __name__ == "__main__": 
    curses.wrapper(main) # called with curses to get user input