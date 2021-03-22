#maepy
import maestro  # using maestro module to control servos
import keyboard # using module keyboard to receive input from keyboard
import time #

import sys
# import thread
# import termios

# from pynput.keyboard import Key, Controller
from pynput import keyboard as kb

servo = maestro.Controller()
# keyboard = Controller()

servo.setAccel(0,4)      #set servo 0 acceleration to 4

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
        
        # if key.char == '0':
        #     servo.setTarget(0,-1)  #set servo to move to center position
        #     time.sleep(1)
        #     servo.setTarget(0,6000)  #set servo to move to center position
        #     time.sleep(1)

        if key.char == 'a':
            servo.setTarget(0,-1)  #trigger '1' key (servo4 --> right)
            time.sleep(1)
            servo.setTarget(0,6000)  #set servo to move to center position
            time.sleep(1)
        
        if key.char == 'b':
            servo.setTarget(2,-1)  #set servo to move to center position
            time.sleep(1)
            servo.setTarget(2,6000)  #set servo to move to center position
            time.sleep(1)

        if key.char == '3':
            servo.setTarget(0,-1)  #set servo to move to center position
            time.sleep(1)
            servo.setTarget(0,6000)  #set servo to move to center position
            time.sleep(1)
    
        if key.char == '4':
            servo.setTarget(0,-1)  #set servo to move to center position
            time.sleep(1)
            servo.setTarget(0,6000)  #set servo to move to center position
            time.sleep(1)
        
        if key.char == '5':
            servo.setTarget(0,-1)  #set servo to move to center position
            time.sleep(1)
            servo.setTarget(0,6000)  #set servo to move to center position
            time.sleep(1)
        
        if key.char == '6':
            servo.setTarget(0,-1)  #set servo to move to center position
            time.sleep(1)
            servo.setTarget(0,6000)  #set servo to move to center position
            time.sleep(1)
        
        if key.char == '7':
            servo.setTarget(0,-1)  #set servo to move to center position
            time.sleep(1)
            servo.setTarget(0,6000)  #set servo to move to center position
            time.sleep(1)
        
        if key.char == '8':
            servo.setTarget(0,-1)  #set servo to move to center position
            time.sleep(1)
            servo.setTarget(0,6000)  #set servo to move to center position
            time.sleep(1)
        
        if key.char == '9':
            servo.setTarget(0,-1)  #set servo to move to center position
            time.sleep(1)
            servo.setTarget(0,6000)  #set servo to move to center position
            time.sleep(1)        
 

    # except AttributeError:
    #     print('special key {0} pressed'.format(
    #         key))
    except AttributeError:
        # print('special key {0} pressed'.format(
        #     key))
        print("Exiting...")
        if key == kb.Key.esc:
            # # Stop listener
            # pass
            # return False
            # break
            sys.exit(1)
    
    # if key == kb.Key.a:
    #     servo.setTarget(0,-1)  #set servo to move to center position
    #     time.sleep(1)
    #     servo.setTarget(0,6000)  #set servo to move to center position
    #     time.sleep(1)


# def on_release(key):
#     print('{0} released'.format(
#         key))
#     servo.setTarget(0,6000)  #set servo to move to center position
#     if key == kb.Key.esc:
#         # Stop listener
#         return False

# Collect events until released
with kb.Listener(
        on_press=on_press,
        # on_release=on_release) as listener:
        ) as listener:
    listener.join()
    

# breakNow = False
# def escExit(key):
#     global breakpoint
#     while True:
#         if key == kb.Key.esc:
#             breakNow = True
#             break
# thread.start_new_thread(escExit, ())

# def escExit(key):
#     while key == kb.Key.esc:
#         try:
#             print("Exiting...")
#             return
#         except KeyboardInterrupt:
#             print("umm...")

# #init positions to center
# servo = maestro.Controller()
# servo.setAccel(0,4)      #set servo 0 acceleration to 4
# servo.setTarget(0,6000)  #set servo to move to center position
# servo.setSpeed(2,10)     #set speed of servo 1
# x = servo.getPosition(2) #get the current position of servo 1

# servo.setAccel(2,4)      #set servo 0 acceleration to 4
# servo.setTarget(2,6000)  #set servo to move to center position

# servo.setAccel(4,4)      #set servo 0 acceleration to 4
# servo.setTarget(4,6000)  #set servo to move to center position

# servo.setAccel(6,4)      #set servo 0 acceleration to 4
# servo.setTarget(6,6000)  #set servo to move to center position

# servo.setAccel(8,4)      #set servo 0 acceleration to 4
# servo.setTarget(8,6000)  #set servo to move to center position


#

servo.close()
