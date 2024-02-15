n, s, f = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))
    
dist = [-1]*(n+1)
dist[s] = 0
vis = [False]*(n+1)
vis[s] = True
prev = [0]*(n+1)
i = s-1
count = 0
min_unvis = 0

while min_unvis != -1:
    min_unvis = -1
    rem = 0
    for j in range(n):
        if matrix[i][j] != -1 and i != j:
            if dist[j+1] == -1 or (matrix[i][j] + dist[i+1] < dist[j+1]):
                dist[j+1] = matrix[i][j] + dist[i+1]
                prev[j+1] = i+1
        if not vis[j+1] and (dist[j+1] < min_unvis and dist[j+1] != -1 or min_unvis == -1):
            min_unvis = dist[j+1]
            rem = j
    i = rem
    vis[i+1] = True
  
if dist[f] == -1:
    print(-1)
else:
    path = []
    j = f
    while j != s:
        path.insert(0, j)
        j = prev[j]

    path.insert(0, s)
    print(' '.join(map(str, path)))
