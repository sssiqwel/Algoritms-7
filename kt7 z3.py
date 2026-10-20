import heapq

n = 4
stations = [2, 4]
roads = [
    (1, 2, 3),
    (2, 3, 4),
    (3, 4, 1),
]

graph = [[] for _ in range(n + 1)]
for u, v, length in roads:
    graph[u].append((v, length))
    graph[v].append((u, length))

INF = 10 ** 18
distance = [INF] * (n + 1)
nearest = [-1] * (n + 1)
queue = []
for station in stations:
    distance[station] = 0
    nearest[station] = station
    heapq.heappush(queue, (0, station, station))

while queue:
    current, station, city = heapq.heappop(queue)
    if current != distance[city] or station != nearest[city]:
        continue
    for nxt, length in graph[city]:
        candidate = current + length
        if candidate < distance[nxt] or (candidate == distance[nxt] and station < nearest[nxt]):
            distance[nxt] = candidate
            nearest[nxt] = station
            heapq.heappush(queue, (candidate, station, nxt))

for city in range(1, n + 1):
    if nearest[city] == -1:
        print(-1, -1)
    else:
        print(nearest[city], distance[city])
