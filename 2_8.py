import turtle as t
t.shape('turtle')
l = 5
for i in range(10):
    for j in range(2):
        t.forward(l)
        t.left(90)
    l += 5
t.mainloop()
