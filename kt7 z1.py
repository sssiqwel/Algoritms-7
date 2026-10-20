import heapq

n = 4
s = 1
roads = [
    (1, 2, 4),
    (1, 3, 2),
    (3, 2, 1),
    (2, 4, 5),
    (3, 4, 10),
]

graph = [[] for _ in range(n + 1)]
for start, finish, time in roads:
    graph[start].append((finish, time))

INF = 10 ** 18
distance = [INF] * (n + 1)
distance[s] = 0
queue = [(0, s)]
while queue:
    current, city = heapq.heappop(queue)
    if current != distance[city]:
        continue
    for nxt, time in graph[city]:
        candidate = current + time
        if candidate < distance[nxt]:
            distance[nxt] = candidate
            heapq.heappush(queue, (candidate, nxt))

for city in range(1, n + 1):
    if distance[city] >= INF:
        print("INF")
    else:
        print(distance[city])
