t = int(input())
for _ in range(t):
    n, a, b = map(int, input().split())

    groups = n // a
    res = n % a
    if b-a == 0:
        if res == 0:
            print('YES')
        else:
            print('NO')
    else:
        check = res // (b-a) 
        if res % (b-a) != 0:
            check += 1
        if check <= groups:
            print('YES')
        else:
            print('NO')
    
        
