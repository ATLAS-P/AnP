# this file shows an example on how to use the Graph.py to visualize your serach algorithms. This example uses the BFS implemented during the first AI lecture.

# to run: use terminal in pycharm not run, type in terminal: python Testing.py

import Graph as graph
import BFS as bfs

def free(x, y):
    return x != 10 or y < 2

WIDTH = 20
HEIGHT = 20

nodes = graph.create_area(WIDTH, HEIGHT, free)

start = graph.xyIndex(0, 0, WIDTH)
target = graph.xyIndex(15, 15, WIDTH)

visited = bfs.BFS(start, target, nodes)
path = bfs.construct_path(visited, target)

graph.draw_area(WIDTH, HEIGHT, nodes, start, target, graph.draw_path_visited(WIDTH, visited, path))