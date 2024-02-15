def merge(nums1, nums2):
    i = 0
    j = 0
    nums = []
    while i < len(nums1) or j < len(nums2):
        if i == len(nums1):
            nums.append(nums2[j])
            j += 1
        elif j == len(nums2) or nums1[i] <= nums2[j]:
            nums.append(nums1[i])
            i += 1
        else:
            nums.append(nums2[j])
            j += 1
    return nums

def merge_sort(nums):
    if len(nums) == 1:
        return nums
    return merge(merge_sort(nums[:(len(nums)//2)]), merge_sort(nums[(len(nums)//2):]))

n = int(input())
if n == 0:
    print('')
else:
    nums = list(map(int, input().split()))
    print(' '.join(str(el)for el in merge_sort(nums)))