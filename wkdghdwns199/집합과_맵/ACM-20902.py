import sys
input = sys.stdin.readline
N,M = map(int, input().split())
word_count = {}
for _ in range(N):
    word = input().rstrip()
    if len(word) >= M :
        if word in word_count :
            word_count[word] += 1
        else :
            word_count[word] = 1

# print(word_count.items())
sorted_word_list = sorted(word_count.items(), key=lambda word_info : (-word_info[1], -len(word_info[0]), word_info[0]))
# print()
for word in sorted_word_list :
    print(word[0]) 
