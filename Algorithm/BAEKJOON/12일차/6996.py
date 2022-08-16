import sys

sys.stdin = open("6996.txt")

T = int(input()) # 테스트케이스 개수
for i in range(T):
    A, B = map(str, input().split()) # A단어, B단어 입력

    # 리스트로 변환 후 sorted를 이용해서 오름차순으로 정렬
    x = sorted(list(A))
    y = sorted(list(B))

    # A에 속한 알파벳의 순서를 바꿔서 B를 만들 수 있다면 -> 애너그램
    if x == y: # 정렬한 결과가 같으면
        #s 사용해서 문자열 출력
        # %(A, B) 를 사용해서 A의 문자열, B의 문자열이 오게 설정
        print("%s & %s are anagrams." %(A, B)) # anagrams으로 출력
    else: # 같지 않다면
        print("%s & %s are NOT anagrams." %(A, B)) # NOT anagrams로 출력