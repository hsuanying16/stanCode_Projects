"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

This program shows a breakout game,
move the paddle to bounce the ball and remove bricks
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3  # Number of attempts


def main():
    '''
    start the game by clicking the mouse
    move the paddle to bounce the ball
    when the ball bounce on brick, remove the brick
    restart the game when the ball fall out the window
    when remove every bricks, win the game
    '''
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    # Add animation loop here!
    while True:
        pause(FRAME_RATE)
        if graphics.ball.y >= graphics.window.height:
            lives -= 1
            if lives > 0:
                graphics.set_ball()
            elif graphics.brick_num == graphics.brick_count:    # when remove all the bricks
                break
            else:
                break
        graphics.collision()                            # when ball bouncing on wall, change position
        graphics.remove_brick()                         # when bouncing on bricks, remove bricks and change position
        graphics.bounce_on_paddle()                     # when bouncing on paddle, change position
        graphics.ball.move(graphics.dx, graphics.dy)


if __name__ == '__main__':
    main()
