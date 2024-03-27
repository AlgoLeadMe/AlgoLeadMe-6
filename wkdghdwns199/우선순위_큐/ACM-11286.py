import sys, heapq
input =sys.stdin.readline
min_heap = []
max_heap = []
N = int(input())
for _ in range(N):
    number = int(input())
    if (number > 0) :
        heapq.heappush(min_heap, number)
    elif (number < 0) :
        heapq.heappush(max_heap, -number)
    else :
        if min_heap :
            if max_heap :
                if min_heap[0] < max_heap[0] :
                    print(heapq.heappop(min_heap))
                else :
                    print(-heapq.heappop(max_heap))
            else :
                print(heapq.heappop(min_heap))
        elif max_heap :
            print(-heapq.heappop(max_heap))
        else :
            print(0)