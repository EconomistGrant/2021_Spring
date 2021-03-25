Priority Queue
Heap
Heapsort

# Prioroty Queue
insert(S,x)
max(S)
delete_max(S)
![](https://cdn.mathpix.com/snip/images/qaF9KeQKYq7GONyijEdoua7hauomFZTCpfbpdnYi0o4.original.fullsize.png)

# Heap
a group of things placed, thrown, or lying one on other

max heap: key of a node is >= the keys of its children

parent(i) = i/2
left(i) = 2i
right(i) = 2i+1

in process without pointers: space efficient!
## Heap operations
build_max_heap: produce a max-heap from an unordered array
max_heapify:    correct a single violation in a subtree at its root

> max_heapify\
assume left(i) and right(i) are max-heaps\
A[i] violates the max-heap property: step down A, bring up A[i]'s largest child\
costs logn

>Build_Max_Heap\
work on first half nodes, do max_heapify\
O(nlogn)? level k: O(k), summation, its actually O(n)

>Heap_sort\
build max heap in O(n)\

find maximum element\
swap A[n] and A[1]\
discard node n from heap\
max_heapify the root(Ologn)

operation O(nlogn)

```python
def f(a:int)

```