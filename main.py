# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2020C
# Assignment: 1
# Author: Nguyen Phuong Nam
# Created date: 08/12/2020
# Last modified date: 13/12/2020

import turtle
import datetime

x = turtle.Screen()
x.title("assignment problem 2")
x.tracer(0, 0)
pen = turtle.Turtle()
pen.shape("arrow")
pen.speed(0)

# 3 hands set up
hour = turtle.Turtle()
hour.pensize(3)
hour.color("blue")

minute = turtle.Turtle()
minute.pensize(2)
minute.color("green")

second = turtle.Turtle()
second.pensize(1)
second.hideturtle()
second.color("red")

# draw a radius
pen.penup()
pen.goto(0, 200)
pen.penup()
pen.goto(0, -180)
pen.pendown()
pen.color("black")
pen.circle(180)

######
for i in range(0, 12):
    pen.penup()
    pen.goto(0, 0)
    pen.setheading(90)
    pen.right(i * 360 / 12)
    pen.forward(155)
    pen.pendown()
    pen.forward(25)

while True:
    hour.clear()
    minute.clear()
    second.clear()

    currentHour = datetime.datetime.now().hour
    currentMinute = datetime.datetime.now().minute
    currentSecond = datetime.datetime.now().second

    # hour
    hour.penup()
    hour.goto(0, 0)
    hour.setheading(90)
    hour.right(0.5 * (60 * currentHour + currentMinute))
    hour.pendown()
    hour.forward(90)

    # minute
    minute.penup()
    minute.goto(0, 0)
    minute.setheading(90)
    minute.right(currentMinute * 360 / 60)
    minute.pendown()
    minute.forward(130)

    # secondhand
    second.penup()
    second.goto(0, 0)
    second.setheading(90)
    second.right(currentSecond * 360 / 60)
    second.pendown()
    second.forward(150)
    x.update()

    # 1-------->>>>12
    pen.speed(0)
    pen.color("pink")

    pen.penup()
    pen.hideturtle()
    pen.goto(0, 130)
    pen.write("12", align="center", font=("Arial", 15, "normal"))

    pen.penup()
    pen.hideturtle()
    pen.goto(145, -15)
    pen.write("3", align="center", font=("Arial", 15, "normal"))

    pen.penup()
    pen.hideturtle()
    pen.goto(0, -160)
    pen.write("6", align="center", font=("Arial", 15, "normal"))

    pen.penup()
    pen.hideturtle()
    pen.goto(-145, -15)
    pen.write("9", align="center", font=("Arial", 15, "normal"))

    pen.penup()
    pen.hideturtle()
    pen.goto(70, 115)
    pen.write("1", align="center", font=("Arial", 15, "normal"))

    pen.penup()
    pen.hideturtle()
    pen.goto(-73, 110)
    pen.write("11", align="center", font=("Arial", 15, "normal"))

    pen.penup()
    pen.hideturtle()
    pen.goto(130, 65)
    pen.write("2", align="center", font=("Arial", 15, "normal"))

    pen.penup()
    pen.hideturtle()
    pen.goto(-120, 60)
    pen.write("10", align="center", font=("Arial", 15, "normal"))

    pen.penup()
    pen.hideturtle()
    pen.goto(132, -90)
    pen.write("4", align="center", font=("Arial", 15, "normal"))

    pen.penup()
    pen.hideturtle()
    pen.goto(-127, -90)
    pen.write("8", align="center", font=("Arial", 15, "normal"))

    pen.penup()
    pen.hideturtle()
    pen.goto(80, -140)
    pen.write("5", align="center", font=("Arial", 15, "normal"))

    pen.penup()
    pen.hideturtle()
    pen.goto(-70, -140)
    pen.write("7", align="center", font=("Arial", 15, "normal"))

    # times variables:
    curr_date = datetime.datetime.now()
    count_date = datetime.datetime(2021, 1, 1, 0, 0, 0)
    time_left = count_date - curr_date

    # write the time and countdown
    turtle.goto(0, -250)
    turtle.clear()
    turtle.write(curr_date, align="center", font=("Arial", 15, "normal"))

    turtle.penup()
    turtle.goto(-200, -250)
    turtle.hideturtle()
    turtle.write("current time is", align="center", font=("Arial", 15, "normal"))
    turtle.speed(0)

    turtle.goto(0, -300)
    turtle.write(time_left, align="center", font=("Arial", 15, "normal"))

    turtle.penup()
    turtle.goto(-155, -300)
    turtle.hideturtle()
    turtle.write("there are", align="center", font=("Arial", 15, "normal"))

    turtle.penup()
    turtle.goto(190, -300)
    turtle.hideturtle()
    turtle.write("left to new year", align="center", font=("Arial", 15, "normal"))
    x.update()
