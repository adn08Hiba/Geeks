import turtle

def draw_circles(circles):
    t = turtle.Turtle()
    t.speed(1)
    t.penup()
    start_x = -200

    for circle in circles:
        t.goto(start_x, 0)
        t.pendown()
        t.circle(int(circle.radius * 10))
        t.penup()
        start_x += int(circle.radius * 20) + 20

    turtle.done()
