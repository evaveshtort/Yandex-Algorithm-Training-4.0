s1 = input()
s2 = input()

if len(s1) != len(s2):
    print('NO')
    
else:
    d = {}
    for i in range(len(s1)):
        if s1[i] in d:
            d[s1[i]] += 1
        else:
            d[s1[i]] = 1
    flag = False        
    for i in range(len(s2)):
        if not s2[i] in d:
            flag = True
            print('NO')
            break
        d[s2[i]] -= 1
        
    if not flag:
        for i in d.values():
            if i != 0:
                flag = True
                print('NO')
                break
        if not flag:
            print('YES')
            