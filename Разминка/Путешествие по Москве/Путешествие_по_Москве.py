import math

x1, y1, x2, y2 = map(int, input().split())

r1 = math.sqrt(x1**2 + y1**2)
f1 = math.atan2(y1, x1)
r2 = math.sqrt(x2**2 + y2**2)
f2 = math.atan2(y2, x2)
f = min(2*math.pi - abs(f1-f2), abs(f1-f2))

if f <= 2: print(f*min(r1, r2) + abs(r1-r2))
else: print(2*min(r1, r2) + abs(r1-r2))
