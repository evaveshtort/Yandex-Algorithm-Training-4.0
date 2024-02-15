import heapq

n, k = map(int, input().split())
graph = {}
for _ in range(k):
    a, b, l = map(int, input().split())
    if a not in graph.keys():
        graph[a] = {}
    if b not in graph.keys():
        graph[b] = {}
    graph[a][b] = l
    graph[b][a] = l
    
s, f = map(int, input().split())

if not s in graph.keys():
    print(-1)
    
else:
    dist = [-1]*(n+1)
    dist[s] = 0
    queue = [(0, s)]
    while queue:
        current_distance, current_vertex = heapq.heappop(queue)
        if current_distance > dist[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < dist[neighbor] or dist[neighbor] == -1:
                dist[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
            
    print(dist[f])

