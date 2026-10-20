import heapq

n = 3
s = 1
t = 3
roads = [
    (1, 2, 5),
    (2, 3, 5),
    (1, 3, 9),
]

graph = [[] for _ in range(n + 1)]
for start, finish, cost in roads:
    graph[start].append((finish, cost))

INF = 10 ** 18
distance = [[INF, INF] for _ in range(n + 1)]
distance[s][0] = 0
queue = [(0, s, 0)]
while queue:
    current, city, used = heapq.heappop(queue)
    if current != distance[city][used]:
        continue
    for nxt, cost in graph[city]:
        candidate = current + cost
        if candidate < distance[nxt][used]:
            distance[nxt][used] = candidate
            heapq.heappush(queue, (candidate, nxt, used))
        if used == 0:
            candidate = current + cost // 2
            if candidate < distance[nxt][1]:
                distance[nxt][1] = candidate
                heapq.heappush(queue, (candidate, nxt, 1))

answer = min(distance[t])
if answer >= INF:
    print(-1)
else:
    print(answer)
