N = int(input())
paper = list(map(int, input().split()))
pop_check = [0 for _ in range(N+1)]
pop_check[0], pop_check[1] = 1,1
queue = [1]


while len(queue) != N :
    # print (queue[len(queue)-1], paper[queue[len(queue)-1]-1])
    cnt = queue[len(queue)-1] + paper[queue[len(queue)-1]-1]
    if cnt <= 0 : 
        cnt =  (queue[len(queue)-1] - paper[queue[len(queue)-1]-1]) - N
    elif cnt > N :
        cnt = (queue[len(queue)-1] + paper[queue[len(queue)-1]-1]) - N
    # print(cnt)

    while pop_check[cnt] == 1 :
        if paper[queue[len(queue)-1]-1] > 0 : 
            cnt+=1
            if (cnt > N) : cnt = 1
        else : 
            cnt-=1
            if (cnt == 0) : cnt = N
        # print('!', cnt)
    
    pop_check[cnt] = 1
    queue.append(cnt)


for balloon in queue :
    print(balloon, end=' ')
