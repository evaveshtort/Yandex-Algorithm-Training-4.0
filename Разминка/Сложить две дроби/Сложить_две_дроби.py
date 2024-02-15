a, b, c, d = map(int, input().split())

x = a*d + c*b
y = b*d

def NOD(x, y):
    if x%y == 0: return y
    else: return NOD(y, x%y)

nod = NOD(x, y)

print(int(x/nod), int(y/nod))