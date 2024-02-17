import sys
import math

def is_prime(number):
    for i in range(2, int(math.sqrt(number))+1) :
        if number % i == 0 :
            return False
    return True

n = int(sys.stdin.readline().strip())
for _ in range(n):
    m = int(sys.stdin.readline().strip())
    if m==0 or m==1 :
        print(2)
    else :    
        while (is_prime(m) == False) :
            m+=1
        print(m)