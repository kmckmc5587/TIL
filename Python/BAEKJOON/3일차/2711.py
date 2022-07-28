T = int(input())

for i in range(T):
    N, word = input().split()
    N = int(N)
    print(word[:N -1] + word[N:])