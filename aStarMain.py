from sNode import sNode
from aStar import aStar
import heapq



def main():
    #[4,2,3,1,9,7,8]
    userInput=input('Enter integer sequence: ')
    sequence=[ int(i) for i in userInput.split(' ')]
    U = sNode(sequence,[],0)
    solution,lookup,cpuTime,totNodes, maxNodes = aStar(U)
    endToStart=[]
    current=solution
    while( current.parent != [] ):
        current=lookup[current.parent.key]
        endToStart.append(current)
    print('###From Start###')
    for node in reversed(endToStart):
        print(node)
    print('Solution---> ',solution)
    print('CPU Time', cpuTime)
    print('Total Visited States ',totNodes)
    print('Max Size Priority Queue ', maxNodes)
    '''
    print(U,' <--- Start Node')
    while( current.parent != [] ):
        reversePath.append( current )
        current=lookup[hash(str(current.parent.sequence))]
    for node in reversed(reversePath):
        print(node)
    print(solution,' <--- Solution Node')
    '''
if __name__=="__main__":
    main()