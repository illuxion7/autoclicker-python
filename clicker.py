from pynput.mouse import Button, Controller
import keyboard
import time

mouse = Controller()

def end():
    c = input('would you like to continue')
    if c == "y":
        main()
    elif c == "n"    :
        e = input('press enter to end: ')
        print (e)

def click():
    mouse.press(Button.left)
    mouse.release(Button.left)



def main():
    delay = float(0.0000001)
    print(""" \x1b[1;31m





CRYPTZZZ AUTOCLICKER

Dev - illuxion7#0777 / Cryptzz#0001    | too ez brother.


 Instructions - 
 1. After running, hold the 'X' key to start clicking (do not press, hold)
 2. To stop, just stop holding the 'X' key.
 3. cya



    """)
    while True:
        if keyboard.is_pressed('x'):
            time.sleep(delay)
            click()
        elif keyboard.is_pressed('z'):
            end()
            break


main()
