import sys
sys.stdin = open('15829.txt')

L = int(input())
words = input()
ans = 0
for i in range(L):
    ans += (ord(words[i]) - ord('a') + 1) * 31**i
print(ans%1234567891)