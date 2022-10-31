# N: 동전의 종류, K: 가격
N, K = map(int, input().split())
coins = []

for i in range(N):
    if (n := int(input())) <= K:
        coins.append(n)
        continue
    break

coinNums = 0
idx = -1
while K:
    coinNums += K // coins[idx]
    K = K % coins[idx]
    idx -= 1

print(coinNums)
exit()