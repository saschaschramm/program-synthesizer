def minPath(grid, k):
    n = len(grid)
    if k == 1:
        return [grid[0][0]]
    if k == n * n:
        return [grid[i][j] for i in range(n) for j in range(n)]
    if k < n:
        return [grid[0][i] for i in range(k)]
    if k % n == 0:
        return [grid[i][0] for i in range(k // n)]
    if k < 2 * n:
        return [grid[0][i] for i in range(k - n)] + [grid[k - n][0]]
    if k % n == 1:
        return [grid[i][0] for i in range(k // n - 1)] + [grid[k // n - 1][0]] + [grid[k // n][0]]
    if k < 3 * n:
        return [grid[0][i] for i in range(k - 2 * n)] + [grid[k - 2 * n][0]] + [grid[k - n][0]]
    if k % n == 2:
        return [grid[i][0] for i in range(k // n - 2)] + [grid[k // n - 2][0]] + [grid[k // n - 1][0]] + [grid[k // n][0]]
    if k < 4 * n:
        return [grid[0][i] for i in range(k - 3 * n)] + [grid[k - 3 * n][0]] + [grid[k - 2 * n][0]] + [grid[k - n][0]]
    if k % n == 3:
        return [grid[i][0] for i in range(k // n - 3)] + [grid[k // n - 3][0]] + [grid[k // n - 2][0]] + [grid[k // n - 1][0]] + [grid[k // n][0]]
    if k < 5 * n:
        return [grid[0][i] for i in range(k - 4 * n)] + [grid[k - 4 * n][0]] + [grid[k - 3 * n][0]] + [grid[k - 2 * n][0]] + [grid[k - n][0]]
    if k % n == 4:
        return [grid[i][0] for i in range(k // n - 4)] + [grid[k // n - 4][0]] + [grid[k // n - 3][0]] + [grid[k // n - 2][0]] + [grid[k // n - 1][0]] + [grid[k // n][0]]
    if k < 6 * n:
        return [grid[0][i] for i in range(k - 5 * n)] + [grid[k - 5 * n][0]] + [grid[k - 4 * n][0]] + [grid[k - 3 * n][0]] + [grid[k - 2 * n][0]] + [grid[k - n][0]]
    if k % n == 5:
        return [grid[i][0] for i in range(k // n - 5)] + [grid[k // n - 5][0]] + [grid[k // n - 4][0]] + [grid[k // n - 3][0]] + [grid[k // n - 2][0]] + [grid[k // n - 1][0]] + [grid[k // n][0]]
    if k < 7 * n:
        return [grid[0][i] for i in range(k - 6 * n)] + [grid[k - 6 * n][0]] + [grid[k - 5 * n][0]] + [grid[k - 4 * n][0]] + [grid[k - 3 * n][0]] + [grid[k - 2 * n][0]] + [grid[k - n][0]]
    if k % n == 6:
        return [grid[i][0] for i in range(k // n - 6)] + [grid[k // n - 6][0]] + [grid[k // n - 5][0]] + [grid[k // n - 4][0]] + [grid[k // n - 3][0]] + [grid[k // n - 2][0]] + [grid[k // n - 1][0]] + [grid[k // n][0]]
    if k < 8 * n:
        return [grid[0][i] for i in range(k - 7 * n)] + [grid[k - 7 * n][0]] + [grid[k - 6 * n][0]] + [grid[k - 5 * n][0]] + [grid[k - 4 * n][0]] + [grid[k - 3 * n][0]] + [grid[k - 2 * n][0]] + [grid[k - n][0]]
    if k % n == 7:
        return [grid[i][0] for i in range(k // n - 7)] + [grid[k // n - 7][0]] + [grid[k // n - 6][0]] + [grid[k // n - 5][0]] + [grid[k // n - 4][0]] + [grid[k // n - 3][0]] + [grid[k // n - 2][0]] + [grid[k // n - 1][0]] + [grid[k // n][0]]
    if k < 9 * n:
        return [grid[0][i] for i in range(k - 8 * n)] + [grid[k - 8 * n][0]] + [grid[k - 7 * n][0]] + [grid[k - 6 * n][0]] + [grid[k - 5 * n][0]] + [grid[k - 4 * n][0]] + [grid[k - 3 * n][0]] + [grid[k - 2 * n][0]] + [grid[k - n][0]]
    if k % n == 8:
        return [grid[i][0] for i in range(k // n - 8)] + [grid[k // n - 8][0]] + [grid[k // n - 7][0]] + [grid[k // n - 6][0]] + [grid[k // n - 5][0]] + [grid[k // n - 4][0]] + [grid[k // n - 3][0]] + [grid[k // n -
def check(candidate):

    # Check some simple cases
    print
    assert candidate([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3) == [1, 2, 1]
    assert candidate([[5, 9, 3], [4, 1, 6], [7, 8, 2]], 1) == [1]
    assert candidate([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], 4) == [1, 2, 1, 2]
    assert candidate([[6, 4, 13, 10], [5, 7, 12, 1], [3, 16, 11, 15], [8, 14, 9, 2]], 7) == [1, 10, 1, 10, 1, 10, 1]
    assert candidate([[8, 14, 9, 2], [6, 4, 13, 15], [5, 7, 1, 12], [3, 10, 11, 16]], 5) == [1, 7, 1, 7, 1]
    assert candidate([[11, 8, 7, 2], [5, 16, 14, 4], [9, 3, 15, 6], [12, 13, 10, 1]], 9) == [1, 6, 1, 6, 1, 6, 1, 6, 1]
    assert candidate([[12, 13, 10, 1], [9, 3, 15, 6], [5, 16, 14, 4], [11, 8, 7, 2]], 12) == [1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6]
    assert candidate([[2, 7, 4], [3, 1, 5], [6, 8, 9]], 8) == [1, 3, 1, 3, 1, 3, 1, 3]
    assert candidate([[6, 1, 5], [3, 8, 9], [2, 7, 4]], 8) == [1, 5, 1, 5, 1, 5, 1, 5]

    # Check some edge cases that are easy to work out by hand.
    assert candidate([[1, 2], [3, 4]], 10) == [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
    assert candidate([[1, 3], [3, 2]], 10) == [1, 3, 1, 3, 1, 3, 1, 3, 1, 3]


check(minPath)