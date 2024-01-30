import sys
import math
t = int(sys.stdin.readline().strip())
while (t > 0) :
    t-=1
    n,m = map(int, sys.stdin.readline().strip().split())
    print(math.lcm(n,m))
