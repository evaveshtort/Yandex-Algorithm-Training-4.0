import heapq
import time

def dijkstra(n, times, roads):
    graph = {i: [] for i in range(1, n + 1)}

    for road in roads:
        a, b, s = road
        graph[a].append((b, s))
        graph[b].append((a, s))

    time_to_city = [float('inf')] * (n + 1)
    time_to_city[1] = 0

    heap = [(0, 1, 0)]  # (total_time, current_city, current_time)

    while heap:
        total_time, current_city, current_time = heapq.heappop(heap)

        if current_time > time_to_city[current_city]:
            continue

        for next_city, distance in graph[current_city]:
            next_time = current_time + distance
            next_total_time = next_time + times[next_city][0] / times[next_city][1]

            if next_total_time < time_to_city[next_city]:
                time_to_city[next_city] = next_total_time
                heapq.heappush(heap, (next_total_time, next_city, next_time))

    max_time = max(time_to_city[1:])
    return max_time, path_to_last_participant(time_to_city, max_time, times)


def path_to_last_participant(time_to_city, max_time, times):
    last_participant_city = time_to_city.index(max_time)

    current_city = last_participant_city
    path = [last_participant_city]

    while current_city != 1:
        min_time_from_prev_city = float('inf')
        next_city = None

        for neighbor, distance in graph[current_city]:
            total_time_from_prev_city = time_to_city[neighbor] - times[neighbor][0] / times[neighbor][1]
            if total_time_from_prev_city < min_time_from_prev_city:
                min_time_from_prev_city = total_time_from_prev_city
                next_city = neighbor

        path.append(next_city)
        current_city = next_city

    return path[::-1]


def main():
    n = int(input())
    times = [list(map(int, input().split())) for _ in range(n)]
    roads = [tuple(map(int, input().split())) for _ in range(n - 1)]

    start_time = time.time()
    max_time, last_participant_path = dijkstra(n, times, roads)
    end_time = time.time()
    print(f"Максимальное время: {max_time} часов")
    print("Путь последнего участника:", *last_participant_path)
    print(f"Время выполнения программы: {end_time - start_time} секунд")


if __name__ == "__main__":
    main()


