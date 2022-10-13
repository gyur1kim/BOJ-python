import sys
sys.stdin = open('9663.txt')

'''
한 곳에 놓는다
-> 다음 말은 그 행에 못 놓는다
   그 열에도 놓을 수 없음 -> 겹치는 열이 잇는지 check해야 함
   대각선도 놓으면 안됨 -> 행 번호와 열 번호까지 check해야 할 듯함
   내가 만약 (1, 3)에 뒀으면, (0, 2), (0, 4)에 둘 수 없음
   
'''

def queen(row):
    # 열들을 찾아주자
    for nCol in range(N):         # 열이 될 수 있는 후보들.. 0부터 N까지
        if not usedCol[nCol]:
            if check(row, nCol):
                if row + 1 == N:
                    global cnt
                    cnt += 1
                    break
                else:
                    chess[row] = nCol
                    usedCol[nCol] = True
                    queen(row + 1)
                    chess[row] = False
                    usedCol[nCol] = False


def check(row, col):
    for i in range(row):   # 기존에 있던 행이랑 내가 넣으려는 row의 col값을 비교하기
        if chess[i] == col or abs(i-row) == abs(chess[i]-col):
            return False
    return True


N = int(input())
chess = [False] * N  # idx가 행을 뜻하고, 그 안에 들은 값이 열을 뜻한다..
usedCol = [False] * N  # 이미 사용한 열인지 확인하기
cnt = 0
queen(0)
print(cnt)