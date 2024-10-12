# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.

# 표준 입력 예제
'''
a = int(input())                        정수형 변수 1개 입력 받는 예제
b, c = map(int, input().split())        정수형 변수 2개 입력 받는 예제
d = float(input())                      실수형 변수 1개 입력 받는 예제
e, f, g = map(float, input().split())   실수형 변수 3개 입력 받는 예제
h = input()                             문자열 변수 1개 입력 받는 예제
'''

# 표준 출력 예제
'''
a, b = 6, 3
c, d, e = 1.0, 2.5, 3.4
f = "ABC"
print(a)                                정수형 변수 1개 출력하는 예제
print(b, end = " ")                     줄바꿈 하지 않고 정수형 변수와 공백을 출력하는 예제
print(c, d, e)                          실수형 변수 3개 출력하는 예제
print(f)                                문자열 1개 출력하는 예제
'''




'''
아래의 구문은 input.txt 를 read only 형식으로 연 후,
앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.
따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
아래 구문을 사용하기 위해서는 import sys가 필요합니다.
단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''
import sys
sys.stdin = open("miro_input_long.txt", "r")





# T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(10):
    ans=0
    t = int(input())
    arr = []
    arr_len = 100
    # arr.append([1]*(arr_len+1))
    # 1: wall 2:start 3: end
    visit = [[False for _ in range(arr_len)] for _ in range(arr_len)]
    stack_x=[1]
    stack_y= [1]
    for i in range(arr_len):
        row = input()
        arr.append(list(map(int, row)))
    while stack_x and stack_y:
        x=stack_x.pop() # pop(0) 도 결과같음
        y=stack_y.pop()
        visit[x][y]=True
        if arr[x][y] == 3:
            ans= 1
        else:
            if x-1 > 0 and (visit[x-1][y]==False and arr[x-1][y] != 1):
                stack_x.append(x - 1)
                stack_y.append(y)
            if x+1 < arr_len and (visit[x+1][y] == False and arr[x+1][y] != 1):
                stack_x.append(x + 1)
                stack_y.append(y)
            if y-1 > 0 and (visit[x][y-1] == False and arr[x][y-1] != 1):
                stack_x.append(x)
                stack_y.append(y - 1)
            if y+1 < arr_len and (visit[x][y+1] == False and arr[x][y+1] != 1):
                stack_x.append(x)
                stack_y.append(y + 1)

    print(f"#{t}", ans)