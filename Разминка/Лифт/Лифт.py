k = int(input())
n = int(input())

result = 0
rem = [0]*n

for i in range(n):
    a = int(input())
    result += (i+1)*2*(a // k)
    rem[i] = a%k
    
j = n-1
free = k
while(j>=0):
    if rem[j] == 0:
        j -= 1
    else:
        if free == k:
            cur = j
        if rem[j] <= free:
            free -= rem[j]
            j -= 1
        else:
            rem[j] -= free
            free = 0
        if free == 0:
            result += (cur+1)*2
            free = k
            
if free != k:
    result += (cur+1)*2
            
print(result)
            