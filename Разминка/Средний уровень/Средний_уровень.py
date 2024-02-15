n = int(input())
nums = list(map(int, input().split()))

k1 = sum(el for el in nums) - n*nums[0]
for i in range(1, len(nums)):
    k2 = k1 + (i-1)*(nums[i] - nums[i-1]) + (n-i-1)*(nums[i-1]-nums[i])
    nums[i-1] = k1
    k1 = k2
nums[n-1] = k1

print(' '.join(str(el) for el in nums))