'''
Graph as:
- Vertex/node - contains name "key", data "payload"
- Edge - connects 2 vertices, symbolizing relationship
- Weight - cost to traverse vertex
- G = (V,E) (V=vertex, E=edges)
    ex.) V = {V0..V5}, E = {(V0, V1, 5), (V1, V2, 2) ...}
- Path - sequence of vertices connected by edges
- Cycle - path that starts/ends at same vertex 
'''

class Vertex(object):
    def __init__(self, key):
        self.key = key
        self.neighbors = {}
    
    def add_neighbor(self, neighbor, weight=0):
        self.neighbors[neighbor] = weight
    
    def __str__(self):
        return '{} neighbors: {}'.format(
            self.key,
            [x.key for x in self.neighbors]
        )
    
    def get_connections(self):
        return self.neighbors.keys()
    
    def get_weight(self, neighbor):
        return self.neighbors[neighbor]

class Graph(object):
    def __init__(self):
        self.vertices = {}
    
    def add_vertex(self, vertex):
        self.vertices[vertex.key] = vertex
    
    def get_vertex(self, key):
        try:
            return self.vertices[key]
        except KeyError:
            return None
    
    def __contains__(self, key):
        return key in self.vertices
    
    def add_edge(self, from_key, to_key, weight=0):
        if from_key not in self.vertices:
            self.add_vertex(Vertex(from_key))
        
        if to_key not in self.vertices:
            self.add_vertex(Vertex(to_key))
        self.vertices[from_key].add_neighbor(self.vertices[to_key], weight)

    def get_vertices(self):
        return self.vertices.keys()

    def __iter__(self):
        return iter(self.vertices.values())

g = Graph()
for i in range(5):
    g.add_vertex(Vertex(i))

print(g.vertices)

g.add_edge(0, 1, 5)
g.add_edge(0, 5, 2)
g.add_edge(1, 2, 4)
g.add_edge(2, 3, 9)
g.add_edge(3, 4, 7)
g.add_edge(3, 5, 3)
g.add_edge(4, 0, 1)
g.add_edge(5, 4, 8)
g.add_edge(5, 2, 1)

for v in g:
    for w in v.get_connections():
        print('{} -> {}'.format(v.key, w.key))

# Same graph, different representation
g2 = {
    0: {1:5, 5:2},
    1: {2: 4},
    2: {3: 9},
    3: {4:7, 5:3},
    4: {0: 1},
    5: {4: 8}
}