from train_route import TrainRoutes
from simple_util import generateAdjacencyList

networks_directory = "./route-networks"


def testComplextRoute():
    adjacency_list = generateAdjacencyList(
        networks_directory + "/network-1.txt")
    train_routes = TrainRoutes(adjacency_list)

    all_pass = []

    # Distance of path
    expect = 9
    ret = train_routes.distPath("A-B-C")
    all_pass.append(expect == ret)

    expect = 5
    ret = train_routes.distPath("A-D")
    all_pass.append(expect == ret)

    expect = 13
    ret = train_routes.distPath("A-D-C")
    all_pass.append(expect == ret)

    expect = 22
    ret = train_routes.distPath("A-E-B-C-D")
    all_pass.append(expect == ret)

    expect = "NO SUCH ROUTE"
    ret = train_routes.distPath("A-E-D")
    all_pass.append(expect == ret)

    # All paths max_stops
    expect = 2
    ret = train_routes.numDiffPaths('C', 'C', max_stops=3)
    all_pass.append(expect == ret)

    expect = 3
    ret = train_routes.numDiffPaths('A', 'C', min_stops=4, max_stops=4)
    all_pass.append(expect == ret)

    # Shortest path
    expect = 9
    ret = train_routes.shortestPath('A', 'C')
    all_pass.append(expect == ret)

    expect = 9
    ret = train_routes.shortestPath('B', 'B')
    all_pass.append(expect == ret)

    # All paths max_dist
    expect = 7
    ret = train_routes.numDiffPaths('C', 'C', max_dist=30)
    all_pass.append(expect == ret)

    return all_pass


def testDisconnectedNetwork():
    adjacency_list = generateAdjacencyList(
        networks_directory + "/disconnected-train-network.txt")
    train_routes = TrainRoutes(adjacency_list)

    all_pass = []

    # Distance of path
    expect = 'NO SUCH ROUTE'
    ret = train_routes.distPath("B-D")
    all_pass.append(expect == ret)

    expect = 'NO SUCH ROUTE'
    ret = train_routes.distPath("E-D")
    all_pass.append(expect == ret)

    expect = 4
    ret = train_routes.distPath("D-E")
    all_pass.append(expect == ret)

    expect = 'NO SUCH ROUTE'
    ret = train_routes.distPath("B-D")
    all_pass.append(expect == ret)

    expect = 5
    ret = train_routes.distPath("C-A")
    all_pass.append(expect == ret)

    expect = 10
    ret = train_routes.distPath("A-B-C-A")
    all_pass.append(expect == ret)

    # All Paths max stops
    expect = 1
    ret = train_routes.numDiffPaths("A", "B", max_stops=1)
    all_pass.append(expect == ret)

    expect = 1
    ret = train_routes.numDiffPaths("A", "B", max_stops=2)
    all_pass.append(expect == ret)

    expect = 1
    ret = train_routes.numDiffPaths("A", "B", max_stops=3)
    all_pass.append(expect == ret)

    expect = 2
    ret = train_routes.numDiffPaths("A", "B", max_stops=4)
    all_pass.append(expect == ret)

    expect = 0
    ret = train_routes.numDiffPaths("A", "D", max_stops=8)
    all_pass.append(expect == ret)

    expect = 0
    ret = train_routes.numDiffPaths("A", "D", max_stops=2)
    all_pass.append(expect == ret)

    #  All paths with max_dist
    expect = 0
    ret = train_routes.numDiffPaths("A", "A", max_dist=9)
    all_pass.append(expect == ret)

    expect = 0
    ret = train_routes.numDiffPaths("A", "A", max_dist=10)
    all_pass.append(expect == ret)

    expect = 1
    ret = train_routes.numDiffPaths("A", "A", max_dist=11)
    all_pass.append(expect == ret)

    expect = 1
    ret = train_routes.numDiffPaths("A", "A", max_dist=20)
    all_pass.append(expect == ret)

    expect = 2
    ret = train_routes.numDiffPaths("A", "A", max_dist=21)
    all_pass.append(expect == ret)

    expect = 2
    ret = train_routes.numDiffPaths("A", "A", max_dist=30)
    all_pass.append(expect == ret)

    expect = 3
    ret = train_routes.numDiffPaths("A", "A", max_dist=31)
    all_pass.append(expect == ret)

    # shortest Path
    expect = float('inf')
    ret = train_routes.shortestPath("A", "D")
    all_pass.append(expect == ret)

    expect = float('inf')
    ret = train_routes.shortestPath("A", "E")
    all_pass.append(expect == ret)

    expect = 10
    ret = train_routes.shortestPath("A", "A")
    all_pass.append(expect == ret)

    expect = float('inf')
    ret = train_routes.shortestPath("E", "D")
    all_pass.append(expect == ret)

    return all_pass


