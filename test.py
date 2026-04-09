import random
import turtle


SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
STEP = 20
DELAY_MS = 100


class SnakeGame:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.title("Snake Game")
        self.screen.bgcolor("black")
        self.screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        self.screen.tracer(0)

        self.head = self._create_segment("lime")
        self.head.goto(0, 0)
        self.direction = "stop"

        self.segments = []
        self.food = self._create_segment("red", shape="circle")
        self._spawn_food()

        self.score = 0
        self.high_score = 0
        self.game_over = False

        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.shape("square")
        self.pen.color("white")
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(0, SCREEN_HEIGHT // 2 - 40)
        self._draw_score()

        self._bind_keys()

    def _create_segment(self, color, shape="square"):
        seg = turtle.Turtle()
        seg.speed(0)
        seg.shape(shape)
        seg.color(color)
        seg.penup()
        return seg

    def _bind_keys(self):
        self.screen.listen()
        self.screen.onkeypress(lambda: self._set_direction("up"), "Up")
        self.screen.onkeypress(lambda: self._set_direction("down"), "Down")
        self.screen.onkeypress(lambda: self._set_direction("left"), "Left")
        self.screen.onkeypress(lambda: self._set_direction("right"), "Right")
        self.screen.onkeypress(self.restart, "space")

    def _set_direction(self, new_direction):
        if self.game_over:
            return
        opposite = {
            "up": "down",
            "down": "up",
            "left": "right",
            "right": "left",
        }
        if self.direction != opposite.get(new_direction):
            self.direction = new_direction

    def _move_head(self):
        x, y = self.head.xcor(), self.head.ycor()
        if self.direction == "up":
            self.head.sety(y + STEP)
        elif self.direction == "down":
            self.head.sety(y - STEP)
        elif self.direction == "left":
            self.head.setx(x - STEP)
        elif self.direction == "right":
            self.head.setx(x + STEP)

    def _spawn_food(self):
        max_x = SCREEN_WIDTH // 2 - STEP
        max_y = SCREEN_HEIGHT // 2 - STEP
        x = random.randrange(-max_x, max_x + 1, STEP)
        y = random.randrange(-max_y, max_y + 1, STEP)
        self.food.goto(x, y)

    def _draw_score(self):
        self.pen.clear()
        text = f"Score: {self.score}   High Score: {self.high_score}"
        self.pen.write(text, align="center", font=("Arial", 16, "normal"))
        if self.game_over:
            self.pen.goto(0, 0)
            self.pen.write(
                "Game Over! Press SPACE to restart",
                align="center",
                font=("Arial", 18, "bold"),
            )
            self.pen.goto(0, SCREEN_HEIGHT // 2 - 40)

    def _is_collision_with_wall(self):
        half_w = SCREEN_WIDTH // 2
        half_h = SCREEN_HEIGHT // 2
        return (
            self.head.xcor() >= half_w
            or self.head.xcor() <= -half_w
            or self.head.ycor() >= half_h
            or self.head.ycor() <= -half_h
        )

    def _is_collision_with_self(self):
        for segment in self.segments:
            if segment.distance(self.head) < STEP / 2:
                return True
        return False

    def _grow(self):
        new_segment = self._create_segment("green")
        self.segments.append(new_segment)

    def _move_body(self):
        for i in range(len(self.segments) - 1, 0, -1):
            x = self.segments[i - 1].xcor()
            y = self.segments[i - 1].ycor()
            self.segments[i].goto(x, y)
        if self.segments:
            self.segments[0].goto(self.head.xcor(), self.head.ycor())

    def _check_food_collision(self):
        if self.head.distance(self.food) < STEP:
            self._spawn_food()
            self._grow()
            self.score += 10
            self.high_score = max(self.high_score, self.score)
            self._draw_score()

    def _handle_game_over(self):
        self.game_over = True
        self.direction = "stop"
        self._draw_score()

    def restart(self):
        self.head.goto(0, 0)
        self.direction = "stop"
        for segment in self.segments:
            segment.goto(1000, 1000)
            segment.hideturtle()
        self.segments.clear()
        self.score = 0
        self.game_over = False
        self._spawn_food()
        self._draw_score()

    def game_loop(self):
        if not self.game_over:
            self._move_body()
            self._move_head()
            self._check_food_collision()
            if self._is_collision_with_wall() or self._is_collision_with_self():
                self._handle_game_over()

        self.screen.update()
        self.screen.ontimer(self.game_loop, DELAY_MS)

    def run(self):
        self.game_loop()
        self.screen.mainloop()


if __name__ == "__main__":
    SnakeGame().run()