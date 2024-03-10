def solution(gems):
    answer = []
    head, tail = 0, 0
    gem_length = len(set(gems))
    gems_dict = {}
    gem_min = len(gems) + 1
    
    while head <= tail < len(gems):
        gems_dict[gems[tail]] = gems_dict.get(gems[tail], 0) + 1
        tail+=1
    
        if len(gems_dict) == gem_length:
            while head < tail:
                if gems_dict[gems[head]] > 1:
                    gems_dict[gems[head]] -= 1
                    head += 1
                
                elif gem_min > tail - head:
                    gem_min = tail - head
                    answer = [head+1, tail]
                    break
                    
                else:
                    break
        
    return answer