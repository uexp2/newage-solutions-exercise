class TrainRoutes:
    def __init__(self, adjacency_list):
        self.locations = set()
        self.adjacency_list = adjacency_list

        # generate set of vertices
        for (start, end, dist) in adjacency_list:
            self.locations.add(start)
            self.locations.add(end)

    def dijkstra(self, start):
        verticies = self.locations.copy()

        dist = {}
        prev = {}
        for vertex in verticies:
            dist[vertex] = float("inf")
            prev[vertex] = None
        dist[start] = 0

        # While set of vertices is not empty
        while len(verticies) != 0:
            min_vert = self._minDist(dist, verticies)

            verticies.remove(min_vert)

            for (start, end, dist_adj) in self.adjacency_list:
                # only look at those that are adjacent to min_vert
                if start != min_vert:
                    continue
                temp = dist[min_vert] + dist_adj
                if temp < dist[end]:
                    dist[end] = temp
                    prev[end] = min_vert
        return (dist, prev)
    
    def getDistPath(self, path):
        '''
        @param: path should have hyphen separated points. e.g A-B-D-G
        '''
        list_path = path.split('-')
        
        for i in range(len(list_path)-1):
            start, end = list_path[i], list_path[i+1]
            
        return 0

    def _minDist(self, dict_distances, vertices):
        min_dist = float("inf")
        min_vert = None
        for vertex in vertices:
            if (dict_distances[vertex] < min_dist):
                min_dist = dict_distances[vertex]
                min_vert = vertex
        return min_vert

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


def getDistPath(path):
    pass


def getNumDiffPaths(start, end, min_stops, max_stops):
    pass


def findShortestPath(start, end):
    pass


def main():
    train_routes = TrainRoutes(generateAdjacencyList())
    print(train_routes.dijkstra('A'))

if __name__ == "__main__":
    main()
