N, R, C = map(int, input().split())
answer =0

while N :
    N-=1
    if R<2**N and C<2**N :
        answer += (2**N) * (2**N) * 0
    elif R<2**N and C>=2**N :
        answer += (2**N) * (2**N) * 1
        C-= (2**N)
    elif R>=2**N and C<2**N :
        answer += (2**N) * (2**N) * 2
        R-=(2**N)
    elif R>=2**N and C>=2**N :
        answer += (2**N) * (2**N) * 3
        R-=(2**N)
        C-= (2**N)

print(answer)