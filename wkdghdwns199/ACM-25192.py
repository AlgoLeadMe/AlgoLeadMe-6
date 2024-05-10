import sys
input = sys.stdin.readline
N = int(input())
emoji_using_users = set()
time_for_emoji_use = False
emoji_use_count = 0
for _ in range(N):
    chat_string = input().rstrip()
    if chat_string == 'ENTER' :
        if time_for_emoji_use :
            emoji_use_count += len(emoji_using_users)
        else :
            time_for_emoji_use = True
        emoji_using_users = set()
    else :
        emoji_using_users.add(chat_string)

emoji_use_count+=len(emoji_using_users)
print(emoji_use_count)