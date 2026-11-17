start = [
    1,2,3,
    4,0,6,
    7,5,8
]
print("Initial state is ==>")
print(start[0:3])
print(start[3:6])
print(start[6:9])
print("----------------------------------")

goal = [
    1,2,3,
    4,5,6,
    7,8,0
]

def heuristic(state):
    h = 0
    for i in range(9):
        if state[i] != 0:
            target = goal.index(state[i])
            h += abs(i // 3 - target // 3)
            h += abs(i % 3 - target % 3)

    return h

open_list = [start]
visited = []

while open_list:
    current = open_list[0]
    for state in open_list:
        if heuristic(state) < heuristic(current):
            current = state

    open_list.remove(current)

    if current == goal:
        print("===Goal is reached===")
        print(current[0:3])
        print(current[3:6])
        print(current[6:9])
        break

    visited.append(current)
    zero = current.index(0)
    moves = [-3, 3, -1, 1]

    for move in moves:
        new_pos = zero + move

        if 0 <= new_pos < 9:
            if abs(zero % 3 - new_pos % 3) <= 1:
                new_state = current.copy()

                new_state[zero], new_state[new_pos] = new_state[new_pos], new_state[zero]

                if new_state not in visited and new_state not in open_list:
                    open_list.append(new_state)

else:
    print("----No Solution found----")