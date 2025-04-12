from Net import Net

NUM_VARS = 5

class FullDistribution:
    def __init__(self):
        self.net = Net()
        self.distribution = []
        self.expandDistribution()

    def expandDistribution(self)->None:
        num_combs = (2**NUM_VARS)
        for i in range(num_combs):
            binary_rep = [int(i) for i in bin(i)[2:].zfill(NUM_VARS)]
            prob = self.net.And(binary_rep[0],binary_rep[1],binary_rep[2],binary_rep[3],binary_rep[4])
            binary_rep.insert(0,prob)
            self.distribution.append(binary_rep)

    def infer(self,ands=[int],given=[int]):
        ands_sum = self.sumProbs(ands)
        given_sum = self.sumProbs(given)
        return ands_sum/given_sum

    def sumProbs(self,vars=[int]):
        prob = 0
        for i in range(len(self.distribution)):
            matches = True
            j = 0
            while j<len(vars) and matches:
                if vars[j]>0:
                    if self.distribution[i][abs(vars[j])] == 0:
                        matches = False
                elif self.distribution[i][abs(vars[j])] == 1:
                    matches = False
                j = j+1
            if matches:
                prob = prob + self.distribution[i][0]
        return prob