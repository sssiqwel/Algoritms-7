n = 4
s = 1
roads = [
    (1, 2, 5),
    (2, 3, -2),
    (1, 3, 10),
]

INF = 10 ** 18
distance = [INF] * (n + 1)
distance[s] = 0
for _ in range(n - 1):
    updated = False
    for start, finish, cost in roads:
        if distance[start] < INF and distance[start] + cost < distance[finish]:
            distance[finish] = distance[start] + cost
            updated = True
    if not updated:
        break

for city in range(1, n + 1):
    if distance[city] >= INF:
        print("INF")
    else:
        print(distance[city])
