import sys

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

input = sys.stdin.readline


def whole_year():
    def push_trees(tree):
        if not (age + 1) % 5:
            for d in range(8):
                nx = i + dx[d]
                ny = j + dy[d]
                if nx >= 0 and nx < N and ny >= 0 and ny < N:
                    new_tree.append((nx, ny, tree))

    new_tree = []
    for i in range(N):
        for j in range(N):
            if trees[i][j]:  # 빈 딕셔너리면 그냥 통과
                dead_trees = 0
                alive = {}
                OKAY = True  # 토양이 나무들을 성장시킬 수 있는지 없는지 확인하기 위한 플래그
                for age in sorted(trees[i][j]):  # 어린 나무부터 확인하기 위해 딕셔너리 정렬
                    if OKAY:
                        if age * trees[i][j][age] > bat[i][j]:
                            survive = bat[i][j] // age
                            if survive:
                                bat[i][j] -= survive * age
                                alive[age+1] = survive
                                push_trees(survive)
                            dead_trees += (trees[i][j][age] - survive) * (age // 2)
                            OKAY = False
                        else:
                            bat[i][j] -= age * trees[i][j][age]
                            alive[age+1] = trees[i][j][age]
                            push_trees(trees[i][j][age])
                    else:
                        dead_trees += trees[i][j][age] * (age // 2)

                bat[i][j] += dead_trees
                trees[i][j] = alive

            bat[i][j] += yang[i][j]

    for x, y, tree in new_tree:
        if 1 in trees[x][y].keys():
            trees[x][y][1] += tree
        else:
            trees[x][y][1] = tree
        # trees[x][y][1] = trees[x][y].get(1, 0) + tree


N, M, K = map(int, input().split())

answer = 0
yang = [list(map(int, input().split())) for _ in range(N)]
bat = [[5]*N for _ in range(N)]
trees = [[{} for _ in range(N)] for _ in range(N)]

for _ in range(M):
    x, y, z = map(int, input().split())
    trees[x-1][y-1][z] = 1


for _ in range(K):
    whole_year()

for i in range(N):
    for j in range(N):
        answer += sum(trees[i][j].values())

print(answer)
