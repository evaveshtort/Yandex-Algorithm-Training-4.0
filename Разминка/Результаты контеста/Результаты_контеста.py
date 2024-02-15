a = int(input())
b = int(input())
n = int(input())

max_first = a
min_second = b // n
if b % n != 0:
    min_second += 1
if max_first <= min_second:
    print('No')
else:
    print('Yes')
