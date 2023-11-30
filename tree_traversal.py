n=int(input())

tree_list=list()
for _ in range(n):
    tree_list.append(list(input().split()))

################### preset#############3333
# n=7

# tree_list=[['A', 'B', 'C'],
#            ['B', 'D', '.'],
#            ['C', 'E', 'F'],
#            ['E', '.', '.'],
#            ['F', '.', 'G'],
#            ['D', '.', '.'],
#            ['G', '.', '.']]



############ input test #######
# print(n)
# for i in range(n):
#     print(tree_list[i])
###############################



def find_index(tree_list, value):
    for i, row in enumerate(tree_list):
        if row[0]==value:
            return i
    print('찾는 value가 없습니다.')
    return None




def preorder(tree_list, traversal_list, present=0):
    traversal_list.append(tree_list[present][0])
    
    if tree_list[present][1] != '.':
        preorder(tree_list, traversal_list, find_index(tree_list, tree_list[present][1]))
    
    if tree_list[present][2] !='.':
        preorder(tree_list, traversal_list, find_index(tree_list, tree_list[present][2]))
    
    return traversal_list

def inorder(tree_list, traversal_list, present=0):
    if tree_list[present][1] != '.':
        inorder(tree_list, traversal_list, find_index(tree_list, tree_list[present][1]))

    traversal_list.append(tree_list[present][0])
    
    if tree_list[present][2] !='.':
        inorder(tree_list, traversal_list, find_index(tree_list, tree_list[present][2]))
    
    return traversal_list

def postorder(tree_list, traversal_list, present=0):
    if tree_list[present][1] != '.':
        postorder(tree_list, traversal_list, find_index(tree_list, tree_list[present][1]))

    if tree_list[present][2] !='.':
        postorder(tree_list, traversal_list, find_index(tree_list, tree_list[present][2]))

    traversal_list.append(tree_list[present][0])
    
    return traversal_list

traversal_list=list()
print(''.join(map(str, preorder(tree_list, traversal_list))))
traversal_list=list()
print(''.join(map(str, inorder(tree_list, traversal_list))))
traversal_list=list()
print(''.join(map(str, postorder(tree_list, traversal_list))))