from random import *
import turtle as t
t.shape('turtle')
for i in range(100):
    x = [t.left(randint(0, 360)), t.right(randint(0, 360))]
    x[randint(0, 1)]
    t.forward(randint(5, 50))
t.mainloop()
