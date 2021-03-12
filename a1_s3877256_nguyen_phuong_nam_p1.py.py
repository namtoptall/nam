# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2020C
# Assignment: 1
# Author: Nguyen Phuong Nam (s2877256)
# Created date: dd/mm/yyyy
# Last modified date: dd/mm/yyyy
import turtle
import time
import math
import winsound

win = turtle.Screen()
win.bgcolor("black")
win.title("Timer")

pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
pen.setx(-75)

box = turtle.Turtle()
box.hideturtle()
box.color("white")
box.pensize(5)
box.penup()
box.setx(-50)
box.sety(-50)
box.pendown()
box.forward(250)
box.left(90)
box.forward(150)
box.left(90)
box.forward(300)
box.left(90)
box.forward(150)
box.left(90)
box.forward(150)

num = math.floor(win.numinput("Timer", "Enter the seconds", minval=0, maxval=59))
minute = math.floor(win.numinput("Timer", "Enter the minutes number: ", minval=0, maxval=59))
hours = math.floor(win.numinput("Timer", "Enter the hours number: ", minval=0, maxval=59))
stop = False

while True:
    pen.sety(0)
    pen.write(str(hours)+":"+str(minute)+":"+str(num), font=("Arial", 50))
    pen.sety(100)
    pen.write("Time Left:", font=("Arial", 15))
    num -= 1
    time.sleep(1)
    pen.clear()
    if num <= 0 and minute <= 0 and hours <= 0:
        pen.clear()
        box.clear()
        pen.setx(-100)
        pen.write("Time Over", font=("Arial", 50))
        winsound.PlaySound("E:\\Nirma\\ChillingMusic.wav", winsound.SND_ASYNC)
        time.sleep(5)
        pen.clear()
        break
    if num == 0 and minute >= 1 and stop is not True:
        num = 60
        minute -= 1
    if num == 0 and minute == 0 and hours >= 1 and stop is not True:
        minute = 60
        hours -= 1
    print(num)
    win.update()

print("Time Has Ended!!")