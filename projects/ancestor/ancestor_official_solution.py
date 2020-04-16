from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}  # This is our adjacency list

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph from v1 to v2
        """
        # Check if they exist
        # if v1 in self.vertices and v2 in self.vertices:
        if v1 in self.vertices:
            # Add the edge
            self.vertices[v1].add(v2)
        else:
            print(f"ERROR ADDING EDGE between {v1} and {v2} : Vertex not found")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            return None

    # def get_neighbors(self, vertex_id):
    #     """
    #     Get all neighbors (edges) of a vertex.
    #     """
    #     if vertex_id in self.vertices:
    #         return self.vertices[vertex_id]

    #     elif vertex_id :
    
    #     # for vertex_id in gg.vertices:
    # #     print(gg.vertices[vertex_id])
    
    #     print()

    #     else:
    #         return None
    
    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create a q and enqueue starting vertex
        qq = Queue()
        qq.enqueue([starting_vertex])
        # Create a set of traversed vertices
        visited = set()
        # eldest = []
        depth_counter = {} 
        starter = 0 
        # visited = []
        # While queue is not empty:
        while qq.size() > 0:
            # dequeue/pop the first vertex
            path = qq.dequeue()
            # if not visited
            # print(visited)
            starter += 1
            if path[-1] not in visited:
                # DO THE THING!!!!!!!
                # print(path[-1])
                depth_counter[starter] = path[-1]
                # mark as visited
                visited.add(path[-1])
                # visited.append(path[-1])
                # enqueue all neightbors
                
                if not self.get_neighbors(path[-1]):
                    
                    if starting_vertex == path[-1]:
                        return -1
                    else:
                        # print("eldest ancestor:",path[-1])
                        depth_counter[starter] = path[-1]
                        # print(depth_counter)
                        # eldest.append(path[-1])
                else:
                    # starter += 1
                    for next_vert in self.get_neighbors(path[-1]):  
                        new_path = list(path)
                        new_path.append(next_vert)
                        qq.enqueue(new_path)


        return depth_counter[starter]

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create a s and push starting vertex
        ss = Stack()
        ss.push([starting_vertex])
        # Create a set of traversed vertices
        visited = []
        eldest = [] 
        # While stack is not empty:
        while ss.size() > 0:
            # dequeue/pop the first vertex
            path = ss.pop()
            if path[-1] not in visited:
                # DO THE THING!!!!!!!
                # print(path[-1])
                # mark as visited
                visited.append(path[-1])
                print(visited)
                # enqueue all neightbors
                if not self.get_neighbors(path[-1]):
                    if starting_vertex == path[-1]:
                        return -1
                    else:
                        # print("eldest ancestor:",path[-1])
                        eldest.append(path[-1])

                for next_vert in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    # print(new_path)
                    new_path.append(next_vert)
                    ss.push(new_path)
                    
        return min(eldest)
            
# def get_neighbors_list(list_node):
#     list_neighbors = []
#     gg = Graph()
#     for node in list_node:
#         list_neighbors.append(gg.get_neighbors(node))
#     return list_neighbors
def earliest_ancestor(ancestors, starting_node):
    # hierarchy = {}
    # level = 0 
    gg = Graph()
    # list_neighbors = []
    for parent, child in ancestors:
        gg.add_vertex(parent)
        gg.add_vertex(child)
    for parent, child in ancestors:
        gg.add_edge(child,parent)
    
    # hierarchy[level] = [starting_node]
    # list_neighbors = gg.get_neighbors(starting_node)
    # while list_neighbors is not None:
    #     new_list = []
    #     print("---- ",hierarchy)
    #     level += 1 
    #     for node in list_neighbors:
    #         print("node ---- ",node)
    #         if (gg.get_neighbors(node) != set()):
    #             new_list.append(list(gg.get_neighbors(node)))
    #     hierarchy[level] = new_list
    #     list_neighbors = new_list
    # print("---- ",hierarchy)


    # print(gg.get_neighbors(2))
        # gg.get_neighbors(hierarchy[level])
        # ll = []
        # for next_vert in gg.get_neighbors(hierarchy[level]):
        #     ll.append(next_vert)
        #     hierarchy[level] = ll
        #     print(hierarchy)

    # else:
    #     if starting_vertex == gg.get_neighbors(hierarchy[level]):
    #                 return -1

    return gg.dft(starting_node)


if __name__ == "__main__":
    gg = Graph()
    ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
    # ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8)]
    print(earliest_ancestor(ancestors,9))
    # print(gg.vertices)
    # print(gg.dft(9))


    
    
    
