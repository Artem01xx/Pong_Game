import turtle
import sys


# Moving Pedals
def pedal_a_up():
    plus_to_position = 30
    y_position = pedal_a.ycor()
    y_position += plus_to_position
    pedal_a.sety(y_position)


def pedal_a_down():
    minus_to_position = 30
    y_position = pedal_a.ycor()
    y_position -= minus_to_position
    pedal_a.sety(y_position)


def pedal_b_up():
    plus_to_position = 30
    y_position = pedal_b.ycor()
    y_position += plus_to_position
    pedal_b.sety(y_position)


def pedal_b_down():
    minus_to_position = 30
    y_position = pedal_b.ycor()
    y_position -= minus_to_position
    pedal_b.sety(y_position)


# Creating Objects
def creating_pedal_a():
    pedal_a.speed(0)
    pedal_a.shape("square")
    pedal_a.shapesize(stretch_wid=5, stretch_len=1)
    pedal_a.color("white")
    pedal_a.penup()
    pedal_a.goto(-350, 0)


def creating_pedal_b():
    pedal_b.speed(0)
    pedal_b.shape("square")
    pedal_b.shapesize(stretch_wid=5, stretch_len=1)
    pedal_b.color("white")
    pedal_b.penup()
    pedal_b.goto(350, 0)


def creating_ball():
    ball.speed(0)
    ball.shape("circle")
    ball.color("white")
    ball.penup()
    ball.goto(0, 0)


def creating_pen():
    pen.speed(0)
    pen.hideturtle()
    pen.goto(0, 260)
    pen.penup()
    pen.color("white")


def quit_game():
    main_screen.bye()
    sys.exit()


# Input System
def input_key():
    main_screen.listen()
    main_screen.onkeypress(pedal_a_up, "w")
    main_screen.onkeypress(pedal_a_down, "s")
    main_screen.onkeypress(pedal_b_up, "Up")
    main_screen.onkeypress(pedal_b_down, "Down")
    main_screen.onkeypress(quit_game, "e")


# Main Game Function And Game Loop
def main():
    creating_pedal_a()
    creating_pedal_b()
    creating_ball()
    creating_pen()
    ball.dy = 0.2
    ball.dx = 0.2
    score_a = 0
    score_b = 0
    while True:
        main_screen.update()
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)
        # Checking Ball Coordination
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -ball.dy
        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy = -ball.dy
        if ball.xcor() > 390:
            ball.goto(0, 0)
            ball.dx = -ball.dx
            score_a += 1
            pen.clear()
            pen.write(f"Player 1: {score_a} - Player 2: {score_b}", align="center",
                      font=("Courier", 20, "normal"))
        if ball.xcor() < -390:
            ball.goto(0, 0)
            ball.dx = -ball.dx
            score_b += 1
            pen.clear()
            pen.write(f"Player 1: {score_a} - Player 2: {score_b}", align="center",
                      font=("Courier", 20, "normal"))
        # Check If Ball Hits Pedals
        if (340 < ball.xcor() < 350) and pedal_b.ycor() + 50 > ball.ycor() > pedal_b.ycor() - 50:
            ball.dx = -ball.dx
        if (-340 > ball.xcor() > -350) and pedal_a.ycor() + 50 > ball.ycor() > pedal_a.ycor() - 50:
            ball.dx = -ball.dx
        # Checking Pedal Coordination
        if pedal_a.ycor() > 249:
            pedal_a.sety(249)
        if pedal_a.ycor() < -249:
            pedal_a.sety(-249)
        if pedal_b.ycor() > 249:
            pedal_b.sety(249)
        if pedal_b.ycor() < -249:
            pedal_b.sety(-249)
        # Win State
        if score_a >= 10 or score_b >= 10:
            main_screen.bye()
            sys.exit()


# Setting Main Screen And Objects
pen = turtle.Turtle()
pedal_a = turtle.Turtle()
pedal_b = turtle.Turtle()
ball = turtle.Turtle()
main_screen = turtle.Screen()
main_screen.title(" Pong by @artem01xx")
main_screen.bgcolor("black")
main_screen.setup(800, 600)
main_screen.tracer(0)

# Calling input
input_key()

if __name__ == "__main__":
    main()
