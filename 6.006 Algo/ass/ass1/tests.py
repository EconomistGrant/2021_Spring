import unittest

def find_first_missing_element(arr, d):
    '''
    Inputs: 
        arr        (list(int)) | List of sorted, unique positive integer order id's
        d          (int)       | Positive integer of smallest possible value in arr
    Output: 
        -          (int)       | The smallest integer greater than or equal to d that's not present in arr
    '''
    n = len(arr)
    j = int(n/2)
    lb = 0
    rb = n - 1
    
    if n == 0 or arr[0] != d:
        return d
    if n == 1:
        return d+1

    
    while True:
        # j being the last continous index
        print(j)
        if rb - lb == 1:
            break
        elif arr[j] > j+d:
            #move left
            rb = j    
            j = int((lb + j)/2)
        else: 
            #arr[j] == j+d:
            #move right
            lb = j
            j = int((rb+j)/2)
        
    if arr[j] > j+d:
        return j+d
    if arr[j] == j+d:
        if arr[j+1] > j+d+1:
            return j+d+1
        else:
            return j+d+2
    
        



find_first_missing_element([1,3,4], 1)

tests = (
    (
        [1, 3, 4],
        1,
        2,
    ),
    (
        [1, 2, 3, 4, 5, 6],
        1,
        7,
    ),
    (
        [], 
        3029319,
        3029319
    ),
    (
        [1, 2, 3, 4, 5, 6, 7, 10, 11],
        1,
        8,
    ),
    (
        [3],
        3,
        4
    ), 
    (
        [2, 3, 4, 5],
        1,
        1,
    ),
)

def check(test):
    arr, d, staff_sol = test
    student_sol = find_first_missing_element(arr, d)
    return staff_sol == student_sol

class TestCases(unittest.TestCase):
    def test_01(self): self.assertTrue(check(tests[ 0]))
    def test_02(self): self.assertTrue(check(tests[ 1]))
    def test_03(self): self.assertTrue(check(tests[ 2]))
    def test_04(self): self.assertTrue(check(tests[ 3]))
    def test_05(self): self.assertTrue(check(tests[ 4]))
    


if __name__ == '__main__':
   res = unittest.main(verbosity = 3, exit = False)
