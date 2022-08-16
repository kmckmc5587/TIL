import sys

sys.stdin = open("0_무방향_그래프_표현하기.txt")
from pprint import pprint # pprint 꼭 작성해야 graph 정답 답게 나옵니다.

N, M = map(int, input().split()) # 정점의 개수 = N, 간선의 개수 = N
graph = [list([0] * (N + 1)) for i in range(N + 1)]
list = [[] for i in range(N + 1)]

for j in range(M):
    u, v = map(int, input().split()) # 간선의 양 끝 점 = u, v
    graph[u][v] = 1 # 인접행렬은 graph[][] 이렇게 정의
    graph[v][u] = 1 # u에서 v로 가는 간선이 존재하면 1, 존재하지 않다면 0 # 양방향
    list[u].append(v) # list[u] -> u번째 노드에 연결된 노드들을 원소로 갖는 리스트
    list[v].append(u) # 리스트도 마찬가지

pprint(graph)
print(list)