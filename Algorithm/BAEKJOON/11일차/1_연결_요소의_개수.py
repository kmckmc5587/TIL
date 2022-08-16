import sys

sys.stdin = open("1_연결_요소의_개수.txt")

N, M = map(int, input().split()) # 정점의 개수 = N, 간선의 개수 = M
adj = [[] for _ in range(N + 1)] # 최적화를 위해 인접 리스트(adj) 활용
visited = [0] * (N + 1) # 노드 탐색 유무
count = 0

for _ in range(M):
    u, v = map(int, input().split()) # 간선의 양 끝 점 = u, v
    adj[u].append(v)
    adj[v].append(u)

def dfs(u): # dfs 이용해서 푸는 문제
    visited[u] = 1
    for i in adj[u]:
        if not visited[i]: # 방문이 안 되었다는 것 -> 연결 요소가 아니라는 것
            dfs(i)
    
for j in range(1, N + 1): # 1번부터 N 번까지의 노드를 순회하면서 방문 여부 확인
    if not visited[j]:    # 방문이 안 되었다는 것 -> 연결 요소가 아니라는 것
        dfs(j)
        count += 1

print(count) # 모든 요소가 연결되어있다면 count의 값은 1로 출력