from sNode import sNode
from aStar import aStar
import heapq



def main():
    U = sNode([4,2,3,1,9,7,8],[],0)
    node, ofLife = aStar(U)
    print('solution ',node)
    while(node.parent != []):
        node = ofLife[node]
        print(node)
    print('^^^Start^^^')
    print(ofLife)


if __name__=="__main__":
    main()