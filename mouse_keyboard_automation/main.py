import pyautogui as pg
import time

class MouseMover:
    def __init__(self, screen_width, screen_height, margin=100):
        self.width = screen_width
        self.height = screen_height
        self.margin = margin
        self.corners = self.calculate_corners()

    def calculate_corners(self):
        return [
            (self.margin, self.margin),
            (self.width - self.margin, self.margin),
            (self.margin, self.height - self.margin),
            (self.width - self.margin, self.height - self.margin)
        ]

    def move_mouse(self):
        for x, y in self.corners:
            pg.moveTo(x, y, duration=1)
            pg.click(x, y)

    def run(self, total_revolutions, time_per_revolution):
        for _ in range(total_revolutions):
            self.move_mouse()
            time.sleep(time_per_revolution)

if __name__ == "__main__":
    width, height = pg.size()
    mover = MouseMover(width, height)

    try:
        total_minutes = int(input("Enter the desired duration in minutes: "))
        minutes_per_revolution = int(input("Enter minutes between movements: "))

        total_revolutions = total_minutes // minutes_per_revolution
        time_per_revolution = minutes_per_revolution * 60  # Convert to seconds

        mover.run(total_revolutions, time_per_revolution)

    except ValueError:
        print("Invalid input. Please enter whole numbers for minutes.")