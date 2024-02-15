import random

def partition(x, nums):
    i1, i2 = -1, -1
    for i in range(len(nums)):
        if nums[i] < x:
            if i == 0:
                i1 = 0
                i2 = 0
            else:
                k = nums[i]
                if i1 == i2 or i == i2 + 1:
                    nums[i] = nums[i1+1]
                    nums[i1+1] = k
                else:
                    nums[i] = nums[i2 + 1]
                    nums[i2 + 1] = nums[i1+1]
                    nums[i1+1] = k
                i1 += 1
                i2 += 1
        elif nums[i] == x:
            if i == 0:
                i2 = 0
            else:
                k = nums[i]
                nums[i] = nums[i2 + 1]
                nums[i2+1] = k
                i2 += 1
    return(i1, i2)

def q_sort(nums):
    if len(nums) == 1:
        return nums
    pred = random.choice(nums)
    a, b = partition(pred, nums)
    if a == -1:
        if b == len(nums) - 1:
            return nums
        return nums[a+1:b+1] + q_sort(nums[b+1:])
    if b == len(nums) - 1:
        return q_sort(nums[:a+1]) + nums[a+1:]
    return q_sort(nums[:a+1]) + nums[a+1:b+1] + q_sort(nums[b+1:])

n = int(input())
if n == 0:
    print('')
else:
    nums = list(map(int, input().split()))
    print(' '.join(str(el) for el in q_sort(nums)))
    