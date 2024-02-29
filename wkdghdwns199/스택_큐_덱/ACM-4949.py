while True :
    str = input()
    if str == "." : break

    stack=[]
    for char in str :
        if char == '[' or char == '(':
            stack.append(char)
        elif char == ']' :
            if len(stack) !=0 :
                if stack[len(stack)-1] == '[' : stack.pop()
                else : stack.append(char)
            else :
                stack.append(char)
        elif char == ')' :
            if len(stack) !=0 :
                if stack[len(stack)-1] == '(' : stack.pop()
                else : stack.append(char)
            else :
                stack.append(char)
    if len(stack) == 0 : print('yes')
    else : print('no')