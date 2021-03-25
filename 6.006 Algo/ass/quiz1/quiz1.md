P1:
(a) worst O(n), expected O(n)
(b) worst O(n+k), expeccted O(n+k)

P2:
sorted array rotated
find the "decreasing" position
```python
def find(X, start, end):
    middle = (start+end)/2
    if X[start] > X[start-1]:
        return start
    elif len(X) == 1: return 0
    else return find(X,start, middle) + find(X,middle+1,end)
```

T(n) = T(n/2) + 1
T(n) = logn

P3:
counting sort O(n)
merge sort O(nlogn)
insertion sort O(n)
radix sort: make sure the "keys" are bounded in some way! O(nC)

P4:
consider parent: if its left child, do nothing
if its right child, index += parent.left.size+1

P6:
each index: n^2 total d*n^2
stable sort

P7:
Shortest Path to leaf
```python
def shortest_path(node):
    if not x.left and not x.right: return 0
    elif x.left and x.right return 1 + min(shortest_path(x.left),shortest_path(x.right))
    elif x.left return 1 + shortest_path(x.left)
    else return 1+shortest_path(x.right)
```

P8:
expected chain length