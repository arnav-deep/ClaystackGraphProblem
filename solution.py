from AllClassesAndFunctions import *

print('Enter your input in one line separated with commas.\n' +
        'For Example: AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7\n')
routelist = [s.strip() for s in input().strip().split(',')]

g = Graph()
for route in routelist:
    g.addEdge(route[0], route[1], int(route[2]))

runForAll(g)