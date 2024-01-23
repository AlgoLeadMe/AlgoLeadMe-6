string = input()
checkString = set()

for i in range(len(string)):
    for j in range(i, len(string)) :
        temp = string[i:j+1]
        checkString.add(temp)
print(len(checkString))

