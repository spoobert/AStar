import heapq as hq
        
#arr[ [fVal] [cost] [currentSeq] [parentSeq] ]
def findH(arr):
    count = 0
    for i in range( len( arr ) - 1 ):
        if ( not( arr[i] == arr[i + 1] - 1) and
            not( arr[i] - 1 == arr[i + 1] ) ):
            count += 1   
    return count / 2 

def getF(arr):
    return arr[0][0]

def getCost(arr):
    return arr[1][0]

def getSeq(arr):
    return arr[2]

def makeChild(arr, parArr, childCost):
    tmp = []
    tmp.append( [ findH(arr) + childCost ] )
    tmp.append( [childCost] )
    tmp.append( arr )
    tmp.append( parArr )
    return tmp


def revSubSeq( seq, lBound, rBound ):
    newSeq = [ i for i in seq[:lBound] ]
    rPart = seq[rBound + 1:]
    mPart = seq[ lBound:rBound + 1 ]
    for i in reversed(mPart):
        newSeq.append(i)
    for i in rPart:
        newSeq.append(i)
    return newSeq


def isSolution( arr ):
    for i in range( 0, len(arr) - 1 ):
        if arr[i] > arr[i + 1]:
            return False
    return  True

def getParent(arr):
    return arr[3]

def cycle(parent, child):
    pass

def getKey(arr):
    tmp = ''
    for i in getSeq(arr):
        tmp += str(i)
    return tmp

def getKeyArr(arr):
    tmp = ''
    for i in arr:
        tmp += str(i)
    return tmp

#RULE: makechild is the only function that returns multi dim array
def aStar( seq ):
    children = []
    nodeLookup = {}
    nodeLookup[ getKey(seq) ] = []
    for L in range(0, len( getSeq(seq) ) - 1):
        for R in range(1, len( getSeq(seq) ) - L):
            child = makeChild( revSubSeq( getSeq( seq ), L, L + R ), getSeq( seq ), 1 )
            if getKey(child) not in nodeLookup:
                nodeLookup[ getKey( child ) ] = getParent( child )
            hq.heappush( children, child )
    for key in nodeLookup:
        print('key in astar ', key)
        print(nodeLookup[key])
        
    while( True ):
        current = hq.heappop(children)
        if isSolution( getSeq( current ) ):
            return (current, nodeLookup)
        for L in range(0, len( getSeq(current) ) - 1):
            for R in range(1, len( getSeq(current) ) - L):
                child = makeChild( revSubSeq( getSeq( current ), L, L + R ), getSeq( current ), getCost(current) + 1 )
                if getKey(child) not in nodeLookup:
                    nodeLookup[ getKey(child) ] = getParent( child )
                hq.heappush( children, child )
            


    return (children, nodeLookup)

        
def main():
    S = [ [0], [0], [4,1,2,3], [] ]
    (meaning, ofLife) = aStar( S )
    print('root parent ', ofLife[getKey(S)])
    print('###sol###',meaning,'###sol###')
    meaning = ofLife[ getKey(meaning) ]
    while( meaning != [] ):
        print('key: ',getKeyArr(meaning))
        meaning = ofLife[ getKeyArr( meaning ) ]
        print( meaning )
        input('waiting...')

if __name__=="__main__":
    main()




'''

def spawnChildren( arr ):
    children = []
    for L in range(0, len(getSeq(arr)) - 1):
        for R in range(1, len(getSeq(arr)) - L):
            childArr = revSubSeq( getSeq(arr), L, L + R )
            if  not childArr == getSeq(arr) and not childArr == getSeq(arr):
                child = makeChild( arr, childArr )   
                children.append( child )
    return children
'''