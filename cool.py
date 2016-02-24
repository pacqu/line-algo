from display import *
from draw import *
from random import randint

screen = new_screen()
color = [ 0, 0, 0 ]

for x in range(XRES):
    color[GREEN] =  (x*randint(0,12))% 14
    color[RED] = randint(0,MAX_COLOR)
    color[BLUE] = randint(0,MAX_COLOR)
    draw_line(screen, XRES/2 , YRES/2 - 100, x*(x%2) , YRES/2 + 100 , color)
for n in range(XRES):
    color[RED] = 0
    color[GREEN] = randint(0,MAX_COLOR)
    color[BLUE] = randint(0,MAX_COLOR)
    draw_line(screen, XRES/2 , YRES/2 + 100 , n*(n%2) , YRES/2 - 100 , color)

for y in range(YRES):
    color[RED] = randint(0,MAX_COLOR)
    color[BLUE] = (x**randint(0,7))% 21
    color[GREEN] = randint(0,MAX_COLOR)
    draw_line(screen, XRES/2 - 100 , YRES/2 , XRES/2 + 100, y*(y%2) , color)
    
for y in range(YRES):
    color[RED] = randint(0,MAX_COLOR)
    color[BLUE] = y % MAX_COLOR
    color[GREEN] = randint(0,MAX_COLOR)
    draw_line(screen, XRES/2 + 100 , YRES/2 , XRES/2 - 100 , y*(y%2) , color)

save_ppm(screen,"wow1.ppm")
