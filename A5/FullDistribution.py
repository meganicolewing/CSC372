from Net import Net

NUM_VARS = 5

class FullDistribution:
    def __init__(self):
        self.net = Net()
        self.distribution = []
        self.expandDistribution()

    #expands the full joint distribution using the given net and iterating over binary
    #adds the probabilities and the corresponding binary into the distribution attribute
    def expandDistribution(self)->None:
        num_combs = (2**NUM_VARS)
        for i in range(num_combs):
            binary_rep = [int(i) for i in bin(i)[2:].zfill(NUM_VARS)]
            prob = self.net.And(binary_rep[0],binary_rep[1],binary_rep[2],binary_rep[3],binary_rep[4])
            binary_rep.insert(0,prob)
            self.distribution.append(binary_rep)

    #calculates and returns the probability
    #ands = values of all query and priors
    #given = values of all priors
    def infer(self,ands=[int],given=[int]) -> float:
        ands_sum,given_sum = self.sumProbs(ands,given)
        return ands_sum/given_sum

    #sums the total probability of the ands and givens
    #ands, givens = list of values
    def sumProbs(self,ands=[int], givens=[int]) -> tuple[int,int]:
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