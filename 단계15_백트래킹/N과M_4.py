import sys
sys.stdin = open('N과M_4.txt')

def combination_H(i, depth):
    if depth == b:
        global ans
        ans += ' '.join(map(str, lst)) + '\n'
        return

    for i in range(i, a+1):
        lst.append(i)
        combination_H(i, depth + 1)
        lst.pop()


ans = ''
a, b = map(int, input().split())
lst = []
combination_H(1, 0)
print(ans)