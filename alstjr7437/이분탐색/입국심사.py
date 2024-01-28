def solution(n, times):
    answer = 0
    # left = 제일 작은 시간, right = 제일 많은 시간
    left = min(times)
    right = max(times) * n
    while left <= right :
        mid = (right + left) // 2
        people = 0
        print(mid, people)
        for i in times:
            people += mid // i 
            print(people)
            if people >= n:
                break
        
        if people >= n:
            answer = mid
            right = mid - 1
        else :
            left = mid + 1
    return answer