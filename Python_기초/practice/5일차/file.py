# 'r' : read (읽기 전용)
# 'w' : write (쓰기 전용 - 덮어씀)
# 'a' : append (쓰는데 파일 있으면 이어서 씀)
with open('test.txt', 'w', encoding = 'utf-8') as f:
    f.write('Hello World!\n')
    for i in range(1, 7):
        f.write(f'{i} 번째!\n')