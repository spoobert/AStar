

class sNode():
    def __init__(self, seq, par, cost):
        self.sequence = seq
        self.parent = par
        self.cost = cost 
        self.lenSeq = len(seq)
        h = 0
        for i in range( len( self.sequence ) - 1 ):
            if ( not( self.sequence[i] == self.sequence[i + 1] - 1) and
                not( self.sequence[i] - 1 == self.sequence[i + 1] ) ):
                h += 1   
        self.fVal = (cost + ( (1/2)*h ) )
    
    def __repr__(self):
        return  str(self.sequence) + " <--- " + str(self.parent) + " " + str(self.fVal)

    def __lt__(self,other):
        return self.fVal < other.fVal

    def isSolution(self):
        for i in range( 0, len(self.sequence) - 1 ):
            if self.sequence[i] > self.sequence[i + 1]:
                return False
        return  True

