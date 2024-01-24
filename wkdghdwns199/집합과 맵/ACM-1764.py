import sys
n,m = map(int, sys.stdin.readline().split())
listen = set()
hear = set()
for _ in range(n):
    listen.add(sys.stdin.readline().strip())
for _ in range(m):
    hear.add(sys.stdin.readline().strip())
answer = listen & hear
print(len(answer))
for name in sorted(answer) :
    sys.stdout.write(name + '\n')