import sys
sys.setrecursionlimit(10**9)
N = int(input())
tree = {i:[] for i in range(1, N+1)}


for _ in range(N-1) :
    a,b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

answer = [0 for _ in range(N+1)]

def dfs(current_node) :
    for node in tree[current_node] :
        if answer[node] == 0 :
            answer[node] = current_node
            dfs(node)

answer[1] = 1
dfs(1)

for index in range(2,N+1) :
    print(answer[index]) 