import sys
sys.stdin = open('N과M_6.txt')


'''
백트래킹으로 푸는 문제였다..!!
'''
def combination(idx, depth):
    if depth == b:
        print(*ansLst)
        return

    for i in range(idx, a):
        if visited[i]:
            continue

        visited[i] = True
        ansLst.append(inputLst[i])
        combination(i + 1, depth + 1)
        visited[i] = False
        ansLst.pop()


a, b = map(int, input().split())
inputLst = list(map(str, sorted(list(map(int, input().split())))))
visited = [False] * a
ansLst = []
combination(0, 0)