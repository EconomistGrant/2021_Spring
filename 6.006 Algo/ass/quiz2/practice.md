# Q1
"levels":
"Edges from hot cities from the first copy go to the corresponsing vertices in the second copy, and so on"

# Q2
DFS only back edge
possible additional forward edges:
A - E, A - H, C - H, A - F, A - G, C - I, A - I

BFS
B: C, D 2
C: B, D 2
D: B, C, E, F 4
E: F, D, G, 3
F: D, E, G, H, I 5
G: E, F, H, I 4
H: F, G 2
I: F. G 2
2+2+4+3+5+4+2+2 / 2=12

BCD: 3
among EFG: 3
ED, FD 2
HF, IF, FH, IG 4

and HI as well

orginal tree: 8

# Q3
GREAT QUESTION
think smart instead of hard

# Q4
representation: a chain of vertices, how to connect vertices

# Q5


其实所有的问题基本都是how to duplicate nodes
从这个角度出发去思考
