from turtle import Screen
from Snake import Snake
from Food import Food
from Scoreboard import Scoreboard
import time


def configure_screen():
    screen = Screen()
    screen.tracer(0)
    screen.setup(width=600, height=600)
    screen.title("Snake Game")
    screen.bgcolor("black")

    return screen


def add_events(screen):
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")


def play(game_is_on, screen):
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # Detect collision with food.
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        # Detect collision with wall.
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            game_is_on = False
            scoreboard.game_over()

        # Detect collision with tail.
        for segment in snake.segments:
            if segment == snake.head:
                pass
            elif snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()


screenOjb = configure_screen()
# Declare the required objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()

add_events(screenOjb)
play(True, screenOjb)


screenOjb.exitonclick()
