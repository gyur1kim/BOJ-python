'''
5
1 6
3 7
6 2
7 100
9 635

'''

tc = int(input())
for v in range(tc):
    a, b = map(int, input().split())
    res = a**(b%4 or 4) % 10 or 10
    print(res)

# for v in  {
#     const [a, b] = input[i].split(" ");
#     const result = a ** (b % 4 || 4) % 10 || 10;
#     console.log(result);
# }