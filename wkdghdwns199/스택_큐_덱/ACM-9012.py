N = int(input())
for _ in range (N):
    stack=[]
    str = input()
    for p in str :
        if p=='(' : stack.append(p)
        else :
            if len(stack) > 0 :
                if stack[len(stack)-1] == ')' : stack.append(p)
                else : stack.pop()
            else :
                stack.append(p)
    if len(stack) == 0 : print('YES')
    else : print('NO')