# DFS tree
categorize edges

# Topological Sort
if u -> v: TS(u) < TS(v)
point to higher priority

think reversely: if u -> v: TS(u) > TS(v)
## DFS backtrack numbering
when you back track: assign a number!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
= topological reverse sort
O(n+m)

proof: u -> v, dfs(v) finishes befores dfs(u)

## Strongly connected components
for any pair, you can find both way paths

condensation graph: DAG(directed accyclical graph) created by collapsing SCC

### low linking alg
in[u]: discovery time, DFS number
low[u]: minimal discovery time for a path starting at u

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
    
tto
there might be some node not explored: the "root" for example?
outter cycle: for each node u in G, if in[u] == 0, DFS


in == low: no back edge to lower value nodes

# Articulation point: disconnects graph
DFS tree: 
1. root is an articulation point <=> at least two children
two childrem -> articulation: no cross edge
articulation -> two children: 

2. nonroot vertex: an articulation point <=> 
v has a child s such that there is no back edge from s or any descendant of s to a ancestor of v

v.low = minimum of v's dicovery time and w's discovery time, where w back edge to v

1. apply part 3 getting v.low
2. compare v.low to v.d, if equals then articulation point
    
