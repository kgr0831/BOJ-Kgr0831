# https://www.acmicpc.net/problem/10952

# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

results = list()

while True :
    a, b = map(int, input().split())
    
    if a == 0 and b == 0 :
        for result in results :
            print(result)
        break

    results.append(a + b)