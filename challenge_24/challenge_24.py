# Challenge 24

import io
import zipfile
import numpy as np
from collections import deque
from PIL import Image


def find_path(start, end):
    def valid(n0, n1):
        return (
            0 <= n0 < maze.shape[0]
            and 0 <= n1 < maze.shape[1]
            and (n0, n1) not in visited
            and not np.array_equal(maze[(n0, n1)], np.array([255, 255, 255]))
        )

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = set(start)
    queue = deque([(start, [maze[start]], [start])])

    while queue:
        node, pixels, path = queue.pop()
        for dx, dy in directions:
            next_node = (node[0] + dx, node[1] + dy)
            if valid(*next_node):
                visited.add(next_node)
                if next_node == end:
                    return pixels + [maze[next_node]], path + [next_node]
                queue.append(
                    (next_node, pixels + [maze[next_node]], path + [next_node])
                )


maze = np.array(Image.open("maze.png").convert("RGB"))

start = (0, np.where(maze[0] != 255)[0][-1])
end = (maze.shape[0] - 1, 1)

pixels, positions = find_path(start, end)

zip_file = io.BytesIO(bytes([p[0] for p in pixels[1::2]]))
with zipfile.ZipFile(zip_file, "r") as zip_file:
    print(zip_file.namelist())
    image_data = zip_file.read(zip_file.namelist()[0])
    result = Image.open(io.BytesIO(image_data))

result.save("challenge_24_output.png")

for p in positions + [end]:
    redval = maze[p][0]
    maze[p] = (redval, 255, 0)
image = Image.fromarray(maze)
image.save("mazeresult.png")

######################################
# OUTPUT:                            #
#                                    #
# ['maze.jpg', 'mybroken.zip']       #
#                                    #
# IMAGE: see challenge_24_output.png #
#                                    #
# Maze Result Image (just for fun):  #
#        see mazeresult.png          #
######################################
