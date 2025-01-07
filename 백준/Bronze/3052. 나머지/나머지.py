arr = []

for i in range (1,11):
    num = int(input())
    K = str(num % 42)
    if K not in arr:    
        arr.append(K)

print(len(arr))