"""
File: bouncing_ball.py
Name: Sharon
-------------------------
This file simulates a ball bouncing with gravity
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked
#
# VX = 3
# DELAY = 10
# GRAVITY = 1
# SIZE = 20
# REDUCE = 0.9
# START_X = 30
# START_Y = 40
#
# # global variable
# window = GWindow(800, 500, title='bouncing_ball.py')
# count = 0
# ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
# ball.filled = True
#

# def main():
#     """
#     This program simulates a bouncing ball at (START_X, START_Y)
#     that has VX as x velocity and 0 as y velocity. Each bounce reduces
#     y velocity to REDUCE of itself.
#     """
#     window.add(ball)
#     onmouseclicked(start)
#
#
# def start(event):
#     global count, ball
#     window.add(ball)
#     onmouseclicked(skip)                                    # ignore the click when ball is not at start point
#     count += 1                                              # update the times that the ball bounced
#     n = 0                                                   # vertical speed
#     while ball.x < window.width and count <= 3:             # bounce 3 times
#         n += GRAVITY                                        # update gravity
#         ball.move(VX, n)
#         if ball.y + ball.height >= window.height:
#             n = -n * REDUCE                                 # change the direction of vertical speed
#             ball.move(0, -(ball.y + ball.height - window.height))       # move the ball to window.height
#         pause(DELAY)
#     ball.x = START_X                                          # back to the start point
#     ball.y = START_Y
#
#
# def skip(event):
#     # ignore the click when ball is not at start point
#     if ball.x != START_X and ball.y != START_Y:
#         pass
#     else:
#         start(event)

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
n = 0
V = 0
time = 0
end = 0

window = GWindow(800, 500, title='bouncing_ball.py')


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """

    onmouseclicked(bounce)
    pass


def bounce(m):
    global n, V, time, end
    if (time <= 3) and (end == 0):
        end = 1
        X = START_X
        Y = START_Y
        ball = GOval(SIZE, SIZE)
        ball.filled = True
        window.add(ball, X, Y)
        while X < 800:
            while Y < 500:
                n += 1
                pause(DELAY)
                window.clear()
                window.add(ball, X, Y)
                pause(DELAY)
                X = X + VX
                V = GRAVITY * n
                Y = Y + V
            V = V * 0.9
            n = 0
            while V > 0:
                n += 0.1
                X = X + VX
                V = V - GRAVITY * n
                Y = Y - V
                pause(DELAY)
                window.clear()
                window.add(ball, X, Y)
                pause(DELAY)
        window.add(ball, START_X, START_Y)
        time += 1
        end = 0



if __name__ == "__main__":
    main()
