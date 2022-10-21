N, L = map(int, input().split())

for l in range(L, 101):
    a = N / l - (l - 1) / 2
    if a.is_integer():
        if a < 0:
            print(-1)
            break
        a = int(a)
        for j in range(a, a + l):
            print(j, end=" ")
        break
else:
    print(-1)