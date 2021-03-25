G = (V,E)vertices and edges

# undirected graph
V = {a,b,c,d}
E = {{a,b},{c,d},...}

# directed

# degree
number of nodes connected to x

outdegree & indegree

# Representation
1. Adjacency list
neighbors of each vertex a -> {b,c,...}
directed & undirected
2. Adjacency matrix
which pairs are adjacent

list vs. matrix
sparse graph: |E| = O(n): list more economical
Dense: adjacency matrix faster edge check

# Graph Notions
subgraph G`=(V`,E`)
path: a sequence of verices that adjacent vertices are adjacent
  simple: none of the vertices are equal
  from s0 to sk, length is k

connected graph: each pair is connected
connected component: maximal connected subgraph

distance: minimum length

# BFS
i = 0, mark unmarked neighbors i+1 of vertices marked i
i = i+1

theorem: upon termination, each vertex is marked with its distance from s

complexity for adjacenncy list: O(n+m)
BFS tree: spanning tree(remember the parent), subgraph of the original graph

what if not connected?
different connected components

# Recitation
<br>Strongly connected: any two is connected
