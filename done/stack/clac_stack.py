import sys


'''
      아래의 구문은 input.txt 를 read only 형식으로 연 후,
      앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
      여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
      아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.

      따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
      아래 구문을 사용하기 위해서는 import sys가 필요합니다.

      단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''
sys.stdin = open("stack.txt", "r")


# for t in range(1, 1 + int(input())):
T=int(input())
for t in range(1, T+1):
    N = int(input())
    inlst= input()
    print(N,len(inlst))
    lst=[]

    ans = ''
    # for i in inlst:
    #     if i == '(':
    #         lst.append(i)
    #     elif i == ')':
    #         while lst and lst[-1] != '(':
    #             print(lst.pop(),end=" ")
    #         lst.pop() # remove ( in stack
    #     elif i == '*' or i == '/':
    #         while lst and (lst[-1] == '*' or lst[-1] == '/'):
    #             print(lst.pop(),end=" ")
    #         lst.append(i)
    #     elif i == '+' or i == '-':
    #         while lst and lst[-1] != '(':
    #             print(lst.pop(),end=" ")
    #         lst.append(i)
    #     else:
    #         # ans += i
    #         print(i,end=" ")
    # while lst:
    #     print(lst.pop(),end=" ")
    # # print(ans)
    for i in inlst:
        if i == '(':
            lst.append(i)
        elif i == ')':
            while lst and lst[-1] != '(':
                ans += lst.pop()
            lst.pop()
        elif i == '*' or i == '/':
            while lst and (lst[-1] == '*' or lst[-1] == '/'):
                ans += lst.pop()
            lst.append(i)
        elif i == '+' or i == '-':
            while lst and lst[-1] != '(':
                ans += lst.pop()
            lst.append(i)
        else:
            ans += i
    while lst:
        ans += lst.pop()
    print(ans)

    for i in ans:
        if not i in ["+","*"]:
            lst.append(i)
        elif i is "+":
            a=int(lst.pop())
            b=int(a)+int(lst.pop())
            lst.append(str(b))
        elif i is "*":
            a=int(lst.pop())
            b=int(a)*int(lst.pop())
            lst.append(str(b))
    print(lst.pop())



