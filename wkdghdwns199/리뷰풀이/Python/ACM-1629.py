import sys
input = sys.stdin.readline

def power(A,B,C):
    if (B == 1) : return A%C
    else :
        temp = power(A,B//2, C)
        if (B%2 == 0) : return temp * temp % C
        else : return temp * temp * A % C

A,B,C = map(int, input().split())
print(power(A,B,C))