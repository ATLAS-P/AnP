# this file can be used to visualize your serach algorithms
# see Testing.py for an example on how to use it

# to use this file you first need to install colorama:
# open your console and type: pip install colorama, then you are good to go

import colorama

def create_area(x, y, free):
    area = {}
    for y1 in range(y):
        for x1 in range(x):
            if free(x1,y1):
                num = x1 + y1 * x
                nodes = set()

                if x1 > 0 and free(x1 - 1, y1):
                   nodes.add(num - 1)

                if x1 < x - 1 and free(x1 + 1, y1):
                    nodes.add(num + 1)

                if y1 > 0 and free(x1, y1 - 1):
                    nodes.add(num - x)

                if y1 < y - 1 and free(x1, y1 + 1):
                    nodes.add(num + x)

                area[num] = nodes
    return area

def xyIndex(x, y, width):
    return x + y * width

def draw_area(x, y, nodes, start, target, draw):
    colorama.init()
    print(colorama.Back.BLUE + "   " * (x + 2) + colorama.Back.RESET)

    for row in range(y):
        print(colorama.Back.BLUE + "   " + colorama.Back.RESET,  end="")

        for column in range(x):
            num = x * row + column

            if num not in nodes:
                print(colorama.Back.BLUE + "   " + colorama.Back.RESET,  end="")
            elif num == start:
                print(colorama.Back.RED + "   " + colorama.Back.RESET,  end="")
            elif num == target:
                print(colorama.Back.GREEN + "   " + colorama.Back.RESET,  end="")
            elif draw(column, row) != None:
                print(draw(column, row),  end="")
            else:
                print(colorama.Back.WHITE + "   " + colorama.Back.RESET, end="")

        print(colorama.Back.BLUE + "   " + colorama.Back.RESET)

    print(colorama.Back.BLUE + "   " * (x + 2) + colorama.Back.RESET)


def draw_path_visited(width, visited, path):
    def draw(x, y):
        index = xyIndex(x, y, width)

        if index in path:
            return colorama.Back.YELLOW + "   " + colorama.Back.RESET
        elif index in visited:
            return colorama.Fore.YELLOW + " O " + colorama.Fore.RESET
        else:
            return None

    return draw

def no_draw():
    return lambda x, y: None