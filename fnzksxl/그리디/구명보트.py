from collections import deque

def solution(people, limit):
    answer = 0
    heavy = 0
    people.sort()
    
    q = deque(people)
    while q:
        heavy = q.pop()
        if len(q) and heavy+q[0] <= limit:
            q.popleft()
            
        answer+=1
        
    return answer