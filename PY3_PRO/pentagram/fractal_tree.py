"""
    分形数
"""
import turtle


def draw_fractal_tree(length):
    if length >= 30:
        turtle.forward(length)
        turtle.right(20)
        draw_fractal_tree(length - 10)
        turtle.left(40)
        draw_fractal_tree(length - 10)
        turtle.right(20)
        turtle.color('brown')
        turtle.backward(length)

    elif length >0 and length < 30:
        turtle.forward(length)
        turtle.right(20)
        draw_fractal_tree(length - 10)
        turtle.left(40)
        draw_fractal_tree(length - 10)
        turtle.right(20)
        turtle.color('orange')
        turtle.backward(length)


def main():
    turtle.color('brown')
    turtle.left(90)
    turtle.penup()
    turtle.backward(100)
    turtle.pendown()
    draw_fractal_tree(50)

    #   点击退出画板
    turtle.exitonclick()


if __name__ == '__main__':
    main()
