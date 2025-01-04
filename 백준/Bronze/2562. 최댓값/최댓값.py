nums = []

for i in range (9):
    a = int(input())
    nums.append(a)

print(max(nums))
print(nums.index(max(nums))+1)
