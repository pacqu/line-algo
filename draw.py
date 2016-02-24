from display import *

def draw_line( screen, x0, y0, x1, y1, color ):
    if ((y1 - y0) == 0):
        draw_hor(screen, x0, y0, x1, y1,color)
    elif ((x1 - x0) == 0):
        draw_ver(screen, x0, y0, x1, y1,color)
    else:
        slope =  (y1 - y0)/( (x1 - x0) * 1.0)
        #print slope
        if (slope > 0):
            if (slope < 1):
                if (x0 < x1):
                    draw_oct1(screen, x0, y0, x1, y1,color)
                else:
                    draw_oct1(screen, x1, y1, x0, y0,color)
            else:
                if (x0 < x1):
                    draw_oct2(screen, x0, y0, x1, y1,color)
                else:
                    draw_oct2(screen, x1, y1, x0, y0,color)
        else:
            if (slope > -1):
                if (x0 < x1):
                    draw_oct8(screen, x0, y0, x1, y1,color)
                else:
                    draw_oct8(screen, x1, y1, x0, y0,color)
            else:
                if (x0 < x1):
                    draw_oct7(screen, x0, y0, x1, y1,color)
                else:
                    draw_oct7(screen, x1, y1, x0, y0,color)

def draw_oct1(screen, x0, y0, x1, y1,color):
    x = x0
    y = y0
    A = y1 - y0
    B = - (x1 - x0)
    d = (2*A) + B
    while ( x <= x1):
        plot(screen, color, x, y)
        if ( d > 0 ):
            y += 1
            d += (2*B)
        x += 1
        d += (2*A)


def draw_oct2(screen, x0, y0, x1, y1,color):
    x = x0
    y = y0
    A = y1 - y0
    B = - (x1 - x0)
    d = (2*B) + A
    while ( y <= y1):
        plot(screen, color, x, y)
        if ( d < 0 ):
            x += 1
            d += (2*A)
        y += 1
        d += (2*B)

def draw_oct8(screen, x0, y0, x1, y1,color):
    x = x0
    y = y0
    A = y1 - y0
    B = - (x1 - x0)
    d = (2*B) + A
    while ( x <= x1):
        plot(screen, color, x, y)
        if ( d < 0 ):
            y -= 1
            d -= (2*B)
        x += 1
        d += (2*A)

def draw_oct7(screen, x0, y0, x1, y1,color):
    x = x0
    y = y0
    A = y1 - y0
    B = - (x1 - x0)
    d = (2*B) + A
    while ( y >= y1):
        plot(screen, color, x, y)
        if ( d > 0 ):
            x += 1
            d += (2*A)
        y -= 1
        d -= (2*B)

def draw_hor(screen, x0, y0, x1, y1,color):
    x = x0
    y = y0
    while (x <= x1):
        plot(screen, color, x, y)
        x += 1

def draw_ver(screen, x0, y0, x1, y1,color):
    x = x0
    y = y0
    while (y <= y1):
        plot(screen, color, x, y)
        y += 1
