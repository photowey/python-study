# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file flower.py
# @description flower
# @author WcJun
# @date 2021/08/05
# ---------------------------------------------


import turtle as turtle
import random
import time


# 画樱花的躯干(60,t)
def tree(branch, t: turtle.Turtle):
    time.sleep(0.0005)
    if branch > 3:
        if 8 <= branch <= 12:
            if random.randint(0, 2) == 0:
                t.color('snow')
            else:
                t.color('lightcoral')
            t.pensize(branch / 3)
        elif branch < 8:
            if random.randint(0, 1) == 0:
                t.color('snow')
            else:
                t.color('lightcoral')
            t.pensize(branch / 2)
        else:
            t.color('red')
            t.pensize(branch / 10)
        t.forward(branch)
        a = 1.5 * random.random()
        t.right(20 * a)
        b = 1.5 * random.random()
        tree(branch - 10 * b, t)
        t.left(40 * a)
        tree(branch - 10 * b, t)
        t.right(20 * a)
        t.up()
        t.backward(branch)
        t.down()


def petal(m, t: turtle.Turtle):
    for i in range(m):
        a = 200 - 400 * random.random()
        b = 10 - 20 * random.random()
        t.up()
        t.forward(b)
        t.left(90)
        t.forward(a)
        t.down()
        t.color('pink')
        t.circle(1)
        t.up()
        t.backward(a)
        t.right(90)
        t.backward(b)


if __name__ == '__main__':
    t = turtle.Turtle()
    w = turtle.Screen()
    t.hideturtle()
    t.getscreen().tracer(5, 0)
    w.screensize(bg='skyblue')
    t.left(90)
    t.up()
    t.backward(150)
    t.down()
    t.color('sienna')
    tree(60, t)
    petal(100, t)
    w.exitonclick()
