import pyautogui as pg
import time
import threading
import tkinter as tk

# Function that moves the mouse to the 4 corners of the screen
def move_mouse():
    corners = [(100, 100), (1820, 100), (100, 980), (1820, 980)]
    for x, y in corners:
        pg.moveTo(x, y, duration=1)
        pg.click(x, y)

# Function to start the mouse movement in a separate thread
def start_movement():
    global running
    running = True
    while running:
        move_mouse()
        time.sleep(time_per_revolution)

# Function to stop the mouse movement thread
def stop_movement():
    global running
    running = False

# With 160 revolutions over 180 seconds (due to movement of the mouse being 1 sec each)
# total time mouse will be moving is 8 hours.
total_revolutions = 160
time_per_revolution = 180  # seconds

running = False

# Create the tkinter GUI
root = tk.Tk()
root.title("Mouse Automation")

# Set minimum window size
root.minsize(300, 150)

# Label to indicate automation status
status_label = tk.Label(root, text="Mouse Automation: Stopped")
status_label.pack(pady=10)

# Start button
start_button = tk.Button(root, text="Start", command=lambda: threading.Thread(target=start_movement).start())
start_button.pack(pady=10)

# Stop button
stop_button = tk.Button(root, text="Stop", command=stop_movement)
stop_button.pack(pady=10)

def failsafe_check():
    x, y = pg.position()
    if running:
        if (x, y) in pg.FAILSAFE_POINTS:
            confirmation = pg.confirm('Would you like to stop mouse automation?')
            if confirmation == 'OK':
                stop_movement()
                update_status_label()
            else:
                start_movement()
                update_status_label()
            
def update_status_label():
    while True:
        if running:
            status_label.config(text="Mouse Automation: Running")
        else:
            status_label.config(text="Mouse Automation: Stopped")
            
        failsafe_check()
        time.sleep(0.2)

# Start status label update thread
status_thread = threading.Thread(target=update_status_label)
status_thread.daemon = True
status_thread.start()
# Run the tkinter main loop
root.mainloop()
