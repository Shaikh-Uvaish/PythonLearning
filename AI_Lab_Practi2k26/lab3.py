# A* Algorithm for 8 Puzzle Problem

# Initial and Goal states
start = [1, 2, 3,
         4, 0, 6,
         7, 5, 8]

goal = [1, 2, 3,
        4, 5, 6,
        7, 8, 0]


# Function to calculate Manhattan Distance
def heuristic(state):
    h = 0

    for i in range(9):
        if state[i] != 0:
            target = goal.index(state[i])

            # Calculate row and column distance
            h += abs(i // 3 - target // 3)
            h += abs(i % 3 - target % 3)

    return h


# A* Algorithm
open_list = [start]
visited = []

while open_list:

    # Find state with lowest heuristic value
    current = open_list[0]

    for state in open_list:
        if heuristic(state) < heuristic(current):
            current = state

    open_list.remove(current)

    # Check if goal is reached
    if current == goal:
        print("Goal State Reached!")
        print(current[0:3])
        print(current[3:6])
        print(current[6:9])
        break

    visited.append(current)

    # Find blank space position
    zero = current.index(0)

    # Possible movements
    moves = [-3, 3, -1, 1]

    for move in moves:
        new_pos = zero + move

        # Check valid movement
        if 0 <= new_pos < 9:

            # Prevent left-right boundary crossing
            if abs(zero % 3 - new_pos % 3) <= 1:

                new_state = current.copy()

                # Swap blank with adjacent tile
                new_state[zero], new_state[new_pos] = new_state[new_pos], new_state[zero]

                if new_state not in visited and new_state not in open_list:
                    open_list.append(new_state)

else:
    print("No solution found")
