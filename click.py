import time
import pyautogui
from pynput import mouse
import os

'''This script will require an input from the user in seconds
and repeat a left button click every n seconds.
After entering the time interval the next left button click 
of the mouse will set the position at which the clicks will be repeated.
To exit the script press the right button of the mouse'''

click_position = None
continue_clicking = False
click_interval = None

def keep_clicking(click_position, continue_clicking, click_interval):
    if continue_clicking == False:
        exit()
    while continue_clicking:
        time.sleep(click_interval)
        pyautogui.click(click_position)

def on_click(x, y, button, pressed):
    global click_position, continue_clicking, click_interval
    if button == mouse.Button.left and pressed:
        continue_clicking = True
        if click_position == None: 
            click_position = (x, y)
            print(f"\nReceived click position at {click_position[0]}, {click_position[1]}")
            print(f"\nNow clicking every {click_interval} seconds at position {click_position[0]}, {click_position[1]}")
    elif button == mouse.Button.right and pressed:
        print("\nRight button clicked. Stopping.\n")
        os._exit(0)

def get_time_interval():
    try:
        user_input = float(input('''\nEnter the time interval for the click in seconds and then press Enter.
                                 
Your input: '''))
        if user_input == float(0):
            os._exit(0)
        return user_input
    except ValueError:
        print('\nEnter a valid number or enter 0 to stop the program')
        get_time_interval()   

def get_position():
    try:
        user_input = input('''\n1. Enter the position (x, y) for the click and press Enter.
2. Leave blank and press Enter to get the position with the first click,
3. Enter 0 to exit the program.

Your input: ''')
        if user_input == '0':
            os._exit(0)
        if user_input == '':
            return None
        user_input = user_input.split(',')
        pos  = (int(user_input[0]), int(user_input[1]))
        return pos
    except ValueError:
        print('\nEnter a valid format for the coordinates <x, y> or enter 0 to stop the program')
        get_position()

click_interval = get_time_interval()   
click_position = get_position()
if click_position == None:
    print(f'''\nNow the next click with the left button of the mouse 
will be the position at which the click will be repeated every {click_interval} seconds.
Press the right button of the mouse to stop the process.''')
if click_position:
    print(f'''\nNow a click will be repeated every {click_interval} seconds at {click_position[0]}, {click_position[1]}.
Press the right button of the mouse to stop the process.''')

with mouse.Listener(on_click=on_click) as listener:
    while not continue_clicking:
        time.sleep(1)
    while continue_clicking == True and click_position != None:
        keep_clicking(click_position, continue_clicking, click_interval)