# Sorting I: the power of divide and conquer
Input: an key of elements with keys taht can be compared
output: array in sorted order

Binary search can search a sorted array in O(log(n)) time

# Brute Force: permutation sort
find all permutations...

# Insertion sort 
sort first k elements, when new comes, swap until it is in the right place(first k+1 sorted)
better than bubble sort
O(n**2), worst case reverse order

# Merge Sort
sort the left and right half seperately and then merge
T(n) = 2T(n/2) + t_merge(n) = 2T(n/2) + c*n
merge in O(n) in a single pass: take the smaller of the bottom two 
T(n) = cnlogn

# Peak Finding
Brute force: O(n) time, scan

1D Peak finding: find a peak in O(logn)
start with mid element, go to the upper hill -> you will always find a peak!

2D peak finidng: brute force takes O(mn) time

find the max of the mid row -> recurse on the uphill half
at-the-border row max will be higher than every element in just-over-the-border row
so at end of the day, if you only end up with one row -> the max will be higher than its upper and lower row

# Rec 3 Dynamic Array Sequence
amortized constant time, table doubling
Faster sets: sorted array, find logn, find max O(1)