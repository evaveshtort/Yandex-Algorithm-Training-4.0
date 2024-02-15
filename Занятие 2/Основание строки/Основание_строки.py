x = 257
p = 10**9 + 7
def create_hash(str1):
    str1 = ' ' + str1
    h = [0] * len(str1)
    xs = [0] * len(str1)
    xs[0] = 1
    for i in range(1, len(str1)):
        h[i] = (h[i-1] * x + ord(str1[i]))%p
        xs[i] = (xs[i-1] * x)%p
    return h, xs

def equal(h, xs, fr1, fr2, l):
    return (h[fr1 + l] + h[fr2]*xs[l])%p == (h[fr2 + l] + h[fr1]*xs[l])%p

s = input()
h, xs = create_hash(s)
max_l = len(s)
for i in range(1, len(s)):
    if equal(h, xs, 0, i, len(s) - i):
        max_l = i
        break
    
print(max_l)