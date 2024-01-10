import time
from tkinter import Canvas, Tk, PhotoImage, CENTER
from random import randint
from math import sin, pi

monitor_delay = 17
size = 900  # size of canvas
root = Tk()
canvas = Canvas(root, width=size, height=size)
canvas.pack()
qnt_balls = 9  # number of balls along each axis
balls_array = [1] * 100  # array (list) of ball properties [Xcoord, Yold_coord, Ynew_coord]
current_ball_pointers = [1] * 100  # Contains references to objects of canvas.create_image for each ball
img_ball = [PhotoImage(file='green.png'), PhotoImage(file='red.png'), PhotoImage(file='silver.png'),
            PhotoImage(file='azure.png'), PhotoImage(file='blue.png'), PhotoImage(file='cyan.png'),
            PhotoImage(file='emerald.png'), PhotoImage(file='gold.png'), PhotoImage(file='pink.png'),
            PhotoImage(file='purple.png'), PhotoImage(file='scarlet.png'), PhotoImage(file='steel.png'),
            PhotoImage(file='bronze.png'), PhotoImage(file='yellow.png')]


def move_balls(grad):  # Move every ball
    for x in range(qnt_balls):  # Rows of balls
        for k in range(qnt_balls):  # Columns of balls
            balls_index = x * qnt_balls + k  # Using one-dimensional array as two-dimensional
            balls_array[balls_index][2] = grad + k * 15  # Each column of balls is at a diff. height (different angle)
            balls_array[balls_index][2] = balls_array[balls_index][2] + x * 15  # Delay rows of ball
            balls_array[balls_index][2] = balls_array[balls_index][2] * pi / 180  # Grad to radian
            balls_array[balls_index][2] = sin(balls_array[balls_index][2])  # Sinus
            balls_array[balls_index][2] = (650 - x * 60) + int(
                balls_array[balls_index][2] * 55)  # New Y-coord each ball
            canvas.move(current_ball_pointers[balls_index], 0,
                        (balls_array[balls_index][2] - balls_array[balls_index][1]))  # Move current ball
            balls_array[balls_index][1] = balls_array[balls_index][2]  # Old Y-coord <== New Y-coord


def draw_balls():  # Fill start balls array and draw them
    for m in range(qnt_balls):
        for i in range(qnt_balls):
            balls_index = m * qnt_balls + i  # Using one-dimensional array as two-dimensional
            color_index = randint(0, 13)  # index for list of ball color
            balls_array[balls_index] = [70 * (i + 1) + m * 20, 650 - m * 60, 650 - m * 60]  # [x, old_y, new_y]
            current_ball_pointers[balls_index] = canvas.create_image(balls_array[balls_index][0],
                                                                     balls_array[balls_index][1],
                                                                     image=img_ball[color_index], anchor=CENTER)
                                                                        # Draw ball at start position


start = time.time()
draw_balls()
# Main cycle
for j3 in range(5):
    for j in range(360):
        move_balls(j)
        root.update()

end = time.time()
print(end - start)
