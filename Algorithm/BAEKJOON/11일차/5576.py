import sys

sys.stdin = open("5576.txt")

W = []
K = []
for _ in range(10):
    W.append(int(input()))
for _ in range(10):
    K.append(int(input()))

W.sort(reverse = True) # 내림차순 정렬
K.sort(reverse = True) # 내림차순 정렬
W_score = 0
K_score = 0

for i in range(3):
    W_score += W[i]
    K_score += K[i]

print(W_score, K_score)