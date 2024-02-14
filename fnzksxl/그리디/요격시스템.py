def solution(targets):
    answer = 0
    ceil = 0
    
    sorted_targets = sorted(targets, key=lambda x: x[1])
    
    for s, e in sorted_targets:
        if s >= ceil:
            answer += 1
            ceil = e
    
    return answer
  