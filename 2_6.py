import turtle as t

t.shape('turtle')

n = int(input())
for i in range(n):
    t.forward(100)
    t.stamp()
    t.left(180)
    t.forward(100)
    t.left(180*(n-2)/n-360)


t.mainloop()
