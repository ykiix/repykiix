import turtle as t
t.shape('turtle')
l = 10
for i in range(10):
    l += 20
    t.shape('turtle')
    t.forward(l)
    t.left(90)
    t.forward(l)
    t.left(90)
    t.forward(l)
    t.left(90)
    t.forward(l)
    t.left(90)
    t.penup()
    t.right(90)
    t.penup()
    t.right(90)
    t.forward(10)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.pendown()
t.mainloop()
