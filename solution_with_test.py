from AllClassesAndFunctions import *

g = Graph()
routelist = ['AB5', 'BC4', 'CD8', 'DC8', 'DE6', 'AD5', 'CE2', 'EB3', 'AE7']
for route in routelist:
    g.addEdge(route[0], route[1], int(route[2]))

runForAll(g)