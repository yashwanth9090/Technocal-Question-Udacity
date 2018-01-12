parent = {}
rank = {}
def create_set(vertex):
    parent[vertex] = vertex
    rank[vertex] = 0

# search for the set to which the vertex belongs
def search(vertex):
    if parent[vertex] != vertex:
        parent[vertex] = search(parent[vertex])
    return parent[vertex]

# merge the sets represented by these two given root nodes
def union(vertex1, vertex2):
    root1 = search(vertex1)
    root2 = search(vertex2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]: rank[root2] += 1

# perform kruskal algorithm to find mst
def kruskal(vertices, edges):
    minimum_spanning_tree = set()
    for vertex in vertices:
        create_set(vertex)
    
    for edge in edges:
        wt, vertex1, vertex2 = edge
        if search(vertex1) != search(vertex2):
            union(vertex1, vertex2)
            minimum_spanning_tree.add(edge)
            
    return minimum_spanning_tree

def question3(G):
    
    # check if input is dictionary
    if type(G) != dict:
        return "Input is not a dictionary!"

    # check if graph has enough edges
    if len(G) < 2:
        return "Not enough edges!"
    
    nodes = G.keys()
    edge_list = set()
    
    # extract edges from the given input graph
    for node in nodes:
        # build edge tuples
        edges = G[node]
        for edge in edges: 
            start_node= node
            end_node, weight = edge
            if start_node > end_node:
                edge_list.add((weight,end_node,start_node))
            if start_node < end_node:
                edge_list.add((weight,start_node,end_node))
                
    # sort edges by increasing weights
    edge_list = sorted(list(edge_list))
    
    # perform Kruskal's algorithm
    output = kruskal(nodes, edge_list)
    
    # graph is converted to desired ouput
    output_graph = {}
    for node in output:
        weight,start_node,end_node = node
        
        if end_node < start_node:
            start_node = node[2]
            end_node = node[1]
            
        if start_node in output_graph:
            output_graph[start_node].append((end_node, weight))
        else:
            output_graph[start_node] = [(end_node, weight)]
            
    return output_graph


def test3():
    print "Test Case 1 - Edge Case"
    print "Input - not dictionary"
    print "Expected Output - Input is not a dictionary!"
    print "Output - "+str(question3(123))
    
    print "Test Case 2 - Edge Case"
    print "Input - not enogh edges"
    print "Expected Output - Not enough edges!"
    print "Output - "+str(question3({}))
    
    G = {'A': [('B', 1), ('C', 7)],
     'B': [('A', 1), ('C', 5), ('D', 3), ('E', 4)],
     'C': [('A', 7), ('B', 5), ('D', 6)],
     'D': [('B', 3), ('C', 6), ('E', 2)],
     'E': [('B', 4), ('D', 2)],
    }
    
    print "Test Case 3"
    print "Input - G"
    print "Expected Output - {'A': [('B', 1)], 'B': [('C', 5), ('D', 3)], 'D': [('E', 2)]}"
    print "Output - "+str(question3(G))
    
    G = {'A': [('B', 1), ('C', 1)],
     'B': [('A', 1), ('C', 1)],
     'C': [('A', 1), ('B', 1)],
    }
    
    print "Test Case 4"
    print "Input - G"
    print "Expected Output - {'A': [('C', 1), ('B', 1)]}"
    print "Output - "+str(question3(G))
test3()