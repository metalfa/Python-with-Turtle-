"""
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""

from turtle import *

color('red', 'yellow')

begin_fill()

while True:

    forward(200)

    left(170)

    if abs(pos()) < 1:

        break

end_fill()

done()