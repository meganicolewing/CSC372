class Node:

    def __init__(self, parent, action:int, state, path_cost:int, heuristic:float=0):
        '''initializes a node with all necesary properties, where the parent is a Node and the state is a Cube.
        the action is an int that indicates the rotation that, when performed on the parent's state, results in this state.
        a heuristic value may be given for A* search. otherwise, the value defaults to 0.'''
        self.parent = parent
        self.action = action
        self.state = state
        self.path_cost = path_cost
        self.total_cost = path_cost + heuristic
