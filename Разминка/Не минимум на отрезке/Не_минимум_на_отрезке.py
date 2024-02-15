n, m = map(int, input().split())
nums = list(map(int, input().split()))
for _ in range(m):
    l, r = map(int, input().split())
    flag = False
    for i in range(l+1, r+1):
        if nums[i] < nums[i-1]:
            print(nums[i-1])
            flag = True
            break
        if nums[i] > nums[i-1]:
            print(nums[i])
            flag = True
            break
    if not flag: print('NOT FOUND')