import sys
sys.stdin = open("graph_input.txt", "r")
# 첫 # 줄에 # 테스트 # 케이스 # 개수
# T가 1≤T≤50
# 다음 줄부터 테스트 케이스의 첫 V와 E가
# 5≤V≤50, 4≤E≤1000
# # 테스트케이스의
# 둘째
# 줄부터
# E개의
# 줄에
# 걸쳐, 출발
# 도착
# 노드로
# 간선
# 정보가
# 주어진다.
#
# E개의
# 줄
# 이후에는
# 경로의
# 존재를
# 확인할
# 출발
# 노드
# S와
# 도착노드
# G가
# 주어진다.
T=int(input())

for t in range(1,T+1):
    ans=0
    V,E=map(int,input().split())
    graph=[[] for _ in range(V+1)]
    visit=[False for _ in range(V + 1)]

    for i in range(E):
        s,e=map(int,input().split())
        graph[s].append(e)
    start,end=map(int,input().split())
    stack = [start]
    while stack and visit[e] == 0:  # stack이 없거나 원하는 도착점까지 도달했는지 확인
        v = stack.pop()
        if not visit[v]:  # 방문하지 않는 정점만 확인
            visit[v] = True  # 방문했음을 표시
            for v2 in graph[v]:  # 정점에서 연결된 정점들을 순회
                if not visit[v2]:  # 방문하지 않은 정점을 방문
                    stack.append(v2)
    if visit[end]:
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')
    # print(ans)


