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

n = int(input())
nums1 = list(map(int, input().split()))
m = int(input())
nums2 = list(map(int, input().split()))
print(' '.join(str(el) for el in merge(nums1, nums2)))
            
