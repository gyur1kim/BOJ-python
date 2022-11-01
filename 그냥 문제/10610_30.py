# n = list(map(int, input()))
#
# if sum(n) % 3:
#     print(-1)
# else:
#     n = sorted(n, reverse=True)
#     if n[-1]:
#         print(-1)
#     else:
#         n = int(''.join(map(str, n)))
#         print(n)


## 숫자를 str로 바꾸는 데에는 O(logn)의 시간이 걸린다......
## str로 안바꾸고 출력하면 어떨까
n = list(map(int, input()))
if sum(n) % 3:
    print(-1)
else:
    n = sorted(n, reverse=True)
    if n[-1]:
        print(-1)
    else:
        print(*n, sep="")


## 이 방법이 제일 빠르다
N_list = sorted(list(map(int, input())), reverse=True)
print(-1) if N_list[-1] or sum(N_list) % 3 else print(*N_list, sep="")

'''
파이썬에서 print할 때 항상 end만 사용했는데 sep을 새롭게 배웠다.
'''
