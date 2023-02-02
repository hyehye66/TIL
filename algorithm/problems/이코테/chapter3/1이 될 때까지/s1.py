import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, sys.stdin.readline().split())
    temp = K
    i = 1
    while True:
        i += 1
        temp *= K
        if temp <= N < temp*K:
            if temp == N:
                print(f'#{tc} {i}')
            else:
                print(f'#{tc} {i + (N-temp)}')
            break




