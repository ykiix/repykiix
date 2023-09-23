import turtle as t
t.shape('turtle')
n = int(input())
for i in range(n):
    t.forward(200)
    t.left(180*(n-1)/n)
t.mainloop()
