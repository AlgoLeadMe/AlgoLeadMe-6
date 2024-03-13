import sys
input = sys.stdin.readline
N,M = map(int, input().split())
word_count = {}
for _ in range(N):
    word = input().rstrip()
    if len(word) >= M :
        if word in word_count :
            word_count[word][0] += 1
        else :
            word_count[word] = [1,len(word)]

print()
for key in word_count :
    print (key)

sorted_word_list = sorted(word_count, key=lambda key : (-word_count[key][0], -word_count[key][1], key))
print()
for word in sorted_word_list :
    print(word) 
