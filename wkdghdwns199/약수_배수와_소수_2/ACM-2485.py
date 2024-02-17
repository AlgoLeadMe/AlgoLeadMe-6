import sys
import math
tree = [int(sys.stdin.readline().strip()) for _ in range(int(sys.stdin.readline().strip()))] 
treeSpace = list(map(lambda pair : pair[1]- pair[0], zip(tree, tree[1:])))
totalGcd = math.gcd(*treeSpace)
print(int(sum(list(map(lambda x : x/totalGcd-1,treeSpace)))))