
start = (3, 3, 0)
goal = (0, 0, 1)

moves = [(2, 0), (0, 2), (1, 1), (1, 0), (0, 1)]


def is_valid(m, c):

    if not (0 <= m <= 3 and 0 <= c <= 3):
        return False

    mr, cr = 3 - m, 3 - c

    return (m == 0 or m >= c) and (mr == 0 or mr >= cr)


def dfs(state, visited):

    if state == goal:
        return [state]

    visited.add(state)
    m, c, boat = state

    for dm, dc in moves:

        if boat == 0:
            nm, nc = m - dm, c - dc
        else:
            nm, nc = m + dm, c + dc

        new_state = (nm, nc, 1 - boat)

        if is_valid(nm, nc) and new_state not in visited:
            path = dfs(new_state, visited)

            if path:
                return [state] + path

    return None


solution = dfs(start, set())

if solution:
    print("Solution Found:")
    for state in solution:
        print(state)
else:
    print("No Solution Found")
