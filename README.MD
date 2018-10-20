# A* 
## Devin Brown & Trent Rhodes Ousley 
### Extra Credit Solution
The A* algorithm is using a hastable.  Children or sNodes are stored in key value pairs like '[1,3,2]':sNode().  An instance of an sNode contain a self sequence like [1,3,2] and a pointer to a parent instance of sNode.  If a new child has a sequence value existing in the hash table that child is not placed in the heap.  The new children instead have their g value or cost checked against the existing node. If a cheaper cost is found the already existing node has their cost and parent values updated in the heap. 