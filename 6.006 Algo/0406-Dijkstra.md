# Concepts:
Edge weights are non zero
path: sum of weights
shortest path: needless to be unique, assume directed

Single Source Shortest Path: given u, find a shortest path from u to every other vertex

Fact: if shortest path from u->v go thru a, then it contains a shortest path from u to a
intuition: intermediate vertices

keep track of 
d[v]: our best guess of distance from u to v
parent[v]: reconstruct the shortest path by finding parents

delta[u,a] + delta[a,v] >= delta[u,v] (delta: true shortest distance)

"relax"
whenever d[v] > d[a] +w(a,v) -> a shorter path d[v] = d[a]+w(a,v), parent[v] = a

# Framework:
keep on relaxing until we cant anymore

# Dijstra
S: verteces done
priority queue: vertices, key = distance

while pq:
    v1 = pq.pop_min; S.add(v1)
    for (v1,v2) in E:
    try to relax(v1,v2)
    pq.update_key(v2)

return d, parent

# Correctness
while loops runs V times; once a vertex added to S, never revisit
We prove d[v] and parent[v] must be correct when adding to S

contradiction: suppose not, v = the first violation vertex
shortest path: u -> x -> y -> v such that x is the last vertex in S and y is the first vertex not
d[x] is delta[x]: true shortest path

by fact: u -> x -> y is a shortest path, since its on the shortest path u -> v
delta[y] = delta[x] + w(x,y)

x is in S: we already tries to relax (x,y) already? d[y] is already <= d[x] + w(x,y) = delta[y]
do d[y] = delta[y]

y is out side of S: y still in pq, but we pop v at this point:
d[v] <= d[y]
d[v] <= d[y] = delta[y] <= delta[v] <= d[v]
every equality holds! delta[v] = d[v]

# Runtime:
Ti: time to insert into PQ
Te: time to extract min key from PQ
Td: time to decrease key for PQ
O(|V|Ti + |V|Te + |E|Td)

Dictionary for PQ: expected O(Ti),O(Td) = O(1), extract min O(|V|) => O(|V|^2 + |E|)
Good for dense graph

Binary min heap: insert, extract O(logV), decrease key: keep track of pointer, O(logn) => O((V+E)logV)
Good for sparse graph

Best Case: Fibonacci Heap O(VlogV + E)



Heap O((V+E)logV)
Fibonacci heap: O(VlogV + E)
