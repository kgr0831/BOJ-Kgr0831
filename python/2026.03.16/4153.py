import sys
input = sys.stdin.readline

results = []

while True:
    a, b, c = map(int, input().split())
    
    if a == 0 and b == 0 and c == 0:
        break

    a, b, c = sorted([a, b, c])
    if a**2 + b**2 == c**2 :
        results.append("right")
    else :
        results.append("wrong")

for result in results :
    print(result)