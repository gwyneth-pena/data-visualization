from random_walk import RandomWalk
import matplotlib.pyplot as plt # type: ignore

def generate_walk():
    rw = RandomWalk(500)
    rw.fill_walk()
    plt.style.use("classic")
    fig, ax = plt.subplots(figsize=(6, 10), dpi=128)
    point_nums = range(rw.num_points)
    ax.scatter(0, 0, c='green', edgecolors="none", s=100)
    ax.scatter(rw.x_values, rw.y_values, c=point_nums, cmap=plt.cm.Blues, edgecolors="none", s=15)
    ax.set_aspect('equal')
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()

while True:
    generate_walk()
    keep_going = input("Make another walk? (y/n) ")
    if keep_going.upper() == 'N':
        break