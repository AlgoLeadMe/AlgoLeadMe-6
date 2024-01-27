# 삼각형의 둘레 원칙 : 제일 긴 막대보다 작은 두 막대의 합이 더 길어야 한다.

line = sorted(map(int, input().split()))
print (line[0] + line[1] + min(line[0] + line[1]-1, line[2]))