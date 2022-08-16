import sys

sys.stdin = open("0_바이러스.txt")

N = int(input()) # 컴퓨터의 수
M = int(input()) # 연결된 컴퓨터 쌍의 수
adj = [[] for _ in range(N + 1)] # 인접리스트 adj 선언 및 입력받기
visited = [0] * (N + 1)	# 방문 처리 : 방문한 컴퓨터 수를 출력해야하므로 visited에 0 / 1로 처리

for _ in range(M): # 연결된 컴퓨터 쌍의 수만큼 반복
    x, y = map(int, input().split())		
    adj[x].append(y)
    adj[y].append(x)

def dfs(graph, v, visited): # dfs를 이용해서 푸는 문제
    visited[v] = 1
    for i in graph[v]:
        if visited[i] == 0:
            dfs(graph, i, visited)
    return True
dfs(adj, 1, visited)

print(sum(visited) - 1)	# 방문한 컴퓨터 개수 - 1번 컴퓨터