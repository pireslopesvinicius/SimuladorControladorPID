import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 800
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Controlador PID")

clock = pygame.time.Clock()
FPS = 30

setpoint = 1050
temperature = 0
increment = 10

kp = 2
ki = 3
kd = 1

p = 0
i = 0
d = 0

points = []
x = 0

run = True
while run:
    deltatime = clock.tick(FPS) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        setpoint += increment
    if keys[pygame.K_DOWN]:
        setpoint -= increment

    error = setpoint - temperature
    last_error = error

    p = error * kp
    pid = p + i + d

    i += error * ki * deltatime

    d = (last_error - error) * kd * deltatime

    temperature += pid * (random.random() / 10)

    print(f"SP:{setpoint}; T:{temperature};E:{error};")

    points.append([x, HEIGHT / 2 - temperature / 10])

    win.fill((255, 255, 255))

    for j in range(len(points)):
        if j > 1:
            pygame.draw.line(win, (0, 200, 0), points[j - 1], points[j], 2)

    pygame.display.update()

    x += 1

pygame.quit()
