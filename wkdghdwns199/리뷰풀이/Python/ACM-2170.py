import sys
input = sys.stdin.readline
N = int(input())
lines = [list(map(int, input().rstrip().split())) for _ in range(N)]
lines.sort()

length =0 
current_start = lines[0][0]
current_end = lines[0][1]
for start, end in lines[1:]:
    if start > current_end :
        print(start, current_end)
        length += (current_end - current_start)
        current_start = start
    current_end = max(current_end, end)
length += (current_end - current_start)
print(length)