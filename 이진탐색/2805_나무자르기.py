import sys
sys.stdin = open('2805.txt')

N, M = map(int, input().split())         # N: 나무 갯수, M: 필요한 나무 길이
trees = list(map(int, input().split()))

start, end = 0, 10**9
pieces = (start+end)//2 * (N + 1)  # 일단 임시로 넣어준 값
H = 0
while start <= end:
    tmpH = (start+end)//2   # 지면으로부터 몇 m 떨어진 높이에서 자를건지!
    tmpPieces = 0           # 임시로 저장할 나무 잘랐을 때 가져갈 수 있는 길이

    for tree in trees:
        if tree - tmpH > 0:
            tmpPieces += tree - tmpH

    if tmpPieces == M:    # 만약 내가 원하는 길이가 따아아악 나오면!!!!!
        H = tmpH          # 내가 잘라야하는 높이인거지
        break
    elif tmpPieces > M:   # 내가 원하는 길이보다 임시로 잘라본 나무의 길이가 더 길면?
        if pieces and pieces > tmpPieces:
            pieces = tmpPieces
            H = tmpH
        else:        # 기존의
            pieces = tmpPieces
            H = tmpH
        start = tmpH + 1
    else:
        end = tmpH - 1

print(H)