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
        ands_sum,given_sum = self.sumProbs(ands,given)
        return ands_sum/given_sum

#change this to sum over both - make it go faster
    def sumProbs(self,ands=[int], givens=[int]):
        prob_and = 0
        prob_given = 0
        for i in range(len(self.distribution)):
            matches = True
            j = 0
            while j<len(ands) and matches:
                if ands[j]>0:
                    if self.distribution[i][abs(ands[j])] == 0:
                        matches = False
                elif self.distribution[i][abs(ands[j])] == 1:
                    matches = False
                j = j+1
            if matches:
                prob_and = prob_and + self.distribution[i][0]
            matches = True
            j = 0
            while j<len(givens) and matches:
                if givens[j]>0:
                    if self.distribution[i][abs(givens[j])] == 0:
                        matches = False
                elif self.distribution[i][abs(givens[j])] == 1:
                    matches = False
                j = j+1
            if matches:
                prob_given = prob_given + self.distribution[i][0]
        return prob_and, prob_given