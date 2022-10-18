import math

dx = 150 - 250
dy = 350 - 250

if dx > 0 and dy > 0:
    target_angle = math.degrees(math.atan(dy/dx)) - 180
elif dx > 0 and dy < 0:
    target_angle = math.degrees(math.atan(dy/dx)) + 180
elif dx < 0 and dy > 0:
    target_angle = math.degrees(math.atan(dy/dx))
elif dx < 0 and dy < 0:
    target_angle = math.degrees(math.atan(dy/dx))

print(target_angle)