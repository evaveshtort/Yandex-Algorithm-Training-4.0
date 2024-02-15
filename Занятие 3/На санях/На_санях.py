import time as ti
import heapq
from collections import defaultdict

n = int(input())
s_t = ti.time()
coachmen = [[]] + [list(map(int, input().split())) for _ in range(n)]
graph = defaultdict(dict)

for _ in range(n - 1):
    a, b, s = map(int, input().split())
    graph[a][b] = s
    graph[b][a] = s

time = [[0] * (n + 1) for _ in range(n + 1)]

for s in range(1, n + 1):
    dist = [-1] * (n + 1)
    dist[s] = 0
    queue = [(0, s)]

    while queue:
        current_distance, current_vertex = heapq.heappop(queue)

        for neighbor, weight in graph[current_vertex].items():
            if dist[neighbor] == -1:
                distance = current_distance + weight
                dist[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
                time[s][neighbor] = distance / coachmen[neighbor][1] + coachmen[neighbor][0]

t = time[1]
next_ = [1] * (n + 1)
vis = [False] * (n + 1)
vis[1] = True
min_unvis = 0
i = 1

max_value = -1  


while min_unvis != -1:
    min_unvis = -1

    for j in range(2, n + 1):
        if i != j and i != 1:
            if t[j] == -1 or (time[i][j] + t[i] < t[j]):
                t[j] = time[i][j] + t[i]
                next_[j] = i

        if not vis[j] and (t[j] < min_unvis and t[j] != -1 or min_unvis == -1):
            min_unvis = t[j]
            rem = j

    i = rem
    vis[i] = True

    if t[i] > max_value:
        max_value = t[i]
        m = i

path = []

while m != 1:
    path.append(m)
    m = next_[m]

path.append(1)
print(max_value)
print(' '.join(map(str, reversed(path))))  

f_t = ti.time()
print(f_t - s_t)

          
    
    

    

            
            
    

            
        
    
