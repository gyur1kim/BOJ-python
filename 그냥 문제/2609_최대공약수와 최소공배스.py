a, b = map(int, input().split())

if a<b:
    a, b = b, a
B = b
GCD = 0
while True:
    n = a//b
    if n == 0:
        GCD = b
        break
    else:
        b = n

LCM = a * (int(B/GCD))
print(GCD)
print(LCM)