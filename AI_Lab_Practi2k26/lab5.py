from collections import deque

# Grid: 0 = Free path, 1 = Obstacle
grid = [
    [0, 0, 1, 0],
    [1, 0, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 0]
]

start = (0, 0)
goal = (3, 3)

# Queue stores position and path
queue = deque([(start, [start])])
visited = {start}

# Possible movements: Up, Down, Left, Right
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while queue: #while loop until the queue is not empty
    position, path = queue.popleft()

    if position == goal:
        print("Shortest Path: ", path)
        print("Path Length: ", len(path) - 1)
        break

    for dx, dy in directions:
        x = position[0] + dx
        y = position[1] + dy

        if (0 <= x < 4 and 0 <= y < 4 and
            grid[x][y] == 0 and (x, y) not in visited):

            visited.add((x, y))
            queue.append(((x, y), path + [(x, y)]))

else:
    print("No Path Found")
