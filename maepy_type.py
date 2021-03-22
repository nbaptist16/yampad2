#maepy
import maestro  # using maestro module to control servos
import keyboard # using module keyboard to receive input from keyboard
import time # using module time to add pauses between servo actions
import sys # using module sys to exit cleanly on 'esc'

# initialize keyboard input and servo controller
from pynput import keyboard as kb
servo = maestro.Controller()

# set servo accelerations to 4
servo.setAccel(0,9)      # set servo 0 acceleration to 9
servo.setAccel(2,9)
servo.setAccel(4,9)
servo.setAccel(6,9)
servo.setAccel(8,9)

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))

        # range: 992    1500    2000
        if key.char == '0':
            servo.setTarget(4,1)  # trigger '1' key (servo3\5 --> left)
            time.sleep(1)
            servo.setTarget(6,6000)  #set servo to move to center position
            time.sleep(1)

        if key.char == '1':
            servo.setTarget(4,-1)  # trigger '1' key (servo5 --> right)
            time.sleep(1)
            servo.setTarget(6,6000)  #set servo to move to center position
            time.sleep(1)
        
        if key.char == '2':
            servo.setTarget(6,-1)  # trigger '2' key (servo3 --> left)
            time.sleep(1)
            servo.setTarget(6,6000)  #set servo to move to center position
            time.sleep(1)

        if key.char == '3':
            servo.setTarget(6,1)  # trigger '3' key (servo4 --> right)
            time.sleep(1)
            servo.setTarget(0,6000)  #set servo to move to center position
            time.sleep(1)
    
        if key.char == '4':
            servo.setTarget(2,1)  #set servo to move to center position
            time.sleep(1)
            servo.setTarget(0,6000)  #set servo to move to center position
            time.sleep(1)
        
        if key.char == '5':
            servo.setTarget(2,-1)  #set servo to move to center position
            time.sleep(1)
            servo.setTarget(0,6000)  #set servo to move to center position
            time.sleep(1)
        
        if key.char == '6':
            servo.setTarget(8,1)  #set servo to move to center position
            time.sleep(1)
            servo.setTarget(0,6000)  #set servo to move to center position
            time.sleep(1)
        
        if key.char == '7':
            servo.setTarget(0,-1)  #set servo to move to center position
            time.sleep(1)
            servo.setTarget(0,6000)  #set servo to move to center position
            time.sleep(1)
        
        if key.char == '8':
            servo.setTarget(0,1)  #set servo to move to center position
            time.sleep(1)
            servo.setTarget(0,6000)  #set servo to move to center position
            time.sleep(1)
        
        if key.char == '9':
            servo.setTarget(8,-1)  #set servo to move to center position
            time.sleep(1)
            servo.setTarget(0,6000)  #set servo to move to center position
            time.sleep(1)        


    except AttributeError:
        print("Exiting...")
        if key == kb.Key.esc:
            # # Stop listener
            # pass
            # return False
            # break
            sys.exit(1)


# Collect events until released
with kb.Listener(
        on_press=on_press,
        # on_release=on_release) as listener:
        ) as listener:
    listener.join()


servo.close()
