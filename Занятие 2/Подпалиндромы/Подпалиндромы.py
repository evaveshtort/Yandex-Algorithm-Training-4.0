def calc_pal(str1):
    d1 = [0] * len(str1)
    l, r = 0, 0
    for i in range(len(str1)):
        if i <= r:
            d1[i] = min(d1[l+r-i], r - i + 1)
        while i + d1[i] < len(str1) and i - d1[i] + 1 > 0 and str1[i+d1[i]] == str1[i-d1[i]]:
            d1[i] += 1
        if i + d1[i] - 1 > r:
            r = i + d1[i] - 1
            l = i - d1[i] + 1
    d2 = [0] * (len(str1) - 1)
    l, r = -1, -1
    for i in range(len(str1) - 1):
        if i < r:
            d2[i] = min(d2[l+r-i-1], r - i)
        while i - d2[i] + 1 > 0 and i + d2[i] < len(str1) - 1 and str1[i + d2[i] + 1] == str1[i - d2[i]]:
            d2[i] += 1
        if i + d2[i] > r:
            r = i + d2[i]
            l = i - d2[i] + 1
    return (sum(d1) + sum(d2))

s = input()
print(calc_pal(s))
            
        
