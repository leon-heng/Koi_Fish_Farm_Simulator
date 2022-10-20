import math
import tkinter as tk
from PIL import ImageTk, Image

class tkKoi:

    def __init__(self, master : tk.Tk, canvas : tk.Canvas, x : int, y : int, image : str):
        self.master = master
        self.canvas = canvas
        self.temp_image = Image.open(image)
        self.temp_image = self.temp_image.resize((150, 150))

        self.koi_image = ImageTk.PhotoImage(self.temp_image, master = self.master)
        self.image = self.canvas.create_image(x, y, image=self.koi_image)
        self.velocity = -1.0
        self.angle = 0.0


    def move(self, destination : tuple):
        x, y = self.canvas.coords(self.image)
        target_x, target_y = destination
        dx = target_x - x
        dy = target_y - y
        
        if dx > 0 and dy > 0:
            target_angle = -(math.degrees(math.atan(dy/dx)) - 180)
        elif dx > 0 and dy < 0:
            target_angle = -(math.degrees(math.atan(dy/dx)) + 180)
        elif dx < 0 and dy > 0:
            target_angle = -math.degrees(math.atan(dy/dx))
        elif dx < 0 and dy < 0:
            target_angle = -math.degrees(math.atan(dy/dx))

        
        temp_angle = self.angle
        if temp_angle == 0:
            temp_angle += 360

        if abs(target_angle - (temp_angle - 360))> 0.5:
            if (target_angle - temp_angle) > 0:
                self.angle += 1
            else:
                self.angle -= 1

            self.angle %= 360

        
        x += self.velocity*math.sin(math.radians(90 + self.angle))
        y += self.velocity*math.cos(math.radians(90 + self.angle))


        self.koi_image = ImageTk.PhotoImage(self.temp_image.rotate(self.angle), master = self.master)
        self.image = self.canvas.create_image(x, y, image=self.koi_image)
        


        

