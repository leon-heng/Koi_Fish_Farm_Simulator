import math
import tkinter as tk
from PIL import ImageTk, Image

class tkKoi:

    def __init__(self, master : tk.Tk, canvas : tk.Canvas, x : int, y : int, image : str):
        self.master = master
        self.canvas = canvas
        self.temp_image = Image.open(image)
        self.temp_image = self.temp_image.resize((90, 90))

        self.koi_image = ImageTk.PhotoImage(self.temp_image, master = self.master)
        self.image = self.canvas.create_image(x, y, image=self.koi_image)
        self.velocity = -1.0
        self.angle = 0.0
        self.target_pos = 0, 0
        self.age = 0


    def move(self, destination : tuple):
        self.target_pos = destination
        x1, y1 = self.canvas.coords(self.image)
        x2, y2 = self.target_pos
        dx = x2 - x1
        dy = y2 - y1
        
        target_angle = self.calculate_target_angle(dx, dy)
        temp_angle = self.angle
        if temp_angle == 0:
            temp_angle += 360

        if abs(target_angle - (temp_angle - 360))> 0.5:
            if (target_angle - temp_angle) > 0:
                self.angle += 1
            else:
                self.angle -= 1
            self.angle %= 360

        x1 += self.velocity*math.sin(math.radians(90 + self.angle))
        y1 += self.velocity*math.cos(math.radians(90 + self.angle))

        self.koi_image = ImageTk.PhotoImage(self.temp_image.rotate(self.angle), master = self.master)
        self.image = self.canvas.create_image(x1, y1, image=self.koi_image)


    def calculate_target_angle(self, dx, dy):
        if dx > 0 and dy > 0:
            return -(math.degrees(math.atan(dy/dx)) - 180)
        elif dx > 0 and dy < 0:
            return -(math.degrees(math.atan(dy/dx)) + 180)
        elif dx < 0 and dy > 0:
            return -math.degrees(math.atan(dy/dx))
        elif dx < 0 and dy < 0:
            return -math.degrees(math.atan(dy/dx))
        else:
            return 0
        
