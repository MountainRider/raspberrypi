import os
import time

from gpiozero import MotionSensor

message_list = [
    "halt",
    "intruder alert",
    "intruder alert",
    "dialing nine one one",
    "put your hands up"
]


def main():
    print "Press Ctrl+C to exit..."
    try:
        ms = MotionSensor(18)
        while True:
            # If motion was detected
            if ms.motion_detected:
                # For each message in the list
                for message in message_list:
                    # Use festival to speak the message
                    os.system('echo "%s" | festival --tts' % message)
                    time.sleep(0.5)
                # Wait up to 10 seconds for the motion to stop
                counter = 0
                while ms.motion_detected:
                    time.sleep(1.0)
                    counter += 1
                    if counter > 10:
                        break
                # Wait 5 seconds before going to the start of the loop
                time.sleep(5.0)
    except KeyboardInterrupt:
        print "Keyboard interrupt"


if __name__ == '__main__':
    main()

