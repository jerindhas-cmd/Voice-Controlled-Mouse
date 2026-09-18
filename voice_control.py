import speech_recognition as sr
import pyautogui
import re
import time

# ==============================
# SETTINGS
# ==============================

MOVE_DISTANCE = 150
MOVE_DURATION = 0.2

pyautogui.PAUSE = 0.1

recognizer = sr.Recognizer()
recognizer.energy_threshold = 300
recognizer.dynamic_energy_threshold = True


# ==============================
# MOVE FUNCTIONS
# ==============================

def move_left(distance):
    pyautogui.moveRel(-distance, 0, duration=MOVE_DURATION)


def move_right(distance):
    pyautogui.moveRel(distance, 0, duration=MOVE_DURATION)


def move_up(distance):
    pyautogui.moveRel(0, -distance, duration=MOVE_DURATION)


def move_down(distance):
    pyautogui.moveRel(0, distance, duration=MOVE_DURATION)


# ==============================
# COMMAND PROCESSING
# ==============================

def execute_command(command):

    command = command.lower().strip()

    print("Command:", command)

    # STOP
    if command in ["stop", "exit", "quit", "close voice mouse"]:
        print("Voice Mouse stopped.")
        return False

    # CENTER
    if "move to center" in command or "center mouse" in command:
        screen_width, screen_height = pyautogui.size()

        pyautogui.moveTo(
            screen_width // 2,
            screen_height // 2,
            duration=0.5
        )

        print("Mouse moved to center.")
        return True

    # DOUBLE CLICK
    if "double click" in command:
        pyautogui.doubleClick()
        print("Double click")
        return True

    # RIGHT CLICK
    if "right click" in command:
        pyautogui.rightClick()
        print("Right click")
        return True

    # LEFT CLICK
    if command == "click" or command == "left click":
        pyautogui.click()
        print("Left click")
        return True

    # SCROLL
    if "scroll up" in command:
        pyautogui.scroll(5)
        print("Scroll up")
        return True

    if "scroll down" in command:
        pyautogui.scroll(-5)
        print("Scroll down")
        return True

    # GET NUMBER
    number_match = re.search(r"\d+", command)

    if number_match:
        distance = int(number_match.group())

        # Prevent extremely large movement
        distance = min(distance, 1000)
    else:
        distance = MOVE_DISTANCE

    # MOVE LEFT
    if "move left" in command or "mouse left" in command:
        move_left(distance)
        print("Moved left:", distance)
        return True

    # MOVE RIGHT
    if "move right" in command or "mouse right" in command:
        move_right(distance)
        print("Moved right:", distance)
        return True

    # MOVE UP
    if "move up" in command or "mouse up" in command:
        move_up(distance)
        print("Moved up:", distance)
        return True

    # MOVE DOWN
    if "move down" in command or "mouse down" in command:
        move_down(distance)
        print("Moved down:", distance)
        return True

    print("Unknown command")

    return True


# ==============================
# MAIN PROGRAM
# ==============================

def main():

    print("==============================")
    print("     VOICE CONTROLLED MOUSE")
    print("==============================")

    print()
    print("Commands:")
    print("Move left")
    print("Move right")
    print("Move up")
    print("Move down")
    print("Move left 300")
    print("Move right 500")
    print("Move to center")
    print("Click")
    print("Right click")
    print("Double click")
    print("Scroll up")
    print("Scroll down")
    print("Stop")
    print()

    # Microphone
    try:
        microphone = sr.Microphone()
    except Exception as e:
        print("Microphone error:", e)
        return

    # Calibrate ONLY ONCE
    with microphone as source:

        print("Calibrating microphone...")
        print("Please stay silent for 2 seconds.")

        recognizer.adjust_for_ambient_noise(
            source,
            duration=2
        )

        print("Calibration complete.")
        print("Speak a command.")
        print()

        while True:

            try:

                print("Listening...")

                audio = recognizer.listen(
                    source,
                    timeout=5,
                    phrase_time_limit=4
                )

                print("Processing...")

                command = recognizer.recognize_google(audio)

                print("You said:", command)

                running = execute_command(command)

                if not running:
                    break

                print()

            except sr.WaitTimeoutError:
                print("No speech detected.")

            except sr.UnknownValueError:
                print("Could not understand. Please speak clearly.")

            except sr.RequestError:
                print("Internet connection / speech recognition error.")

            except Exception as e:
                print("Error:", e)

            time.sleep(0.2)


# ==============================
# START
# ==============================

if __name__ == "__main__":
    main()
