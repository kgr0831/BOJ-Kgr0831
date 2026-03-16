import sys
input = sys.stdin.readline

n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]

INF = float('inf')
ALL = (1 << n) - 1
dp = [[INF] * n for _ in range(1 << n)]

for city in range(n):
    if cost[city][0] > 0:
        dp[ALL][city] = cost[city][0]

for visited in range(ALL, 0, -1):
    for city in range(n):
        if dp[visited][city] == INF:
            continue
        if not (visited & (1 << city)):
            continue
        prev_visited = visited ^ (1 << city)
        if prev_visited == 0:
            continue
        for prev in range(n):
            if not (prev_visited & (1 << prev)):
                continue
            if cost[prev][city] == 0:
                continue
            val = cost[prev][city] + dp[visited][city]
            if val < dp[prev_visited][prev]:
                dp[prev_visited][prev] = val

print(dp[1][0])