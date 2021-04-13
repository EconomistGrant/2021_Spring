
def find_start_times(constraints):
    """Find the start times that follows the provided constraints.

    Args:
        constraints(List[Tuple[str, str, int]]): A list of tuples
            `(a, b, t)` where `a` and `b` are strings that contain
            variable names such that `a - b <= t`.
    
    Returns:
        A python dictionary where keys are variables and values are
        their correct assignments.
        `None` if it is not possible.
    """

    # Your code here!
    MAX = 1e8
    vertices = set()
    distance = dict()
    adjacents = dict()
    for con in constraints:
        in_vertex = con[0]
        out_vertex = con[1]
        t = con[2]
        
        vertices.add(in_vertex)
        vertices.add(out_vertex)
        
        old_adjacents = adjacents.get(out_vertex,[])
        old_adjacents.append((in_vertex,t))
        adjacents[out_vertex] = old_adjacents
    
    distance[out_vertex] = 0
    
    for i in range(len(vertices) - 1):
        for out_vertex in vertices:
            out_adjacents = adjacents.get(out_vertex,[])
            for info in out_adjacents:
                in_vertex = info[0]
                t = info[1]
                
                old_in_distance = distance.get(in_vertex, MAX)
                out_distance = distance.get(out_vertex, MAX)
                distance[in_vertex] = min(old_in_distance,out_distance+t)
        
    for out_vertex in vertices:
        out_adjacents = adjacents.get(out_vertex,[])
        for info in out_adjacents:            
            in_vertex = info[0]
            t = info[1]
            old_in_distance = distance.get(in_vertex, MAX)
            out_distance = distance.get(out_vertex, MAX)
            if old_in_distance > out_distance + t: return None
    
    for vertex in vertices:
        if distance.get(vertex,None) is None: distance[vertex] = MAX
    return distance