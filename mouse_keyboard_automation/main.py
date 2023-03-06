# mouse automation
import pyautogui as pg
import time


# Function that moves the mouse to the 4 corners of the screen
def move_mouse():
    pg.moveTo(100, 100, duration=1)
    pg.click(100, 100)
    pg.moveTo(1820, 100, duration=1)
    pg.moveTo(100, 980, duration=1)
    pg.click(100, 980)
    pg.moveTo(1820, 980, duration=1)


# With 160 revolutions over 180 seconds (due to movement of the mouse being 1 sec each)
# total time mouse will be moving is 8 hours.
a = 150

while (a != 0):
    move_mouse()
    a = a - 1
    # Moves mouse every 3 minutes
    time.sleep(176)
