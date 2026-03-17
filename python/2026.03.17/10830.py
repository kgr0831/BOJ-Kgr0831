import sys
input = sys.stdin.readline
 
MOD = 1000
 
def mat_mul(A, B, n):
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            s = 0
            for k in range(n):
                s += A[i][k] * B[k][j]
            C[i][j] = s % MOD
    return C
 
def mat_pow(M, b, n):
    # 단위 행렬로 초기화
    result = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    while b:
        if b & 1:
            result = mat_mul(result, M, n)
        M = mat_mul(M, M, n)
        b >>= 1
    return result
 
N, B = map(int, input().split())
A = []
for _ in range(N):
    row = list(map(int, input().split()))
    A.append([x % MOD for x in row])
 
ans = mat_pow(A, B, N)
for row in ans:
    print(*row)