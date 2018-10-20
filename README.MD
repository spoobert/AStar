# A* 
## Devin Brown & Trent Rhodes Ousley 
### Extra Credit Solution
The A* algorithm is using a hash-table.  Children or sNodes are stored in key value pairs like '[1,3,2]':sNode().  An instance of an sNode contains a self sequence like [1,3,2] also a pointer to a parent instance of an sNode.  If a new child has a sequence value existing in the hash table that child is not placed in the heap until its g value or cost is checked against the existing value.  If a cheaper cost is found the already existing node has its cost and parent values updated in the heap.
