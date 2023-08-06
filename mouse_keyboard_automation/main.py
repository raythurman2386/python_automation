import pyautogui as pg
import time

# Function that moves the mouse to the 4 corners of the screen
def move_mouse():
    corners = [(100, 100), (1820, 100), (100, 980), (1820, 980)]
    for x, y in corners:
        pg.moveTo(x, y, duration=1)
        pg.click(x, y)

# With 160 revolutions over 180 seconds (due to movement of the mouse being 1 sec each)
# total time mouse will be moving is 8 hours.
total_revolutions = 160
time_per_revolution = 176  # seconds

while total_revolutions > 0:
    move_mouse()
    total_revolutions -= 1

    # Moves mouse every 3 minutes
    time.sleep(time_per_revolution)

