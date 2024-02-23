from collections import deque

def func(n, graph, degree):
    for i in range(1, n+1):
        q = deque()
        q.append(i)
        
        while q:
            node = q.popleft()
            
            for next_node in graph[node]:
                _before = len(degree[i])
                degree[i].add(next_node)
                
                if _before == len(degree[i]):
                    continue
                
                q.append(next_node)
                
def solution(n, results):
    answer = 0
    graph = [[] for _ in range(n+1)]
    reversed_graph = [[] for _ in range(n+1)]
    in_degree = [set() for _ in range(n+1)]
    out_degree = [set() for _ in range(n+1)]
    
    for win, defeat in results:
        graph[win].append(defeat)
        reversed_graph[defeat].append(win)
    
    func(n, graph, out_degree)
    func(n, reversed_graph, in_degree)
    
    
    for i in range(1, n+1):
        if len(out_degree[i])+len(in_degree[i]) == n-1:
            answer += 1
    
    return answer