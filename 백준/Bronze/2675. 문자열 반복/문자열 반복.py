TestCase = int(input())
for i in range (TestCase):
    i += i
    R, S = map(str, input().split())
    S = list(S)
    for i in S:
        print(i*int(R), end = '') #end = ''  옆으로 붙임
    print() # 줄넘김


