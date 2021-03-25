import unittest
from common import common

def common(lists):
    '''
    Input:  lists  | Array of arrays of positive integers
    Output: num_common  | number of numbers common to all arrays
    '''
    num_common = 0
    ##################
    # YOUR CODE HERE #
    ##################
    if len(lists) == 0:
        return 0
    
    common_set = {x for x in lists[0]}
    
    for i in range(1,len(lists)):
        cur = {x for x in lists[i]}
        new_common = set()
        for x in common_set:
            if x in cur:
                new_common.add(x)
        common_set = new_common
    
    return len(common_set)

tests = (
    (
        [[1,2,3]],
        3,
    ),
    (
        [[1,2,3], [2,3]],
        2,
    ),
    (
        [[1, 2], [3, 4]],
        0,
    ),
    (
        [],
        0,
    ),
    (
        [[]],
        0,
    ),
)


def check(test):
    A, staff_sol = test
    student_sol = common(A)
    return staff_sol == student_sol

class TestCases(unittest.TestCase):
    def test_01(self): self.assertTrue(check(tests[ 0]))
    def test_02(self): self.assertTrue(check(tests[ 1]))
    def test_03(self): self.assertTrue(check(tests[ 2]))
    def test_04(self): self.assertTrue(check(tests[ 3]))
    def test_05(self): self.assertTrue(check(tests[ 4]))
    
if __name__ == '__main__':
   res = unittest.main(verbosity = 3, exit = False)
