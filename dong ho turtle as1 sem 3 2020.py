# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2020C
# Assignment: 1
# Author: Nguyen Phuong Nam
# Created date: 11/12/2020
# Last modified date: 13/12/2020
import turtle

nam = turtle.Screen()

BAR_H_SCALE = 10
starting_x = -180
starting_y = -100
student_length = 60

# pen setup
p = turtle.Pen()
p.speed(10000000)
turtle.bgcolor("white")
turtle.pensize(1000)
p.color("black")

# starting_x
p.penup()
p.setx(starting_x)
p.sety(starting_y)
p.pendown()
p.forward(150)

# write x
p.right(90)
p.penup()
p.forward(100)
p.pendown()
p.write("Final Result", align="center", font=("time news roman", 20, "normal"))

# back to the first tinme
p.penup()
p.left(180)
p.forward(100)
p.pendown()
p.right(90)
p.forward(150)

# X
p.clone()

# Y
p.setx(starting_x)
p.sety(starting_y)
p.left(90)

# 20 student * 5


def y_axis():
    for number in range(5):
        p.forward(student_length)
        p.dot()
        p.write(20 + number * 20, align="right", font=("Arial", 15, "normal"))


y_axis()

# nn bar
p.penup()
p.goto(-110, -100)
p.pendown()
p.pencolor("black")
p.fillcolor("blue")
p.hideturtle()
p.begin_fill()

p.forward(150)
p.left(90)
p.forward(40)
p.left(90)
p.forward(150)
p.left(90)
p.forward(40)
p.left(90)

# pa bar
p.penup()
p.goto(-70, -100)
p.pendown()

p.forward(110)
p.left(90)
p.forward(40)
p.left(90)
p.forward(110)
p.left(90)
# continue with cr bar
p.penup()
p.goto(-30, -100)
p.pendown()

p.left(90)
p.forward(135)
p.left(90)
p.forward(40)
p.left(90)
p.forward(135)
p.left(90)

# DI
p.penup()
p.goto(10, -100)
p.pendown()

p.left(90)
p.forward(170)
p.left(90)
p.forward(40)
p.left(90)
p.forward(170)
p.left(90)
# HD
p.penup()
p.goto(50, -100)
p.pendown()

p.left(90)
p.forward(125)
p.left(90)
p.forward(40)
p.left(90)
p.forward(125)
p.left(90)

p.end_fill()


# write 5bukets:
p.penup()
p.goto(-130, -130)
p.pendown()
p.write("NN", align="center", font=("times new roman", 15, "bold"))

p.penup()
p.goto(-90, -130)
p.pendown()
p.write("PA", align="center", font=("times new roman", 15, "bold"))

p.penup()
p.goto(-50, -130)
p.pendown()
p.write("CR", align="center", font=("times new roman", 15, "bold"))

p.penup()
p.goto(-10, -130)
p.pendown()
p.write("DI", align="center", font=("times new roman", 15, "bold"))

p.penup()
p.goto(30, -130)
p.pendown()
p.write("HD", align="center", font=("times new roman", 15, "bold"))
nam.exitonclick()
