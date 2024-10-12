#1 1
#2 1
#3 1
#4 0
#5 1
#6 1
#7 0
#8 0
#9 0
#10 0
import sys
sys.stdin = open("1219input.txt", "r")
#
#
#
#
#
# for i in range(10):
#     ans=0
#     b, c = map(int, input().split())
#     info=list(map(int,input().split()))
#     graph=[[] for _ in range(100)]
#     visi=[False for _ in range(100)]
#     end_node=False
#     for j in range(0,len(info),2):
#         # print(info[j],info[j+1])
#         if info[j+1] == 99:
#             end_node=info[j]
#         graph[info[j]].append(info[j + 1])
#     if end_node:
#         # print(graph)
#         stack=[0]
#         # print(end_node)
#         end=[]
#         while stack and not visi[99]:
#             node=stack.pop()
#             visi[node] = True
#             # print(node)
#             if node==end_node:
#                 ans=1
#                 break
#             for j in graph[node]:
#                 if visi[j]==False:
#                     stack.append(j)
#
#
#     print("#{} {}".format(b,ans))
for i in range(10):
    ans=0
    b, c = map(int, input().split())
    info=list(map(int,input().split()))
    visi=[False for _ in range(100)]
    graph=[[] for _ in range(100)]
    end_node=False
    for j in range(0,len(info),2):
        graph[info[j]].append(info[j+1])
        if info[j+1]==99:
            end_node=True
    stack=[0]
    if end_node:
        while stack:
            node=stack.pop()
            if node==99:
                ans=1
                break
            visi[node]=True
            for j in graph[node]:
                if visi[j] ==False:
                    stack.append(j)

    print("#{} {}".format(b, ans))
