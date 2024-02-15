file = open("input.txt", "r")

n = int(file.readline())
nums = [0]*n
for i in range(n):
    nums[i] = file.readline().strip('\n')

    
file.close
file = open("output.txt", "w")
    
file.write('Initial array:\n'+ ', '.join(el for el in nums) + '\n**********')

place = len(nums[0]) - 1
for i in range(len(nums[0])):
    file.write('\nPhase {}\n'.format(i+1))
    buckets = [[] for i in range(10)]
   
    for j in range(n):
        buckets[int(nums[j][place])].append(nums[j])
    for k in range(len(buckets)):
        if len(buckets[k]) == 0:
            file.write('Bucket {}: empty\n'.format(k))
        else:
            file.write('Bucket {}: '.format(k) + ', '.join(el for el in buckets[k]) + '\n')
    place -= 1
    file.write('**********')
    nums = [el for bucket in buckets for el in bucket]

file.write('\nSorted array:\n')
file.write(', '.join(el for el in nums))
file.close