'''
Mike Cao
This assignment draws shapes using recursive functions.
'''

import turtle
import sys

def draw(length: int, sides: int, fill: str) -> int:
    '''
    Determines whether the shapes is to be filled or not, then draws shapes using recursive functions decrementing the sides.
    pre: length: 200, sides<=8 and sides>= 3, fill == 'true' or fill == 'false'
    post: return: total (sum of sides)
    '''

    total = 0
    deg = 360/sides

    if fill == 'true':
        FILL_PEN_WIDTH = 2
        if sides == 8:
            turtle.color('violet')
        if sides == 7:
            turtle.color('blueviolet')
        if sides == 6:
            turtle.color('green')
        if sides == 5:
            turtle.color('red')
        if sides == 4:
            turtle.color('orange')
        if sides == 3:
            turtle.color('blue')

        turtle.begin_fill()
        for num in range(sides):
            turtle.forward(length)
            total += length
            turtle.left(deg)
        turtle.end_fill()
        if sides > 3:
            for i in range(sides):
                turtle.forward(length)
                turtle.left(deg)
                total += draw(length / 2, sides - 1, fill)
    elif fill == 'false':
        UNFILL_PEN_WIDTH = 8
        for num in range(sides):
            turtle.forward(length)
            total += length
            turtle.left(deg)
        if sides > 3:
            for i in range(sides):
                turtle.forward(length)
                turtle.left(deg)
                total += draw(length / 2, sides - 1, fill)
    return total

def init():
    '''
    Sets the window size and writes the name.
    '''
    WINDOW_LENGTH = 800
    SIDE_LENGTH = 200
    turtle.penup()
    turtle.right(90)
    turtle.forward(200)
    turtle.write('Mike Cao', False, align="right")
    turtle.back(50)
    turtle.left(90)
    turtle.pendown()

def main():
    '''
    pre: sides <= 8 and sides >= 3, fill == 'true' or fill == 'false'
    post: total printed
    Gets the sides and fill from script parameters, calls the draw function, and prints the total length of the polygons.
    '''
    sides = int(sys.argv[1])
    assert sides <= 8 and sides >= 3, "$ python3 polygons.py #_sides [fill|unfill]"
    fill = str(sys.argv[2])
    length = 150
    turtle.tracer(0, 0)
    init()
    print('Sum: ' + str(draw(length, sides, fill)))
    turtle.update()
    turtle.mainloop()

if __name__ == '__main__':
    main()