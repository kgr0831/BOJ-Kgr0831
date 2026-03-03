# https://www.acmicpc.net/problem/14940

#지도가 주어지면 모든 지점에 대해서 목표지점까지의 거리를 구하여라.
#문제를 쉽게 만들기 위해 오직 가로와 세로로만 움직일 수 있다고 하자.

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [] # 맵 전체
dist = [[-1] * m for _ in range(n)] # 거리 전체 / 초기값 -1
queue = deque()

for i in range(n) :
    row = list(map(int, input().split())) # 가로 1줄
    graph.append(row)
    for j in range(m) : 
        if row[j] == 2 : # 만약에 목표라면
            queue.append((i,j))
            dist[i][j] = 0 # 여기 거리는 0임 (목표 -> 목표 => 0 거리)
        elif row[j] == 0 : # 만약에 못가는 땅이라면
            dist[i][j] = -1 # 여기는 못가니까 거리 0
        else :
            dist[i][j] = 7

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while queue:
    x, y = queue.popleft() # 하나 뽑기
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i] # 움직이기
        if 0 <= nx < n and 0 <= ny < m: # 맵 안에 있다면
            if dist[nx][ny] == -1 and graph[nx][ny] == 1: # 안 가본땅 / 갈 수 있는 땅 이라면
                dist[nx][ny] = dist[x][y] + 1 # 새로 간 곳의 거리 = 지금 있는 곳의 거리 + 1칸
                queue.append((nx, ny))

for r in dist:
    print(*(r))
# O(N^2)