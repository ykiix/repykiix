import turtle as t
t.shape('turtle')
l = 10
t.left(90)
for i in range(3, 13):
    t.circle(l, 360, i)
    l += 15
    t.penup()
    t.right(90)
    t.forward(15)
    t.left(90)
    t.pendown()
t.mainloop()
