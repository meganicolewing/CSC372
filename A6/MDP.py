
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