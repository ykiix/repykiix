import turtle as t
t.shape('turtle')
n = input()
xt = 0
yt = 0
for i in range(6):
    x = int(n[i])
    if x == 0:
        t.left(90)
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.right(90)
        t.forward(50)
        t.right(90)
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.right(90)
    if x == 1:
        t.left(45)
        t.forward(35)
        t.right(135)
        t.forward(50)
        t.left(90)
    if x == 2:
        t.penup()
        t.goto(xt, 25)
        t.pendown()
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.right(45)
        t.forward(35)
        t.left(135)
        t.forward(25)
    if x == 3:
        t.penup()
        t.goto(xt, 25)
        t.pendown()
        t.forward(25)
        t.right(135)
        t.forward(35)
        t.left(135)
        t.forward(25)
        t.right(135)
        t.forward(35)
        t.left(135)
    if x == 4:
        t.goto(xt, 25)
        t.right(90)
        t.forward(25)
        t.left(90)
        t.forward(25)
        t.left(90)
        t.forward(25)
        t.right(180)
        t.forward(50)
        t.left(90)
    if x == 5:
        t.penup()
        t.goto(xt, -25)
        t.pendown()
        t.forward(25)
        t.left(90)
        t.forward(25)
        t.left(90)
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.right(90)
        t.forward(25)
    if x == 6:
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.right(45)
        t.forward(35)
        t.right(45)
    if x == 7:
        t.penup()
        t.goto(xt, 25)
        t.pendown()
        t.forward(25)
        t.right(135)
        t.forward(35)
        t.left(45)
        t.forward(25)
        t.left(90)
    if x == 8:
        t.forward(25)
        t.left(90)
        t.forward(25)
        t.left(90)
        t.forward(25)
        t.left(90)
        t.forward(50)
        t.left(90)
        t.forward(25)
        t.left(90)
        t.forward(25)
        t.right(90)
    if x == 9:
        t.penup()
        t.goto(xt, -25)
        t.pendown()
        t.left(45)
        t.forward(35)
        t.left(135)
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.left(90)
    t.penup()
    xt += 50
    t.goto(xt, yt)
    t.pendown()
t.mainloop()
