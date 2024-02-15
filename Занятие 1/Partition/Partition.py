def partition(x, nums, n):
    i1, i2 = -1, -1
    for i in range(n):
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

n = int(input())   
nums = list(map(int, input().split()))
x = int(input())

a, b = partition(x, nums, n)
print(a+1)
print(n - a - 1)