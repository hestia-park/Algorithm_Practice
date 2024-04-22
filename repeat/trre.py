import sys
import os
from collections import namedtuple

sys.stdin = open("tree_input.txt", "r")

N=int(input())
tree={}
class Node(object):
    def __init__(self, item,l,r):
        self.item = item
        self.left = l
        self.right = r
for i in range(N):
    me,l,r=map(str,input().split())
    tree[me]=(l,r)
print(tree)

def preorder(tree,node):
    # print(node,tree[node])
    if tree[node] != ".":
        print(node, end=" ")
        if tree[node][0]!='.':
            preorder(tree,tree[node][0])
        if tree[node][1]!='.':
            preorder(tree,tree[node][1])

def inorder(tree,node):
    # print(node,tree[node])
    if tree[node] != ".":
        if tree[node][0]!='.':
            inorder(tree,tree[node][0])
        print(node, end=" ")
    if tree[node][1]!='.':
        inorder(tree,tree[node][1])



def postorder(tree,node):
    # print(node,tree[node])
    if tree[node] != ".":
        if tree[node][0] != '.':
            postorder(tree, tree[node][0])
        if tree[node][1] != '.':
            postorder(tree, tree[node][1])
        print(node, end=" ")


preorder(tree,'A')
print("\n")
inorder(tree,'A')
print("\n")
postorder(tree,'A')