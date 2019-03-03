# Newage-Solutions Exercise
## Overview

### Sample Correctness

Calling,
```
python main.py
```
will load the sample graph provided in the assignment. Specifically,
```
AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7
```
and then runs the the 10 example inputs.

### Simple Use
```python
from train_route import TrainRoutes
from simple_util import generateAdjacencyList

def main():
    adjacency_list = generateAdjacencyList("train-graph-1.txt")
    train_routes = TrainRoutes(adjacency_list)
    print("The Distance of the route A-B-C:", train_routes.distPath("A-B-C"))
```

Output:
```
The Distance of the route A-B-C: 9.0
```

### Structure and Details

This assignment is divided into 4 major files: *graph.py, train_route.py, simple_util.py, and tests.py*

#### Graph.py

Contains only one class, the Graph class. Since train routing and path finding is fundamentally a graphing problem
I felt it was best to separate it to allow it to be more modular and extendable.

There are three major methods and two utility methods.
<p>The three major methods are: *dijkstra(), getWeightPath(), and getAllPathsBetween()*</p>
<p>The two utility methods are: *modGraph() and modUndo()*</p>

The dijkstra method is the traditional lowest cost path from a source to a target in a directed weighted graph. This
function is minimally modified to be able to exit early if the target vertex is reached

The getWeightPath method takes a path and returns the weight of the path if the entirety of the path exists
within the graph. If no such path exists, it returns -1. Functionally, this simply looks at each adjacent
pair of nodes and adds up the weight of the corresponding edge.

The getAllPathsBetween method is a modified Breadth First Search. In this modification visited vertices are no longer
marked visited. Since vertices are no longer marked visited there needed to be a new way to reduce the queue without missing
potential paths. The solution I developed is create a dictionary whose keys are verticies that mapped to a set of paths
whose final destination is the key. 
```
            E.g {"A":{["A", "B", "A"], ["B", "C", "A"], ["F", "A"]},
                 "E":{["F", "E"], ["D", "E", "D", "E"] }
```
This solution allowed me to keep track of paths that have been generated, systematically generate new paths, and easily 
prevent duplication of paths. With the help of the previously mentioned dictionary the queue is only appended to if 
at least one new path was generated. And of the newly generated paths at least one path is within the max path length or max 
path weight bound. Together, these modificaitons of BFS allows getAllPathsBetween to accurately and efficiently generated
all possible paths between two points bounded by max path length or max path weight.

The modGraph method takes a list of tuples each representing starting vertex, ending vertex, edge weight and modifies the
graph either updating a weight, adding a new edge, or removing an edge. The ability to modify the graph allows an efficient
way to compute new paths with consideration of the modification without generating an entirely new graph. Before the
modificaiton is applied the current state of the graph is saved in a stack. This method is paired with modUndo().

The modUndo method is called to undo what is done to the graph by the modGraph method. Simply pops the to saved state and
applies the saved state.

#### train_route.py

Contains only one class, and that class is TrainRoutes. TrainRoutes class only uses the Graph class.

There are three major methods: *shortestPath(), distPath(), and numDiffPaths()*

The shortestPath method in addition to simply lowest weight path using dijkstras provided by Graph, shortestPath can also 
compute lowest weight round trip. Since dijkstras will return zero on the shortest path from A to A. Computing lowest weight
round trip using dijkstras requires a modification in the following way. Find all inward edges towards the source, and duplicate those 
edges to also point towards an artificial edge. Then call dijkstras to find the shortest path from the original source to 
the artificial target. This allows for the discovery of the shortest round-trip.

The distPath method modifies the output of getWeightPath method of Graph. In TrainRoutes if a path does not exists within
the graph disPath returns "NO SUCH ROUTE" instead of -1.

The numDiffPaths method simply calls the getAllPathsBetween method of Graph but only returns the number of different paths, not
all the paths.

#### simple_util.py

Contains file read functions and formatting utility for feeding into graphs.

#### tests.py

These tests are not using Unittest because instructions were not to use external any libraries except for JUnit, and Ant/Maven.
However, conversion to Unittest is simple when required.