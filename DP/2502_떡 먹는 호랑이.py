day, k = map(int, input().split())  # 할머니가 넘어온 날, 떡의 개수

fibo = [1, 1]
for i in range(day-3):
    fibo.append(fibo[i] + fibo[i+1])

# print(fibo)
# print(fibo[-1])
# print(fibo[-2])

a = 1
while True:
    if (k - a*fibo[-2]) % fibo[-1] == 0:
        print(a)
        print((k - a*fibo[-2]) // fibo[-1])
        break
    a += 1