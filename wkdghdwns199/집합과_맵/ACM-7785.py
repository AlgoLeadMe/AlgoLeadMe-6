log = {}
for i in range(0, int(input())) :
    name, enterance = map(str,input().split())
    if enterance == 'enter':
        log[name] = 1
    else :
        del log[name]

for name in sorted(log.keys(), reverse=True) :
    print(name)

print(sorted(log.keys()))