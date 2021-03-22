#maepy
import maestro  # using maestro module to control servos
import keyboard # using module keyboard to receive input from keyboard
import time #


from pynput import keyboard as kb

servo = maestro.Controller()
servo.setAccel(0,4)      #set servo 0 acceleration to 4

# def on_press(key):
#     try:
#         print('alphanumeric key {0} pressed'.format(
#             key.char))
#     except AttributeError:
#         print('special key {0} pressed'.format(
#             key))

# def on_release(key):
#     print('{0} released'.format(
#         key))
#     if key == kb.Key.esc:
#         # Stop listener
#         return False

# # Collect events until released
# with kb.Listener(
#         on_press=on_press,
#         on_release=on_release) as listener:
#     listener.join()

def on_press(key):
    # try:
    #     print('alphanumeric key {0} pressed'.format(
    #         key.char))
    #     servo.setTarget(0,-1)  #set servo to move to center position
    #     time.sleep(1)
    #     servo.setTarget(0,6000)  #set servo to move to center position
    #     time.sleep(1)


    # except AttributeError:
    #     print('special key {0} pressed'.format(
    #         key))
    
    if key == kb.Key.a:
        servo.setTarget(0,-1)  #set servo to move to center position
        time.sleep(1)
        servo.setTarget(0,6000)  #set servo to move to center position
        time.sleep(1)


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
