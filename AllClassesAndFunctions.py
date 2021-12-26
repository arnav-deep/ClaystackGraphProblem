from collections import defaultdict
import math

# Simple Graph class to store routes and distance matrix
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.weightmatrix = [[-1 for i in range(5)] for i in range(5)]
        self.nodenumber = {
            'A': 0,
            'B': 1,
            'C': 2,
            'D': 3,
            'E': 4,
        }

    def addEdge(self, u, v, w):
        self.graph[u].append(v)
        self.weightmatrix[self.nodenumber[u]][self.nodenumber[v]] = w


# Funtion for Outputs 1 to 5.
def distanceOfRoute(g: Graph, route: str):
    """
    Function: Take the routes and the path to caluculate the total distance.

    Input Parameters:
    g: matrix of the routes of the graph.
    route: a string showing the path. For Ex: For path A-B-C-D, string is 'ABCD'.

    Returns:
    Returns the total distance if route exists.
    """
    route = list(route)
    currStop = route[0]
    ans = 0
    for stop in route[1:]:
        stopDist = g.weightmatrix[g.nodenumber[currStop]][g.nodenumber[stop]]
        if stopDist == -1:
            return 'NO SUCH ROUTE'
        ans += stopDist
        currStop = stop
    return ans


# Funtion for Output 6.
def tripsCToCStops(g: Graph, source: str, destination: str, numberOfStops: int):
    """
    Function: Finds the number of routes from source to destination with the maximum numberOfStops stops.

    Input Parameters:
    g: matrix of the routes of the graph.
    source: the source/starting point of the journey.
    destination: the destination/ending point of the journey.
    numberOfStops: maxmimum number of stops allowed

    Returns:
    The number of total trips possible from source to destination with the maximum numberOfStops stops.
    """
    queue = []
    ans = 0
    queue.append([1]+g.graph[source])
    while True:
        tempDestination = queue.pop(0)
        for stop in tempDestination[1:]:
            if stop == destination:
                ans += 1
            else:
                if tempDestination[0] < numberOfStops:
                    queue.append([tempDestination[0]+1] + g.graph[stop])
        if len(queue) == 0:
            break
    return ans


# Function for Output 7.
def tripsWithExactStops(g: Graph, source: str, destination: str, numberOfStops: int):
    """
    Function: Finds the number of routes from source to destination with exactly numberOfStops stops.

    Input Parameters:
    g: matrix of the routes of the graph.
    source: the source/starting point of the journey.
    destination: the destination/ending point of the journey.
    numberOfStops: exact number of stops allowed.

    Returns:
    The number of total trips possible from source to destination with exactly numberOfStops stops.
    """
    queue = []
    ans = 0
    queue.append([1]+g.graph[source])
    while True:
        tempDestination = queue.pop(0)
        for stop in tempDestination[1:]:
            if stop == destination and tempDestination[0] == numberOfStops:
                ans += 1
            else:
                if tempDestination[0] < numberOfStops:
                    queue.append([tempDestination[0]+1] + g.graph[stop])
        if len(queue) == 0:
            break
    return ans


# For Output 8 and 9.
def shortestDistBetweenTwoPoints(g: Graph, source, destination):
    """
    Function: Returns the distance of the shortest path between two stops.

    Input Parameters:
    g: matrix of the routes of the graph.
    source: the source/starting point of the journey.
    destination: the destination/ending point of the journey.

    Returns:
    The distance of the shortest path between the two source ad the destination.
    """
    queue = []
    ans = math.inf
    for stop in g.graph[source]:
        distToStop = g.weightmatrix[g.nodenumber[source]][g.nodenumber[stop]]
        queue.append([distToStop, source, stop])
    while True:
        if len(queue) == 0:
            break
        tempDestination = queue.pop(0)
        if tempDestination[0] >= ans:
            continue
        if tempDestination[2] == destination:
            ans = tempDestination[0]
        else:
            for stop in g.graph[tempDestination[2]]:
                nextDist = tempDestination[0]+g.weightmatrix[g.nodenumber[tempDestination[2]]][g.nodenumber[stop]]
                if nextDist < ans:
                    queue.append([nextDist, tempDestination[2], stop])
    return ans


# Funtion for Output 10.
def roundTripsWithDist(g: Graph, source_stop: str, maxDist: int):
    """
    Function: Finds the number of routes from source_stop to source_stop that have distance less than maxDist.

    Input Parameters:
    g: matrix of the routes of the graph.
    source_stop: the stop where the round trip is done.
    maxDist: the distance from which the total distance should be less than

    Returns:
    The number of total trips possible from source_stop to source_stop that have distance less than maxDist.
    """
    queue = []
    allPossibleTrips = []
    for stop in g.graph[source_stop]:
        distToStop = g.weightmatrix[g.nodenumber[source_stop]][g.nodenumber[stop]]
        queue.append([distToStop, source_stop, stop, source_stop+stop])
    while True:
        if len(queue) == 0:
            break
        tempDestination = queue.pop(0)
        if tempDestination[0] >= maxDist:
            continue
        if tempDestination[2] == source_stop:
            allPossibleTrips.append(tempDestination[3])
        for stop in g.graph[tempDestination[2]]:
            nextDist = tempDestination[0]+g.weightmatrix[g.nodenumber[tempDestination[2]]][g.nodenumber[stop]]
            if nextDist < maxDist:
                queue.append([nextDist, tempDestination[2], stop, tempDestination[3]+stop])
    return len(allPossibleTrips)


# Function to print all outputs
def runForAll(g):
    print('Output 1:  ', distanceOfRoute(g, 'ABC'))
    print('Output 2:  ', distanceOfRoute(g, 'AD'))
    print('Output 3:  ', distanceOfRoute(g, 'ADC'))
    print('Output 4:  ', distanceOfRoute(g, 'AEBCD'))
    print('Output 5:  ', distanceOfRoute(g, 'AED'))
    print('Output 6:  ', tripsCToCStops(g, 'C', 'C', 3))
    print('Output 7:  ', tripsWithExactStops(g, 'A', 'C', 4))
    print('Output 8:  ', shortestDistBetweenTwoPoints(g, 'A', 'C'))
    print('Output 9:  ', shortestDistBetweenTwoPoints(g, 'B', 'B'))
    print('Output 10: ', roundTripsWithDist(g, 'C', 30))
