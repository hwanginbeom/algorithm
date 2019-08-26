N = 12


def placeQueen(queen_pos):
    res = 0
    n = len(queen_pos)
    if n == N:
        return 1
    for i in range(N):
        for j in range(n):
            if i == queen_pos[j]:
                break
            if n - j == i - queen_pos[j]:
                break
            if n - j == queen_pos[j] - i:
                break
        else:
            res += placeQueen(queen_pos + [i])
    return res


print(placeQueen([]))
