tree = [3,5,6,9,1,2,0,-1]

def alphabeta(depth, node, alpha, beta, maximizing):
    if depth == 3:
        return tree[node]

    if maximizing:
        best = -999

        for i in range(2):
            value = alphabeta(depth + 1, node * 2 + i, alpha, beta, False)

            best = max(best, value)
            aplha = max(alpha, value)

            if alpha >= beta:
                break

        return best
    else: 
        best = 999
        for i in range(2):
            value = alphabeta(depth + 1, node * 2 + i, alpha, beta, True)

            best = min(best, value)
            beta = min(beta, value)

            if beta <= alpha:
                break
        return best

result = alphabeta(0, 0, -999, 999, True)
print("Optimal Value :", result)