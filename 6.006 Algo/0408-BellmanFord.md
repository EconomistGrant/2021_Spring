Dijkstra: a negative edge, you never exploredm because you pop min



# Rec
Djistra: O(VlogV + E), no negative weight
Bellman-Ford O(VE), no negative weight cycles

# Bellmman Ford
Idea:
1) initialize distance estimates
2) relax every edge V - 1 times
Why:
Simple path use at most V - 1 edges

for k in range (V-1):
    for u in range(V):
        for v in adj[u]:
            try_to_relax(Adj, w, d, parent, u, v)

#if still relaxable:
for u in range(V):
    for v in adj[u]:
        if d[v] > d[u] + w(u,v): raise Expeption("Negative cycle")

prove by induction: sp with number of edges

## Exercise: maximum total fun
1. Run B-F, find negative cycle

2. if no negative cycle: 
3 run of BF, one for each house, add up fun-ness scores for each intersections, choose most fun
the same runtime

## Exercise: k-limited
run B-F, stop relaxation after k iterations
runtime: 