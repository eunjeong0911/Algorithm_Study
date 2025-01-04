n, m = map(int, input().split())
nums = list(map(int, input().split()))

for i in nums:
    if(m > i):
        print(i, end = " ")