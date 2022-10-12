import sys
sys.stdin = open('9663.txt')

'''
한 곳에 놓는다
-> 다음 말은 그 행에 못 놓는다
   그 열에도 놓을 수 없음 -> 겹치는 열이 잇는지 check해야 함
   대각선도 놓으면 안됨 -> 행 번호와 열 번호까지 check해야 할 듯함
   내가 만약 (1, 3)에 뒀으면, (0, 2), (2, 4), (3, 5)... 에 둘 수 없음
   
'''

def queen(row):
    if row == N:  # 행이 N이다 == 모든 곳을 다 돌았다.
        global cnt
        cnt += 1
        return    # 함수 종료!

    # 열들을 찾아주는 시간간
   for nCol in range(N):
        if chess[row] == False and check(row, nCol):
            chess[row] = nCol
            queen(row+1)
            chess[row] = False


def check(row, col):
    for i in range(N):
        if chess[i] == chess[row] or


N = int(input())

chess = [False] * N  # idx가 행을 뜻하고, 그 안에 들은 값이 열을 뜻한다..
cnt = 0
queen(0)
print(cnt)