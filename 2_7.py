import turtle as t
t.shape('turtle')
l = 1
for i in range(10):
    for i in range(10):
        t.forward(l)
        t.left(20)
    l += 1
t.mainloop()
