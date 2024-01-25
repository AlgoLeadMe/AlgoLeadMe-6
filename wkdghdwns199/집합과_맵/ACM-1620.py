import sys
n,m = map(int, sys.stdin.readline().split())
pokemon = {}
for i in range(1,n+1):
    name = sys.stdin.readline().strip()
    pokemon[name] = i
    pokemon[str(i)] = name

for i in range (0,m) :
    question = sys.stdin.readline().strip()
    print(pokemon[question])