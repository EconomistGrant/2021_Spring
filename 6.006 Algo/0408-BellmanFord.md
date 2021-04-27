Dijkstra: a negative edge, you never exploredm because you pop min
# Path Relaxation Lemma:
if we relax following the order of a true shortest path, then we found the true distance of the end node
proof: induction on path length

# Proposal of Bellman-Ford
On a graph with V vertices, s.p. has at most V - 1 edges
number the edges from 1 to E, relax them in order V-1 times!

# Negative Weight Cycles: no shortest path


# Bellmman Ford
O(VE)
Idea:
1) initialize distance estimates
2) relax every edge V - 1 times
Why:
Simple path use at most V - 1 edges

for k in range (V-1):
    for u in range(V):
        for v in adj[u]:
            try_to_relax(Adj, w, d, parent, u, v)

#if still relaxable, negative cycles
for u in range(V):
    for v in adj[u]:
        if d[v] > d[u] + w(u,v): raise Expeption("Negative cycle")

prove by induction: sp with number of edges

# Shortedt Path on DAGs
O(V+E)
1. topological sort
2. a path following the directed edge -> vertices on a shortest path must in topological order
   for v in topological order: relax all outgoing edges

correctness proven by path relaxation lemma

# Runtime
Djistra: O(VlogV + E), no negative weight
Bellman-Ford O(VE), no negative weight cycles

# Recitation
## Exercise: maximum total fun
1. Run B-F, find negative cycle

2. if no negative cycle: 
3 run of BF, one for each house, add up fun-ness scores for each intersections, choose most fun
the same runtime

## Exercise: k-limited
run B-F, stop relaxation after k iterations
runtime: 

