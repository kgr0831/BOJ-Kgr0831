import sys

input = sys.stdin.readline

def get_result(money: int):
    units = [25, 10, 5, 1]
    result = []
    
    for unit in units:
        count = money // unit
        money %= unit
        result.append(count)
        
    return result

input_count = int(input())

for _ in range(input_count):
    money = int(input())
    res = get_result(money)
    print(f"{res[0]} {res[1]} {res[2]} {res[3]}")