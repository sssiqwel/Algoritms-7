n = 3
s = 1
t = 3
k = 2
roads = [
    (1, 2, 1),
    (2, 3, 1),
    (1, 3, 5),
    (1, 3, 2),
]

MOD = 1_000_000_007
BIG = 10 ** 30
best = [[BIG] * (n + 1) for _ in range(k + 1)]
count = [[0] * (n + 1) for _ in range(k + 1)]
best[0][s] = 0
count[0][s] = 1

for edges_used in range(k):
    for start, finish, cost in roads:
        if best[edges_used][start] >= BIG:
            continue
        candidate = best[edges_used][start] + cost
        if candidate < best[edges_used + 1][finish]:
            best[edges_used + 1][finish] = candidate
            count[edges_used + 1][finish] = count[edges_used][start]
        elif candidate == best[edges_used + 1][finish]:
            count[edges_used + 1][finish] = (
                count[edges_used + 1][finish] + count[edges_used][start]
            ) % MOD

answer = BIG
ways = 0
for edges_used in range(k + 1):
    if best[edges_used][t] < answer:
        answer = best[edges_used][t]
        ways = count[edges_used][t] % MOD
    elif best[edges_used][t] == answer:
        ways = (ways + count[edges_used][t]) % MOD

if answer >= BIG:
    print("IMPOSSIBLE")
else:
    print(answer, ways)
