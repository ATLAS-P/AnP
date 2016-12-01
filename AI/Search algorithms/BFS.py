# this file was created during the first lecture
# use the Graph file for visualizing your algorithms

import queue

def neighbours(nodes, state):
    return nodes.get(state, {})


def BFS(start, end, nodes):
    que = queue.Queue()
    visited = dict()

    visited[start] = None
    que.put(start)

    while not que.empty():
        square = que.get()

        if square == end:
            return visited

        for neigh in neighbours(nodes, square):
            if neigh not in visited:
                visited[neigh] = square
                que.put(neigh)

    return None

def construct_path(visited, end):
    path = list()
    path.append(end)

    last = end

    while last != None:
        last = visited.get(last)

        if last != None:
            path.append(last)

    path.reverse()

    return path

def find_path_BFS(start, end, nodes):
    visited = BFS(start, end, nodes)
    return construct_path(visited, end)