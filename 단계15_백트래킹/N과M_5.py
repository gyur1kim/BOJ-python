import sys
sys.stdin = open('N과M_5.txt')


'''
백트래킹으로 푸는 문제였다..!!
'''
def product(depth):
    if depth == b:
        print(*ansLst)
        return

    for i in range(a):
        if visited[i]:
            continue

        visited[i] = True
        ansLst.append(inputLst[i])
        product(depth+1)
        visited[i] = False
        ansLst.pop()


a, b = map(int, input().split())
inputLst = sorted(list(map(int, input().split())))
map(int, inputLst)
visited = [False] * a
ansLst = []
product(0)