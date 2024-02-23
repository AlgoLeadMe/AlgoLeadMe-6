N = int(input())
order_list = list(map(int, input().split()))
order = 1
stack = []

for student in order_list :
    if student > order :
        stack.append(student)
    elif student == order :
        order+=1

while len(stack) !=0 :
    if len(stack) == 1 or stack[len(stack)-2] > stack[len(stack)-1] : 
        stack.pop()
    else : break

print('Nice') if len(stack)==0 else print('Sad')