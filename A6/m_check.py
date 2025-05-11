from MDP import MDP

def printMatrix(m):
    print(m[12],"\t",m[13],"\t",m[14],"\t",m[15])
    print(m[8],"\t",m[9],"\t",m[10],"\t",m[11])
    print(m[4],"\t",m[5],"\t",m[6],"\t",m[7])
    print(m[0],"\t",m[1],"\t",m[2],"\t",m[3])



def main():
        mdp = MDP()
        #print(mdp.valueIteration(0.01)[0])
        #print(mdp.valueIteration(0.01)[1])
        policy = mdp.policyIteration(10000)
        printMatrix(mdp.rewards)
        printMatrix(policy[0])
        printMatrix(policy[1])
        #diagnositcs:
        '''
        for s in mdp.states:
              for a in mdp.actions:
                print("state:",s,"action:",a)
                print(mdp.transition_matrix[12][s][a],mdp.transition_matrix[13][s][a],mdp.transition_matrix[14][s][a],mdp.transition_matrix[15][s][a])
                print(mdp.transition_matrix[8][s][a],mdp.transition_matrix[9][s][a],mdp.transition_matrix[10][s][a],mdp.transition_matrix[11][s][a])
                print(mdp.transition_matrix[4][s][a],mdp.transition_matrix[5][s][a],mdp.transition_matrix[6][s][a],mdp.transition_matrix[7][s][a])
                print(mdp.transition_matrix[0][s][a],mdp.transition_matrix[1][s][a],mdp.transition_matrix[2][s][a],mdp.transition_matrix[3][s][a])
                print("")
        for action in range(4):  # 0 = up, 1 = down, 2 = left, 3 = right
            print(f"\nACTION {action}")
            for next_state in range(16):
                row = ""
                for current_state in range(16):
                    prob = mdp.transition_matrix[next_state][current_state][action]
                    row += f"{int(round(prob * 100)):4}"
                print(row)

            print("\nColumn totals (should each be 1.0):")
            for current_state in range(16):
                total = sum(mdp.transition_matrix[next_state][current_state][action] for next_state in range(16))
                print(f"State {current_state}, Action {action} --> Total: {round(total, 4)}")
                assert round(total, 4) == 1.0, f"Probabilities for state {current_state}, action {action} sum to {total}, not 1.0"
'''
if __name__ == "__main__":
    main()