import sys
sys.stdin = open("bfs_input.txt", "r")
for t in range(1, 1 + int(input())):
    N,M = map(int,input().split())
    gragh=[[0 for _ in range(N+2)] for _ in range(N+2 )]
    visit = [False for _ in range(N+1)]
    # for i in range(N+2):
    #     gragh[i][0]=1
    #     gragh[i][-1] = 1
    #     gragh[0][i]=1
    #     gragh[-1][i] = 1

        # print(i, gragh[i],gragh[i][0],gragh[0][i])

    for i in range(M):
        v1,v2=map(int,input().split())
        gragh[v1][v2] = 1
        gragh[v2][v1] = 1
        # print(gragh[i])
    for i in range(N + 2):
        print(i, gragh[i], gragh[i][0], gragh[0][i])
    stack=[1]
    while stack:
        node=stack.pop(0)
        print(node ,end =" ")
        visit[node]=True
        for i in range(1,N+1):
            if gragh[node][i]==1 and visit[i] ==False:
                stack.append(i)
                visit[i] = True


