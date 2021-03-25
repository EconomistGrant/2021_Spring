##################################################
##  Problem 4.4. Find order
##################################################

# Given a list of positive integers and the starting integer d, return x such that x is the smallest value greater than
# or equal to d that's not present in the list
def find_first_missing_element(arr, d):
    n = len(arr)
    j = int(n/2)
    lb = 0
    rb = n - 1
    
    if n == 0 or arr[0] != d:
        return d
    if n == 1:
        if arr[0] == d:
            return d+1
        else:
            return d
    
    while rb - lb > 1:
        if arr[j] > j+d:
            rb = j    
            j = int((lb + j)/2)
        else: 
            lb = j
            j = int((rb+j)/2)
        
    if arr[j] > j+d:
        return j+d
    if arr[j] == j+d:
        if arr[j+1] > j+d+1:
            return j+d+1
        else:
            return j+d+2