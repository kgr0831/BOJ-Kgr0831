# https://www.acmicpc.net/problem/2920

# 다장조는 c d e f g a b C, 총 8개 음으로 이루어져있다.
# 이 문제에서 8개 음은 다음과 같이 숫자로 바꾸어 표현한다.
# c는 1로, d는 2로, ..., C를 8로 바꾼다.
# 1부터 8까지 차례대로 연주한다면 ascending,
# 8부터 1까지 차례대로 연주한다면 descending, 둘 다 아니라면 mixed 이다.
# 연주한 순서가 주어졌을 때, 이것이 ascending인지, descending인지,
# 아니면 mixed인지 판별하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

data = list(map(int, input().split()))

ascending_data = merge_sort(data)
descending_data = ascending_data[::-1]

if data == ascending_data:
    print("ascending")
elif data == descending_data:
    print("descending")
else:
    print("mixed")