#1 SOFTWARE
#2 COMPUTER_SCIENCE_AND_ENGINEERING
#3 SOFWARE_ALGORITHM_AND_DATA_STRUCT
#4 DEPTH_FIRST_SEARCH_AND_BREATH_FIRST_SEARCH
#5 WELCOME_TO_ALGORITHM_PROBLEM_SOLVING
#6 ARRAY_STRING_STACK_QUEUE_TREE_GRAPH
#7 HE_WHO_WOULD_HAVE_THE_KERNEL_MUST_CRACK_THE_SHELL
#8 THE_PRESENT_IS_THE_PRESENT_MOMENT
#9 IN_ORDER_PRE_ORDER_POST_ORDER_TRACE
#10 TECHNOLOGY_TRAINING_INSTITUTE
import sys
sys.stdin = open("1231input.txt", "r")
stack=[]
def inorder(v):
    global graph
    if graph[v][1] != False:
        inorder(graph[v][1])
    if graph[v][0] != "":
        print(graph[v][0],end="")
    if graph[v][2] != False:
        inorder(graph[v][2])


for t in range(10):
    print("#{} ".format(t+1), end="")
    node_nums=int(input())
    graph=[['',False,False] for i in range(node_nums+1)]
    for i in range(1,node_nums+1):
        info=list(map(str,input().split()))

        if len(info)==4:
            graph[int(info[0])]=[info[1],int(info[2]),int(info[3])]
        if len(info) == 3:
                graph[int(info[0])] = [info[1], int(info[2]), False]
        if len(info)==2:
            graph[int(info[0])] = [info[1], False,False]
    inorder(1)
    print("\n")
    # print(stack)
    # print("\n")
