import sys 
from heapq import *
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    chapters = list(map(int, input().split()))
    time_list = []
    min_time=0
    for chapter in chapters :
        heappush(time_list, chapter)
    while len(time_list) > 1 :
        temp =0 
        temp += heappop(time_list) + heappop(time_list)
        heappush(time_list, temp)
        min_time += temp
    print(min_time)