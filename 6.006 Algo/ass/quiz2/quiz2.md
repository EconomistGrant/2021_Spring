Topics:
Heap, BFS, DFS, Dijstra, BF

# Heap
max_heapify: assume left and right trees are max-heaps
(heapify-down: exchange with largest child if necessary, O(logn))

build: for i = n/2 down to 1: max heapify, O(n)

heap-sort: swap to the end, discard, heapify-down from top

# BFS
mark **unmarked** neighbors with i+1 for *vertices marked with i*
BFS tree

# DFS
node type: undiscovered, unfinished, finished
to undiscovered: back edge
to finished: cross(earlier visited) or forward(later visited)

complexity: count per edge/per node operations

Intervals

# DFS application
Topologist Sort: right before backtracking/finishing a node, mark
strongly connected component

Tarjan

at a COA (node u):
    consider a adjacent node v
    if not explored:
        DFS(v)
        low[u] =  min (low[u], low[v])
    elif explored and in_stack(a back edge):
        low = min (low, in[v])
    else: dont no nothing *cross edge/forward edge*
    //
    finished explore COA:
    if in = low: a SCC is done, collect nodes in in_stack and label them

# Dijkstra
while pq:
    v1 = pq.pop_min; vertex_done.add(v1)
    for (v1,v2) in E:
        try to relax(v1,v2)
    pq.update_key(v2)

return d, parent

Runtime Analysis:
consider insert into PQ(V times), remove min from PQ(V times), and update key in PQ(E times)

Correctness:
consider the first vertex v add to vertex_done that has the wrong distance
consider the first vertex y on v's shortest path that does not have correct distance
y is on pq, but we poped v at this time, so d[y] = delta[y]

d[v] <= d[y] (by pq pop rule)
= delta[y] <= delta[v]

# BellBellman Ford
for k in range (V-1):
    for u in range(V):
        for v in adj[u]:
            try_to_relax(Adj, w, d, parent, u, v)

#if still relaxable, negative cycles
for u in range(V):
    for v in adj[u]:
        if d[v] > d[u] + w(u,v): raise Expeption("Negative cycle")

DAG: one inner iteration with the order of topological sort (for u in range(V))



# Recitation: R09 - R15
## R09
build heap O(n) proof
convert max heap to min heap: run build again, O(n)
## R10
BFS两道exercise蛮有意思的 相当于是把node复制 每一个node表示“层数/到这个node之前经过了几个node”
## R11
quiz 1 复习
## R12
DFS cross edge proof/no forward cross edge in undirected graph
## R13
DFS applications
articulation point: the definition of low

Let v.low be the minimum of v’s discovery time and w’s discovery time where w is such that(u, w)is a back edge for some descendant u of v
## R14 
Dijkstra
exercise 1: a good reference for representation!
exercise 2: great question
## R15
Bellman Ford
proof of BF: lemma, at the end of i round, correct distance for any vertex that has a shortest path which traverse at most i edges

## R18 
disjoint dimensions

# Psets 5 - 7
pset 5-4: create in-between nodes "a-edge directed chain of edges" 
pset 6-3
pset 7-2-2: good proof

# night before exam
Shortest Path: 
点到点：BFS
点到面：Dijstra，BF

DAG: topological sort relaxation?

特别注意：initialization value

两种常见的复制vertex思路：
1. different levels 或者是第多少次造访，practice Q1是经典例子。如果原先两个node相连，每一level的vertex按照原先相连的点连接到下一个level的vertex。
2. chain of edges 用一系列vertices来表示一个点，这一系列vertices内部相连，并且头尾的vertex与外部相连。practice Q4是经典例子，Q5是advanced 例子。
