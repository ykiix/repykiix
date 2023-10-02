import turtle as t
t.shape('turtle')
n = input()
xt = 0
yt = 0
for i in range(6):
    x = int(n[i])
    with open("C:\\Users\\diese\\repykiix\\numbers.txt", "r") as file:
        exec(file.read())
    t.penup()
    xt += 50
    t.goto(xt, yt)
    t.pendown()
t.mainloop()
