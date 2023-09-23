import turtle as t
t.shape('turtle')
l = 50
t.left(90)
for i in range(10):
    t.circle(l)
    t.left(180)
    t.circle(l)
    t.left(180)
    l += 10
t.mainloop()
