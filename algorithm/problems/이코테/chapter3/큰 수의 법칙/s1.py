import sys
sys.stdin = open("input.txt", "r")

# sys.stdin.readline() => 한 줄씩 받아옴
T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, sys.stdin.readline().split())
    lst = list(map(int, sys.stdin.readline().split()))

    lst.sort(reverse=True)
    if M <= K:
        result = M*lst[0]
        print(f'#{tc} {result}')
    else:
        if lst[0] == lst[1]:
            result = lst[0]*K*2*(M // (K*2)) + lst[0]*(M % (K*2))
            print(f'#{tc} {result}')
        else:
            result = (lst[0]*K + lst[1])*(M // (K+1) + lst[0]*(M % (K+1)))
            print(f'#{tc} {result}')

