# Bounds in time
Upper bound: find an algo and analyze
Lower bound: holy grail!

# Decision tree
every leaf: possible algorithm output
there are n! permutations -> num of leaves 2^S > n! = Theta(sqrt(n) (n/e)^n) (Stirling's approximation)

S >= Theta(nlog(n))
# Counting sort
2 passes: how many of each value you have and then mive into place
stable sort: preserves the order of equal keys

Sorting cards: first by suit, and then by face
sort suit first->4 piles, then sort each suit

clever idea: sort cards by face value then by suit
- if two cards differ by suit: second pass sorts them?

# Radix sort ?
n numbers with d digits in base k?
for 0 <= i < d: (counting & stable) sort by ith digit      (from least significant digit)
O((n+k)d)

optimize efficiency: b bits, change in base 2^r 
-> b/r digits, O((n+2^r)(b/r)), take r=logn

Radix sort is better when: 
n is big and d is small