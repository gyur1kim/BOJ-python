def foo(tmp):
    if len(tmp) == M:
        seq.append(tmp[:])
        return

    for i in range(1, N+1):
        if i not in tmp:
            tmp.append(i)
            foo(tmp)
            tmp.pop()
    # return seq

N, M = 4, 4
tmp = []
seq = []
foo(tmp)
for s in seq:
    print(*s)