"""
    用递归函数画五角星
"""
import turtle


def draw_pentagram(size):
    for i in range(0, 5):
        turtle.forward(size)
        turtle.right(144)
    size = size + 100
    if size <= 500:
        draw_pentagram(size)

    #   点击退出画板
    turtle.exitonclick()


def main():
    turtle.pensize(2)
    turtle.penup()
    turtle.backward(200)
    turtle.pendown()
    turtle.color('red')
    draw_pentagram(200)


if __name__ == '__main__':
    main()
