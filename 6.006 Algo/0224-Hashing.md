# Direct Access Array
j th array: check if j is in the array in the array
Check, insert, delete in O(1) time
super large array

# Hash function
maps elements in the universe U to numbers from }0...m-1}
Initialize: allocate an array T of size m: O(m) time

Insert: put x in T[h(x)], O(1)
Find(x): check if x in T[h(x)], O(1)
delete O(1)

# Collision
two x have the same h(x)
Any hash functions will have collisions

## Simple Uniform Hashing Assumption
each key x maps to a uniformly random h(x) in 0,..m1, independent of other keys
load factor = #elements/table size

even if alpha is small, still have collisions: birthday paradox

# Chaining
used a l3inked list/bucket
average # of element per bucket is alpha
insert/find/delete: $\theta(1+\alpha)$ time on average

worst case: hash to the same value
insert takes O(1)
find/delete takes O(n)

# Choosing a hash function
Prime division hash (often good enough) h(x) = x (mod p)
Any fixed simple hash can be attacked

# Open Addressing
if T[(h(x))] is full, probe again at a different location until finding an empty slot
need a probe sequence h(x,i)

deletions are tricky, put a flag

## Linear Probing
h(x,i) = h(x) + i mod m
essentially go to next value

## Double Hashing
h(x,i) = h1(x) + i * h2(x) mod m
pros: more randomness, harder to attack

Table filled up: chaining works, double hashing stuck (double the table to solve, resizing slow)

# Worst Case/average/amortized
amortized: sequece of many hash table operations

efficient data structures R4, cryptography(messeage authentication)
searching(pset2)

# Recitation
SUHA: a random key will be equally likely to hash to any of the m buckets
average case performance O(1+alpha)

## Open Addressing vs. Chaining
chaining: + never full - difficult to work with long chains
open addressing: delete takes extra step; large alpha really slow

## find duplicated in unsorted array
brute froce: pick two from array
