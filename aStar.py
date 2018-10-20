from sNode import sNode
import heapq
import time


def aStar(currNode):
    cpuTime = time.clock()
    Nodes = []
    totNodes = 0
    maxNodes = 0
    pathMap = {}
    pathMap[currNode.key]=currNode
    for L in range(0, currNode.lenSeq - 1):
        for R in range(1, currNode.lenSeq - L):
            newSeq = currNode.revSubSeq(L, L + R) 
            if newSeq != currNode.sequence:
                child = sNode(newSeq, currNode, 1 + currNode.cost ) 
                if currNode.isSolution():
                    return(currNode, pathMap, time.clock() - cpuTime,totNodes,maxNodes)
                if child.key in pathMap:
                    oldCost = pathMap[child.key].cost
                    newCost = child.cost
                    if newCost < oldCost:
                        pathMap[child.key].cost=newCost
                        pathMap[child.key].parent=child.parent                          
                else:
                    pathMap[child.key]=child
                    heapq.heappush( Nodes, child ) 
                    totNodes+=1                       
    while( True ):
        sizeNodes = len(Nodes)
        if sizeNodes > maxNodes:
            maxNodes=sizeNodes 
        currNode = heapq.heappop(Nodes)
        if currNode.isSolution():
            return (currNode, pathMap, time.clock() - cpuTime, totNodes, maxNodes)
        for L in range(0, currNode.lenSeq - 1):
            for R in range(1, currNode.lenSeq - L):
                newSeq = currNode.revSubSeq(L, L + R )
                if newSeq != currNode.sequence:
                    child = sNode( newSeq, currNode, currNode.cost + 1 )
                    if currNode.isSolution():
                        return(currNode, pathMap, time.clock() - cpuTime,totNodes,maxNodes)
                    if child.key in pathMap:
                        oldCost = pathMap[child.key].cost
                        newCost = child.cost
                        if newCost < oldCost:
                            pathMap[child.key].cost=child.cost
                            pathMap[child.key].parent=child.parent
                    else:
                        pathMap[child.key]=child
                        heapq.heappush( Nodes, child )
                        totNodes+=1 
        

    return (currNode, pathMap, time.clock - cpuTime, totNodes, maxNodes)
