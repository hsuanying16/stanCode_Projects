"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

This program shows a breakout game,
create all the
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40  # Height of a brick (in pixels).
BRICK_HEIGHT = 15  # Height of a brick (in pixels).
BRICK_ROWS = 10  # Number of rows of bricks.
BRICK_COLS = 10  # Number of columns of bricks.
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10  # Radius of the ball (in pixels).
PADDLE_WIDTH = 75  # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels).
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET
                 ,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):

        self.__dx = 0
        self.__dy = 0
        self.brick_count = 0
        self.brick_num = brick_rows * brick_cols
        self.is_game_start = False

        # Create a graphical window, with some extra space
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, (self.window_width - paddle_width) / 2,
                        self.window_height - paddle_offset - paddle_height)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius * 2, ball_radius * 2)
        self.ball.filled = True
        self.window.add(self.ball, (self.window_width - ball_radius * 2) / 2,
                        (self.window_height - ball_radius * 2) / 2)

        # Initialize our mouse listeners
        onmousemoved(self.paddle_position)
        onmouseclicked(self.start)

        # Draw bricks
        color = ['red', 'orange', 'yellow', 'green', 'blue']
        for i in range(BRICK_ROWS):
            for j in range(BRICK_COLS):
                self.brick = GRect(BRICK_WIDTH, BRICK_HEIGHT)
                self.window.add(self.brick, (j * BRICK_WIDTH + j * BRICK_SPACING),
                                (BRICK_OFFSET + (i * BRICK_HEIGHT) + (i - 1) * BRICK_SPACING))
                self.brick.filled = True
                self.brick.fill_color = color[i // 2]
                self.brick.color = color[i // 2]

    def start(self, event):
        # start when click the mouse
        if self.ball.x == (self.window_width - BALL_RADIUS * 2) / 2:
            if not self.is_game_start:
                self.set_ball_velocity()
                self.is_game_start = True
        # elif self.ball.y >= self.window.height:
        #     self.is_game_start = False

    def set_ball_velocity(self):
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self.__dx = -self.__dx

    def paddle_position(self, event):
        # make paddle in move with mouse in window
        self.paddle.x = event.x - self.paddle.width / 2
        self.paddle.y = self.window_height - PADDLE_OFFSET
        if self.paddle.x < 0:
            self.paddle.x = 0
        elif self.paddle.x + self.paddle.width >= self.window_width:
            self.paddle.x = self.window_width - self.paddle.width

    def remove_brick(self):
        # when bouncing on bricks, remove bricks and change position
        if self.ball.y < self.window_height / 2:
            if self.window.get_object_at(self.ball.x, self.ball.y) is not None:
                self.change_dx_dy()
                self.brick_count += 1
                self.window.remove(self.window.get_object_at(self.ball.x, self.ball.y))
            elif self.window.get_object_at(self.ball.x + 2 * BALL_RADIUS, self.ball.y) is not None:
                self.change_dx_dy()
                self.brick_count += 1
                self.window.remove(self.window.get_object_at(self.ball.x + 2 * BALL_RADIUS, self.ball.y))
            elif self.window.get_object_at(self.ball.x, self.ball.y + 2 * BALL_RADIUS) is not None:
                self.change_dx_dy()
                self.brick_count += 1
                self.window.remove(self.window.get_object_at(self.ball.x, self.ball.y + 2 * BALL_RADIUS))
            elif self.window.get_object_at(self.ball.x + 2 * BALL_RADIUS, self.ball.y + 2 * BALL_RADIUS) is not None:
                self.change_dx_dy()
                self.brick_count += 1
                self.window.remove(self.window.get_object_at(self.ball.x + 2 * BALL_RADIUS, self.ball.y + 2 * BALL_RADIUS))
        return self.brick_count

    def bounce_on_paddle(self):
        # when bouncing on paddle, change position
        if self.ball.y > self.window_height / 2:
            if self.window.get_object_at(self.ball.x, self.ball.y + 2 * BALL_RADIUS) is not None:
                if self.window.get_object_at(self.ball.x + 2 * BALL_RADIUS, self.ball.y + 2 * BALL_RADIUS) is not None:
                    self.change_dx_dy()

    def collision(self):
        # when ball bouncing on wall, change position
        if self.ball.x <= 0 or self.ball.x + 2 * BALL_RADIUS >= self.window_width:
            self.__dx = -self.__dx
        if self.ball.y <= 0:
            self.__dy = -self.__dy

    def set_ball(self):
        # add a new ball
        self.window.add(self.ball, (self.window_width - BALL_RADIUS * 2) / 2,
                            (self.window_height - BALL_RADIUS * 2) / 2)
        self.__dx = 0
        self.__dy = 0
        self.is_game_start = False

    @property
    def dx(self):
        return self.__dx

    @property
    def dy(self):
        return self.__dy

    def change_dx_dy(self):
        #  Setter
        # self.__dx = -self.__dx
        self.__dy = -self.__dy

    def ball(self):
        return self.ball
