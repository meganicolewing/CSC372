from Net import Net

class RejctionSampling:
    def __init__(self):
        self.net = Net()

    #simulates the probability at least n times. 
    #continues simulating until the desired probaility has been simulated at least 10 times
    def infer(self,ands=[int],givens=[int], n=int,min=int):
        num_and = 0
        num_given = 0
        i = 0
        while i<n or num_and<min:
            i=i+1
            sample = self.net.priorSample()
            matches = True
            j = 0
            while j<len(ands) and matches:
                if ands[j]>0:
                    if not sample[abs(ands[j])-1]:
                        matches = False
                elif sample[abs(ands[j])-1]:
                    matches = False
                j = j+1
            if matches:
                num_and = num_and + 1
            matches = True
            j = 0
            while j<len(givens) and matches:
                if givens[j]>0:
                    if not sample[abs(givens[j])-1]:
                        matches = False
                elif sample[abs(givens[j])-1]:
                    matches = False
                j = j+1
            if matches:
                num_given = num_given + 1
        return num_and/num_given