def z_func(str1):
    n = len(str1)
    result = [0]*len(str1)
    l, r = 0, 0
    for i in range(1, n):
        if i <= r:
            result[i] = min(r-i+1, result[i-l])
        while i + result[i] < n and str1[i + result[i]] == str1[result[i]]:
            result[i] += 1
        if i + result[i] - 1 > r:
            r = i + result[i] - 1
            l = i
    return result
        

s = input()
if len(s) == 0: print('')
else: print(' '.join(map(str, z_func(s))))