##################################################
##  Problem 1. common
##################################################

# Given an array of lists of distinct numbers, 
# return the number of numbers common to all lists

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
    
    if len(lists) == 1:
        return len(common_set)
    
    for i in range(1,len(lists)):
        cur = {x for x in lists[i]}
        new_common = set()
        for x in common_set:
            if x in cur:
                new_common.add(x)
        common_set = new_common
    
    return len(common_set)