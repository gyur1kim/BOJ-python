import sys
sys.stdin = open('2580.txt')


def search(i, j):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                


sudoku = [list(map(int, input().split())) for _ in range(9)]
