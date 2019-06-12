# coding: utf-8
import turtle as t
import lsys as l
t.pencolor('blue')
t.penup()
#t.setpos(-400,-300)
t.setheading(0)
t.pendown()
t.delay(0)
t.pensize(1)
#t.tracer(False)

angle = 120
head = 0
position = (0,0)
stack = []

def ffun():
    t.fd(10)

def minusfun():
    global angle
    t.left(angle)

def plusfun():
    global angle
    t.right(angle)

def xfun():
    return

def push():
    global stack
    global position 
    global head 
    position = (t.xcor(),t.ycor())
    head = t.heading()
    stack.append((head,position))

def pop():
    global head
    global position
    global stack
    head,position = stack.pop()
    t.penup()
    t.setpos(position)
    t.setheading(head)
    t.pendown()

angle = 120
r = [('F', 'F-G+F+G-F'), ('G', 'GG')]
dicti = {
        'F':ffun,
        'G':ffun,
        '+':plusfun,
        '-':minusfun,
        'X':xfun,
        'Y':xfun,
        '[':push,
        ']':pop
        }

start = 'F-G-G'
start = l.findnth(start,r,4)
print(start)
l.execute(start,dicti)
t.exitonclick()
