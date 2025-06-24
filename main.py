import time

from turtle import Screen
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game!")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

    #detect collision with food
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        score.increase()

    #detect collision with wall
    if snake.head.xcor()>285 or snake.head.xcor() < -285 or snake.head.ycor()>285 or snake.head.ycor()< -285:
        game_on = False
        score.game_over()

    #detect collision with tail
    # if the head collides with any of the snake segments then game over
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            game_on = False
            score.game_over()


screen.exitonclick()