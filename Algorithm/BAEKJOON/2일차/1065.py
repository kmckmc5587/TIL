X = int(input())
N = 0

for i in range(1, X + 1):
    X_list = list(map(int, str(i)))
    if i < 100:
        N += 1
    elif X_list[0] - X_list[1] == X_list[1] - X_list[2]:
        N += 1
print(N)