"""
15684 사다리 조작

i번 세로선의 결과가 i가 나오도록 놓여져 있는 사다리에 추가해야하는 가로선 개수의 최솟값을 출력해야한다.
세로선 개수 N
가로선 개수 M
가로선을 놓을 수 있는 위치의 개수 H

알고리즘: 브루트 포스, BFS

1. 사다리 그리기
2. 테스트
3. 선그리기 반복 최대 3번
    1. 선그리기
    2. 테스트
        1. 선그리기
        2. 테스트
            1. 선그리기
            2. 테스트

(NxH)^3 = 300^3 = 270000
"""
import sys
read = sys.stdin.readline

n, m, h = map(int, read().strip().split())
ladder = [[0]*n for _ in range(h)]
line = []
for _ in range(m):
    a, b = map(int, read().strip().split())
    ladder[a-1][b-1] = 1
    ladder[a-1][b] = -1


def check_ladder(_ladder):
    for j in range(n):
        now_j = j
        for i in range(h):
            if _ladder[i][now_j] == 0:
                continue
            elif _ladder[i][now_j] == 1:
                now_j += 1
            else:
                now_j -= 1
        if now_j != j:
            return False
    return True


def check_empty(_ladder):
    empty_ = []
    for i in range(h):
        for j in range(n-1):
            if _ladder[i][j] == 0 and _ladder[i][j+1] == 0:
                empty_.append((i, j))
    return empty_


min_depth = 4


def add_ladder(depth):
    if depth == 4:
        return
    for i in range(h):
        for j in range(n-1):
            if ladder[i][j] == 0 and ladder[i][j+1] == 0:
                ladder[i][j] = 1
                ladder[i][j+1] = -1
                if check_ladder(ladder):
                    global min_depth
                    min_depth = min(depth, min_depth)
                    if min_depth == 1:
                        print(1)
                        sys.exit(0)
                else:
                    add_ladder(depth+1)
                ladder[i][j] = 0
                ladder[i][j+1] = 0


if check_ladder(ladder):
    print(0)
    sys.exit(0)

add_ladder(1)
if min_depth == 4:
    min_depth = -1
print(min_depth)
