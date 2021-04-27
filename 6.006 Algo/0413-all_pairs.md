Previously: Single Source Shortest Paths
Now: all-pairs shortest paths
APSP

output: 
distanc[u,v]
parent[u,v] parent of v on s.p. from u

output size is O(v^2)

# Nonnegative weights
naive idea: run dijstra from each vertex
O(V^2logV + VE), O(V^3) for dense graph and O(v^2logv) for sparse

# Negative weights
O(V^2E), dense O(V^4) - terrible

# Reweighting
a path is a shortest path in G iff it is one in G' (in the same traversal order)
G' should have nonnegative weights

Naive: add constant to all weights so taht they are nonnegative

h: V -> R, function "potential"
w'(u,v) = w(u,v) + h(u) - h(v)

claim: G' is a reweighting of G regardless of h
stronger claim: any path from uo to uk:
$\ell_{G'}(p)=\ell_{G}(p)+h\left(u_{0}\right)-h\left(u_{k}\right)$

so that every path from G to G' add the same constant!

proof of stronger claim: algebra


## find potential such that new weigths nonnegative
Idea: pick an arbitrary source vertex x, compute distances with SSSP, and reweight

what about not reachable? delta(v) = infinity

add a new SUPERNDOE: directied weight-0 edges from s to all other vertices
and start from s, run BFS, weights <= 0



# Jhonson Algorithm
O(V^2logV + VE)