def testOneWayNetwork():
    adjacency_list = generateAdjacencyList(
        networks_directory + "/connected-by-one-way.txt")
    train_routes = TrainRoutes(adjacency_list)

    all_pass = []

    # All paths between
    expect = 1
    ret = train_routes.numDiffPaths("A", "E", max_stops=4)
    all_pass.append(expect == ret)

    expect = 2
    ret = train_routes.numDiffPaths("A", "E", max_stops=7)
    all_pass.append(expect == ret)

    expect = 2
    ret = train_routes.numDiffPaths("A", "E", min_stops=4, max_stops=7)
    all_pass.append(expect == ret)

    expect = 1
    ret = train_routes.numDiffPaths("A", "E", min_stops=5, max_stops=7)
    all_pass.append(expect == ret)

    expect = 0
    ret = train_routes.numDiffPaths("E", "E", min_stops=5, max_stops=7)
    all_pass.append(expect == ret)

    expect = 0
    ret = train_routes.numDiffPaths("E", "E", min_stops=0, max_stops=7)
    all_pass.append(expect == ret)

    expect = 1
    ret = train_routes.numDiffPaths("A", "D", min_stops=0, max_stops=3)
    all_pass.append(expect == ret)

    expect = 2
    ret = train_routes.numDiffPaths("A", "D", min_stops=0, max_stops=6)
    all_pass.append(expect == ret)

    expect = 1
    ret = train_routes.numDiffPaths("A", "D", min_stops=4, max_stops=6)
    all_pass.append(expect == ret)

    # Shortest path
    expect = 11
    ret = train_routes.shortestPath("C", "E")
    all_pass.append(expect == ret)

    expect = 14
    ret = train_routes.shortestPath("B", "E")
    all_pass.append(expect == ret)

    expect = 16
    ret = train_routes.shortestPath("A", "E")
    all_pass.append(expect == ret)

    return all_pass


def testTwoCylesOneOneway():
    path_to_network = networks_directory + "/two-cycles-with-one-oneway.txt"
    adjacency_list = generateAdjacencyList(path_to_network)
    train_routes = TrainRoutes(adjacency_list)

    all_pass = []

    # All paths max stops and min stops
    expect = 2
    ret = train_routes.numDiffPaths("A", "D", min_stops=4, max_stops=6)
    all_pass.append(expect == ret)

    expect = 3
    ret = train_routes.numDiffPaths("A", "D", min_stops=0, max_stops=6)
    all_pass.append(expect == ret)

    expect = 6
    ret = train_routes.numDiffPaths("A", "D", min_stops=0, max_stops=9)
    all_pass.append(expect == ret)

    expect = 6
    ret = train_routes.numDiffPaths("A", "D", min_stops=0, max_stops=10)
    all_pass.append(expect == ret)

    # All paths max distance
    expect = 0
    ret = train_routes.numDiffPaths("A", "D", max_dist=12)
    all_pass.append(expect == ret)

    expect = 1
    ret = train_routes.numDiffPaths("A", "D", max_dist=13)
    all_pass.append(expect == ret)

    expect = 3
    ret = train_routes.numDiffPaths("A", "D", max_dist=23)
    all_pass.append(expect == ret)

    return all_pass


def testOneAlternatePath():
    path_to_network = networks_directory + "/one-alternate-path.txt"
    adjacency_list = generateAdjacencyList(path_to_network)
    train_routes = TrainRoutes(adjacency_list)

    all_pass = []

    # Simple shortest path
    expect = 7
    ret = train_routes.shortestPath("A", "E")
    all_pass.append(expect == ret)

    expect = float('inf')
    ret = train_routes.shortestPath("E", "A")
    all_pass.append(expect == ret)

    expect = float('inf')
    ret = train_routes.shortestPath("E", "A")
    all_pass.append(expect == ret)

    # All paths between
    expect = 1
    ret = train_routes.numDiffPaths("A", "E", max_stops=3)
    all_pass.append(expect == ret)

    expect = 2
    ret = train_routes.numDiffPaths("A", "E", max_stops=4)
    all_pass.append(expect == ret)

    expect = 1
    ret = train_routes.numDiffPaths("A", "E", min_stops=4, max_stops=4)
    all_pass.append(expect == ret)

    # Dist of path
    expect = 8
    ret = train_routes.distPath("A-B-D-E")
    all_pass.append(expect == ret)

    expect = 7
    ret = train_routes.distPath("A-B-C-D-E")
    all_pass.append(expect == ret)

    expect = "NO SUCH ROUTE"
    ret = train_routes.distPath("A-D-B-E")
    all_pass.append(expect == ret)

    # Shortest path
    expect = float('inf')
    ret = train_routes.shortestPath("D", "D")
    all_pass.append(expect == ret)

    expect = float('inf')
    ret = train_routes.shortestPath("E", "E")
    all_pass.append(expect == ret)

    expect = float('inf')
    ret = train_routes.shortestPath("E", "A")
    all_pass.append(expect == ret)

    return all_pass


def runTests():
    print(testComplextRoute())
    print(testDisconnectedNetwork())
    print(testOneWayNetwork())
    print(testTwoCylesOneOneway())
    print(testOneAlternatePath())


if __name__ == "__main__":
    runTests()
