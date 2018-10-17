from sNode import sNode
import heapq


def revSubSeq( seq, lBound, rBound ):
    newSeq = [ i for i in seq[:lBound] ]
    rPart = seq[rBound + 1:]
    mPart = seq[ lBound:rBound + 1 ]
    for i in reversed(mPart):
        newSeq.append(i)
    for i in rPart:
        newSeq.append(i)
    return newSeq


def aStar(sN):
    sNodes = []
    nodeLookup = {}
    nodeLookup[ sN ] = []
    for L in range(0, sN.lenSeq - 1):
        for R in range(1, sN.lenSeq - L):
            newSeq = revSubSeq(sN.sequence, L, L + R)
            if newSeq != sN.sequence:
                child = sNode(newSeq, sN.parent, 1)
                nodeLookup[ child ] = sN
                heapq.heappush( sNodes, child )
        
    while( True ):
        current = heapq.heappop(sNodes)
        if current.isSolution():
            return (current, nodeLookup)
        for L in range(0, current.lenSeq - 1):
            for R in range(1, current.lenSeq - L):
                newSeq = revSubSeq( current.sequence, L, L + R )
                if newSeq != current.sequence:
                    child = sNode( newSeq, current, current.cost + 1 )
                    heapq.heappush( sNodes, child )
                    nodeLookup[child] = current
                    

    return (sNodes, nodeLookup)
