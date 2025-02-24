class Node:

    def __init__(self, parent, action:int, state, path_cost:int, heuristic:float):
        '''initializes a node with all necesary properties, where the parent is a Node and the state is a Cube.
        the action is an int that indicates the rotation that, when performed on the parent's state, results in this state.'''
        self.parent
        self.action
        self.state
        self.path_cost
        self.heuristic
