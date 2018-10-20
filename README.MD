# A* 
## Devin Brown & Trent Rhodes Ousley 
### Extra Credit Solution
The A* algorithm is using a hastable which in python is a dictionary. When a new child is created it is checked against the hashtable.  If the child already exists in the hashtable the g value is checked.  If a cheaper g value is found the already existing Node has its cost and parent values updated (decrease key.)   