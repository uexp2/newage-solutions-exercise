from graph import Graph
class TrainRoutes:
    def __init__(self, adjacency_list):
        self.routes_graph = Graph(adjacency_list)

    def shortestPath(self, source, target=None):
        if (source == target):
            # Shortest round-trip requested
            adjacency_dict = self.routes_graph.getAdjacencyDict()
            edge_weight_dict = self.routes_graph.getEdgeWeightDict()
            min_dist = float('inf')
            for adj_vert in adjacency_dict[source]:
                dist_adj_to_source = self.routes_graph.dijkstra(adj_vert, target)[0][target]
                total_dist = dist_adj_to_source + edge_weight_dict[(source, adj_vert)]
                if (total_dist < min_dist):
                    min_dist = total_dist
            return min_dist

        return self.routes_graph.dijkstra(source, target)[0][target]

    def distPath(self, path):
        return self.routes_graph.getDistPath(path)

    def numDiffPaths(self, start, end, min_stops=0, max_stops=None, max_dist=None):
        return self.routes_graph.getNumDiffPaths(start, end, min_stops, max_stops, max_dist)

'''
    Returns a list of strings.
'''

def readFile(filename):
    list_strings = []
    file = open(filename, 'r')
    for line in file:
        if (line[0] != '#'):
            list_strings.append(line.rstrip())
    file.close()
    return list_strings


def generateAdjacencyList(filename="train-graph-1.txt"):
    list_3tuple = []
    for string in readFile(filename):
        list_3tuple.append((string[0], string[1], float(string[2:])))
    return list_3tuple

def main():
    train_routes = TrainRoutes(generateAdjacencyList())
    print(train_routes.shortestPath('A', 'C'))
    print(train_routes.shortestPath('B', 'B'))
    print(train_routes.distPath("A-E-D"))
    print(train_routes.numDiffPaths('A', 'C', min_stops=4, max_stops=4))
    temp = train_routes.numDiffPaths('C', 'C', max_dist=30)
    print(list(map(lambda x: ("".join(x), train_routes.distPath(x)), temp)))

if __name__ == "__main__":
    main()
