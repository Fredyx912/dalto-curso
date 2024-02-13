import turtle

def draw_star():
    window = turtle.Screen()
    window.bgcolor("white")

    star = turtle.Turtle()
    star.shape("turtle")
    star.color("black")

    for _ in range(5):
        star.forward(100)
        star.right(144)

    window.exitonclick()

draw_star()


