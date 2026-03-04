# https://www.acmicpc.net/problem/8393
# n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

inputIdx = int(input())

resultIdx = 0
for i in range(1, inputIdx + 1) : 
    resultIdx += i

print(resultIdx)