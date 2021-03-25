import unittest
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

tests = (
    (
        (
            ["a"],
            ["a"]
        ),
        ["a"]
    ),
    (
        (
            ["a", "b", "c", "d", "e", "f", "g"], #in
            ["a", "c", "b", "e", "g", "f", "d"]  #post
        ),
        ["d", "b", "a", "c", "f", "e", "g"]
    ),
    (
        (
            ['d', 'b', 'a', 'e', 'c', 'f'],
            ['d', 'b', 'e', 'f', 'c', 'a']
        ),
        ['a', 'b', 'd', 'c', 'e', 'f']
    ),
    (
        (
            ['h', 'd', 'i', 'b', 'j', 'e', 'k', 'a', 'f', 'g', 'c'],
            ['h', 'i', 'd', 'j', 'k', 'e', 'b', 'g', 'f', 'c', 'a']
        ),
        ['a', 'b', 'd', 'h', 'i', 'e', 'j', 'k', 'c', 'f', 'g']
    ),
    (
        (
            ['h', 'd', 'b', 'a'],
            ['h', 'd', 'b', 'a']
        ),
        ['a', 'b', 'd', 'h']
    ),
    (
        (
            ['b', 'a', 'c', 'd', 'e'],
            ['b', 'e', 'd', 'c', 'a']
        ),
        ['a', 'b', 'c', 'd', 'e']
    ),
    (
        (
            ['b', 'c', 'd', 'e', 'f', 'a', 'j', 'i', 'h', 'g'],
            ['f', 'e', 'd', 'c', 'b', 'j', 'i', 'h', 'g', 'a']
        ),
        ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    ),
)


def check(test):
    args, staff_sol = test
    student_sol = construct_preorder_traversal(*args)
    return staff_sol == student_sol


class TestCases(unittest.TestCase):
    
    def test_01(self):
        self.assertTrue(check(tests[0]))
      
    def test_02(self):
        self.assertTrue(check(tests[1]))
    
    def test_03(self):
        self.assertTrue(check(tests[2]))

    def test_04(self):
        self.assertTrue(check(tests[3]))

    def test_05(self):
        self.assertTrue(check(tests[4]))

    def test_06(self):
        self.assertTrue(check(tests[5]))

    def test_07(self):
        self.assertTrue(check(tests[6]))
      
if __name__ == '__main__':
   res = unittest.main(verbosity = 3, exit = False)
