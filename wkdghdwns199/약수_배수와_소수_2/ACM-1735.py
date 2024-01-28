import sys
import math
a1,b1 = map(int, sys.stdin.readline().strip().split())
a2,b2 = map(int, sys.stdin.readline().strip().split())

lcm = math.lcm(b1,b2)
gcd = math.gcd((int(lcm/b1) * a1) + (int(lcm/b2) * a2), lcm) 
print(int(((int(lcm/b1) * a1) + (int(lcm/b2) * a2)) / gcd), int(lcm/gcd))
