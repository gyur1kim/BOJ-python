n = list(map(int, input()))

if sum(n) % 3:
    print(-1)
else:
    n = sorted(n, reverse=True)
    if n[-1]:
        print(-1)
    else:
        n = int(''.join(map(str, n)))
        print(n)