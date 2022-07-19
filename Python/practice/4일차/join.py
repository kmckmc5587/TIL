names = ','.join(['홍길동', '김철수'])
print(names)
# 홍길동, 김철수

# numbers = ' '.join([10, 20, 100])
numbers = ' '.join(map(str, [10, 20, 100]))
print(numbers)