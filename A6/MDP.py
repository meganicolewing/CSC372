
class MDP:

    def __init__(self):
        states = []
        rewards = []
        for i in range(16):
            states.append(i)
            rewards.append(50)
            if(i%2==0):
                rewards[i] = 0
            elif(i==10):
                rewards[i] = 100
            elif(i==12):
                rewards[i] = 200
        #0 - up
        #1 - down
        #2 - left
        #3 - right
        actions = [0,1,2,3]

    def transition(self,next_state=int, current_state=int, action=int)->float:
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