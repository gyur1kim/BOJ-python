import sys
sys.stdin = open('1991.txt')


class Node():
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


def preorder(n):
    print(n.data, end='')
    if n.left != '.':
        preorder(nodeDict[n.left])
    if n.right != '.':
        preorder(nodeDict[n.right])


def inorder(n):
    if n.left != '.':
        inorder(nodeDict[n.left])
    print(n.data, end='')
    if n.right != '.':
        inorder(nodeDict[n.right])


def postorder(n):
    if n.left != '.':
        postorder(nodeDict[n.left])
    if n.right != '.':
        postorder(nodeDict[n.right])
    print(n.data, end='')


V = int(input())
nodeDict = {}
for _ in range(V):
    d, l, r = input().split()
    nodeDict[d] = Node(d, l, r)
preorder(nodeDict['A'])
print()
inorder(nodeDict['A'])
print()
postorder(nodeDict['A'])