from matplotlib.pyplot import ion, figure, pause
from math import sin

def equation(a, b):
    x = []
    y = []
    time = -50
    while time < 50:
        time += 0.1
        new_x = sin(a * time)
        new_y = sin(b * time)
        if new_x in x and new_y in y:
            break
        x.append(new_x)
        y.append(new_y)
    return x, y

ion()
fig = figure()
ax = fig.add_subplot()
while True:
    a, b = -1, 1
    while a/b <= 2:
        a += 0.001
        x, y = equation(a, b)
        ax.clear()  # Try without clear
        ax.plot(x, y)
        fig.canvas.flush_events()
        pause(0.01)
