chess = [1, 1, 2, 2, 2, 8]
N = list(map(int, input().split()))

for i in range(6): # 완전체 체스에서 예제 입력을 빼야한다.(필요하거나 많은 말 결과가 나온다.)
    print(chess[i] - N[i], end = ' ')