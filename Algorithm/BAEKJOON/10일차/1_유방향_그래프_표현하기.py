import sys

sys.stdin = open("1_유방향_그래프_표현하기.txt")
from pprint import pprint # pprint 꼭 작성해야 graph 정답 답게 나옵니다.

N, M = map(int, input().split())
graph = [list([0] * 7) for i in range(7)]
list = [[] for i in range(N + 1)]

for j in range(M):
    u, v = map(int, input().split())
    graph[u][v] = 1
    list[u].append(v)
    # graph[v][u] = 1 -> 무방향과 유방향의 차이
    # list[v].append(u) -> 있고   없고
    # 단방향만 나타낸다. 양방향 X

pprint(graph)
print(list)