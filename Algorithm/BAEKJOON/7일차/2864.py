A, B = input().split() # str로 입력

min_num = int(A.replace('6', '5')) + int(B.replace('6', '5')) # replace 함수
max_num = int(A.replace('5', '6')) + int(B.replace('5', '6'))
print(min_num, max_num)