import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.move_turtle, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.random_car()
    car.move_car()

    for cars in car.all_cars:
        if cars.distance(player) < 30:
            game_is_on = False
            scoreboard.game_over()

    if player.ycor() > 280:
        player.goto(0, -280)
        car.level_up()
        scoreboard.update_scoreboard()

screen.exitonclick()
