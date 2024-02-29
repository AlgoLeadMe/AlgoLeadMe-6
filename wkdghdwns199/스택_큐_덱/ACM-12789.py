N = int(input())
order_list = list(map(int, input().split()))
order = 1
stack = []

# 5 4 2 3 1

while order_list :
    if order_list[0] == order:
        order_list.pop(0)
        order+=1
    else :
        stack.append(order_list.pop(0))
    
    while stack :
        if stack[-1] == order:
            stack.pop()
            order +=1
        else :
            break
    

print('Nice') if len(stack)==0 else print('Sad')