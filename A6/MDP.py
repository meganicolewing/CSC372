
class MDP:

    def __init__(self):
        self.states = []
        self.rewards = []
        for i in range(16):
            self.states.append(i)
            self.rewards.append(50)
            if(i%2==0):
                self.rewards[i] = 0
            elif(i==10):
                self.rewards[i] = 100
            elif(i==12):
                self.rewards[i] = 200
        #0 - up
        #1 - down
        #2 - left
        #3 - right
        self.actions = [0,1,2,3]
        self.transition_matrix = []
        for next in self.states:
            self.transition_matrix.append([])
            for current in self.states:
                self.transition_matrix[next].append([])
                for action in self.actions:
                    self.transition_matrix[next][current].append(self.transitionFunction(next,current,action))
        self.discount = 0.95

    #returns P(next_state|current_state,action), with bounce taken into account
    #used to calculate the transition matrix in the initializer, should not be used elsewhere for efficiency
    def transitionFunction(self,next_state=int, current_state=int, action=int)->float:
        retval = 0
        if(next_state==current_state):
            return 0.1
        if(action == 0):
            if(next_state == (current_state+4) or ((current_state+4)>15 and (current_state-4)==next_state)):
                retval = retval + 0.7
            if(next_state == (current_state-4) or ((current_state-4)<0 and (current_state+4)==next_state)):
                retval = retval + 0.2
        if(action == 1):
            if(next_state == (current_state-4) or ((current_state-4)<0 and (current_state+4)==next_state)):
                retval = retval + 0.7
            if(next_state == (current_state+4) or ((current_state+4)>15 and (current_state-4)==next_state)):
                retval = retval + 0.2
        if(action == 2):
            if(next_state == (current_state-1) or (((current_state)%4)==0 and (current_state+1)==next_state)):
                retval = retval + 0.7
            if(next_state == (current_state+1) or (((current_state+1)%4)==0 and (current_state-1)==next_state)):
                retval = retval + 0.2
        if(action == 3):
            if(next_state == (current_state+1) or (((current_state+1)%4)==0 and (current_state-1)==next_state)):
                retval = retval + 0.7
            if(next_state == (current_state-1) or (((current_state)%4)==0 and (current_state+1)==next_state)):
                retval = retval + 0.2
        return retval

    #calculates the utility of every state, within the given error
    def utilityFuction(self,error=float)->list[float]:
        utility = []
        new_utility = []
        for i in self.states:
            new_utility.append(0)
            utility.append(0)
        delta = error * (1.0-self.discount)/self.discount
        while delta>=(error * (1.0-self.discount)/self.discount):
            for i in range(len(self.states)):
                utility[i] = new_utility[i]
            delta = 0
            for current in self.states:
                sumOverActions = []
                for action in self.actions:
                    sumOverActions.append(0)
                    for next in self.states:
                        sumOverActions[action] = sumOverActions[action] + self.transition_matrix[next][current][action]*utility[next]
                new_utility[current] = self.rewards[current] + self.discount*max(sumOverActions)
                delta = max(delta,abs(utility[current],new_utility[current]))
        return utility

    #determines the optimal policy using value iteration
    #given the error for the utility
    def valueIteration(self,error=float)->tuple[list[int],list[float]]:
        utility = self.utilityFuction(error)
        policy = []
        for current in self.states:
            policy.append[0]
            valueOfActions = []
            for a in self.actions:
                valueOfActions.append(0)
                for next in self.states:
                    valueOfActions[a] = valueOfActions[a] + self.transition_matrix[next][current][a]*utility[next]
            max_util = max(valueOfActions)
            policy[current]=valueOfActions.index(max_util)
        return policy,utility
