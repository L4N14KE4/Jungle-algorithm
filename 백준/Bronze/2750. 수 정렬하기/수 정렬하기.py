N = int(input())
nums = []
for i in range(N):
    num = int(input())
    nums.append(num)
new_nums  = sorted(set(nums))

for i in range(len(new_nums)):
    print(new_nums[i])