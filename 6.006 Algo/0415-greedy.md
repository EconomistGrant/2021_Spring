# Making change
find change for X with minimum number of coins

Always use the coin of greatest value, iterate

is optimal for nominal 1, 5, 10, 25, 100

optimal solution has at most 
4 * 1s
1 * 5s
2 * 5s and 10s
3 * 25s

Therefore, a solution with only 1's cannot be optimal for any amount > 4
...

So you have to use the larger amount first

# Huffman Algo
Compress all the works of Shakespere

32 symbols, 5 bit per symbol

frequency: q,e,t,s more common, give them shorter code than q or j
(variable length)

alphabet = {A,B,C,D,E,F,G,H}
T = ABGGHHHHHHAEEEEEEEEEEFCDD

variable length: how to we know new symbol starts?
prefix-free codes: no codeword is a predix of another
prefix: tree
A 110
B 1110
C 1111
D 0110
E 00 
F 0111
G 010 
H 10
![](https://cdn.mathpix.com/snip/images/XCWtlHHsFtvcj_ILAM-Mo7lnAmjaPO0sYH6V5Z58hhk.original.fullsize.png)

## Huffman codes
f(x): frequency of letter x
c_x: code for letter x
d(c): length of code c

goal: min sum f(x)*d(c_x)

observations:
1. optimal tree is full
2. you cannot have 2 letters x and y such that f(x) > f(y), but d(c_x) > d(c_y)
o/w you can exchange x and y

# Rec
## optimal substructure property
any optimal solution to given problem
includes optimal solutions to all of its subproblems
## Greedy Choice Property
A globally optimal solution can be achieved by making locally optimal (greedy) choice at each step


## Example: unit interval covering
observation: there is an optimal solution when the left most interval starts at x1!
add interval [x1,x1+1], removes points it covers and repeat

## Example: drive to NY
observation: always want to go the furthest gas station
 
## Example
precious metals
weight wi and total value vi
maximum W

best value per unit weight, take as much as possible, see if you have extra room
