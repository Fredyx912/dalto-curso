from turtle import*
import random

title("jugando")
bgcolor("black")
#pencolor("red")

"""""
forward(100)
right(90)
forward(100)
left(90)
forward(100)
backward(50)
right(90)
forward(100)
mainloop()
"""""

#circulo
"""
circle(90)
circle(100)
"""

#cuadrado
"""
pensize(7)
forward(100)
right(90)
penup()
pensize(3)
pencolor("green")
forward(100)
right(90)
pendown()
forward(100)
penup()
right(90)
pencolor("blue")
forward(100)
"""

"""fillcolor("green")
begin_fill()
for i in range (4):
    forward(100)
    right(90)
end_fill()""" 

  
speed(5)
x = 1
while x < 300:
    r = random.randint(0,250)
    g = random.randint(0,250)
    b = random.randint(0,250)
    colormode(255)
    pencolor(r,g,b)
    forward(5+x)
    x+=1
    
mainloop() 
