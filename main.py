from turtle import Turtle, Screen
from player import Player
from scoreboard import ScoreBoard
from car_manager import CarManager
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = ScoreBoard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move_up, "Up")
#screen.onkey(player.move_down, "Down")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    #Detect collision with cars:
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    #Detect successful crossing:
    if player.is_at_finish_line():
        player.go_to_start()
        scoreboard.increase_point()
        car_manager.level_up()




screen.exitonclick()


