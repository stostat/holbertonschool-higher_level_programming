#!/usr/bin/python3
"""Advanced exercise."""


from sys import argv, exit as status

if len(argv) != 2:
    print("Usage: nqueens N")
    status(1)
try:
    N = int(argv[1])
except ValueError:
    print("N must be a number")
    status(1)
if N < 4:
    print("N must be at least 4")
    status(1)

queens = [[i, -1] for i in range(N)]


def my_queen(queen):
    """Find out if queen already positioned"""
    for i in range(N):
        if queens[i][1] == queen:
            return True
    return False


def my_board(pos, queen):
    """solve game."""
    if my_queen(queen):
        return False
    i = 0
    while i < pos:
        if abs(queens[i][1] - queen) == abs(i - pos):
            return False
        i += 1
    return True


def solution(queen):
    """Backtracking."""
    for count in range(N):
        for i in range(queen, N):
            queens[i][1] = -1
        if my_board(queen, count):
            queens[queen][1] = count
            if queen == N - 1:
                print(queens)
            else:
                solution(queen + 1)


if __name__ == '__main__':
    QUEEN = 0
    solution(QUEEN)
