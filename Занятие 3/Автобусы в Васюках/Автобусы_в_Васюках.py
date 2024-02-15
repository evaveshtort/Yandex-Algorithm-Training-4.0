import heapq

n = int(input())
d, v = map(int, input().split())
r = int(input())
schedule = {}
for _ in range(r):
    a, t1, b, t2 = map(int, input().split())
    if a not in schedule.keys():
        schedule[a] = {}
    if b not in schedule[a].keys():
        schedule[a][b] = []
    schedule[a][b].append([t1, t2])
   
time = [-1]*(n+1)
time[d] = 0

queue = [(0, d)]
while queue:
    current_time, current_village = heapq.heappop(queue)
    if current_time > time[current_village] or current_village not in schedule.keys():
        continue
    for neighbor, cur_sch in schedule[current_village].items():
        flag = False
        for bus in cur_sch:
            if bus[0] >= current_time and (bus[1] < time[neighbor] or time[neighbor] == -1):
                time[neighbor] = bus[1]
                flag = True
                
        if flag: heapq.heappush(queue, (time[neighbor], neighbor))
        
print(time[v])