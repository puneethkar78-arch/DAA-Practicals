from collections import defaultdict
import heapq

def prim_mst(vertices, edges):
    """
    Finds the Minimum Spanning Tree (MST) using Prim's Algorithm.
    
    :param vertices: List of all vertex identifiers (e.g., [0, 1, 2, 3])
    :param edges: List of tuples representing (u, v, weight)
    :return: A tuple containing (list of MST edges, total MST weight)
    """
    # 1. Build an adjacency list representation of the graph
    graph = defaultdict(list)
    for u, v, weight in edges:
        graph[u].append((weight, v))
        graph[v].append((weight, u))  # Graph must be undirected

    # 2. Pick an arbitrary starting vertex
    start_vertex = vertices[0]
    
    # Track visited vertices to avoid cycles
    visited = set()
    
    # Priority queue to pick the edge with the minimum weight.
    # Format: (weight, from_vertex, to_vertex)
    min_heap = []
    
    # Initialize the heap with edges outgoing from the starting vertex
    visited.add(start_vertex)
    for weight, to_vertex in graph[start_vertex]:
        heapq.heappush(min_heap, (weight, start_vertex, to_vertex))
        
    mst_edges = []
    total_weight = 0

    # Loop until the heap is empty or we have connected all vertices
    while min_heap and len(visited) < len(vertices):
        weight, frm, to = heapq.heappop(min_heap)
        
        # If the destination vertex is already in the MST, skip it to prevent cycles
        if to in visited:
            continue
            
        # Add the edge to our Minimum Spanning Tree
        visited.add(to)
        mst_edges.append((frm, to, weight))
        total_weight += weight
        
        # Add all valid outgoing edges from the newly visited vertex to the heap
        for next_weight, next_vertex in graph[to]:
            if next_vertex not in visited:
                heapq.heappush(min_heap, (next_weight, to, next_vertex))
                
    return mst_edges, total_weight

# --- Example Usage ---
if __name__ == "__main__":
    # Define a graph with 5 vertices (0 through 4)
    num_vertices = [0, 1, 2, 3, 4]
    
    # Format: (vertex_1, vertex_2, edge_weight)
    graph_edges = [
        (0, 1, 2),
        (0, 3, 6),
        (1, 2, 3),
        (1, 3, 8),
        (1, 4, 5),
        (2, 4, 7),
        (3, 4, 9)
    ]
    
    mst, total_cost = prim_mst(num_vertices, graph_edges)
    
    print("Edges in the Minimum Spanning Tree:")
    for u, v, w in mst:
        print(f"{u} -- {v} == Weight: {w}")
    print(f"\nTotal Weight of MST: {total_cost}")
