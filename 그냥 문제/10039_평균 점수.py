add = 0
for _ in range(5):
    score = int(input())
    add += score if score > 40 else 40
print(add//5)