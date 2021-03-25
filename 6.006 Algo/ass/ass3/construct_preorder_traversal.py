##################################################
##  Problem 3.5 Constructing Tree Traversals
##################################################
import sys

# DO NOT REMOVE THIS LINE
sys.setrecursionlimit(10000)

def _constructor(inorder,postorder,preorder,inorder_map,instart,inend,poststart,postend):
    global preorder_pos
    
    if inend - instart < 0:
        return 
    
    root = postorder[postend]
    preorder[preorder_pos] = root
    preorder_pos+=1
    
    root_index = inorder_map[root]    

    _constructor(inorder,postorder,preorder,inorder_map,instart,root_index - 1,poststart,poststart + (root_index - 1 - instart))
    _constructor(inorder,postorder,preorder,inorder_map,root_index + 1, inend, postend - inend + root_index, postend - 1)
    
    return preorder

def construct_preorder_traversal(inorder, postorder):
    """
    Args:
        inorder (list): the inorder traversal of the tree
        postorder (list): the postorder traversal of the tree

    Output:
        list: the preorder traversal of the tree.
    """
    global preorder_pos
    preorder_pos = 0
    inorder_map = {}
    
    for i in range(len(inorder)):
        inorder_map[inorder[i]] = i
    
    return _constructor(inorder,postorder,['a']*len(inorder),inorder_map,0,len(inorder)-1,0,len(inorder)-1)
