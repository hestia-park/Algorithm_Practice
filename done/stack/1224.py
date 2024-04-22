#1 672676
#2 1974171
#3 12654
#4 38756
#5 4035
#6 155304
#7 6964
#8 2819
#9 24711
#10 208785
import sys
sys.stdin = open("1224input.txt", "r")
icp={
    "(":3,
    "+":1,
    "-":1,
    "/": 2,
    "*": 2,
    ")":-1
}
isp={
    "(":0,
    "+":1,
    "-":1,
    "/": 2,
    "*": 2
}

def cal():
    global stack,cnt
    if node == "+":
        b = cnt.pop()
        a = cnt.pop()
        cnt.append(str(int(a) + int(b)))
    elif node == "*":
        b = cnt.pop()
        a = cnt.pop()
        cnt.append(str(int(a) * int(b)))
for ts in range(10):
    ans=0
    length=int(input())
    info=list(map(str,input()))
    stack=[]
    cnt=[]
    for i in info:
        if i in icp.keys():
            if i=="(":
                stack.append(i)
            elif i == ")":
                node = stack.pop()
                while node != "(":
                    cal()
                    node = stack.pop()
            else:
                c=stack[-1]
                if isp[c] <= icp[i]:
                    stack.append(i)
                else:
                    while isp[stack[-1]] > icp[i]:
                        node = stack.pop()
                        cal()
                    stack.append(i)
        else:
            cnt.append(i)

    print("#{} {}".format(ts+1, cnt.pop()))
