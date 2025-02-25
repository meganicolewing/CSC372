from cube import Cube
from typing import Self

class Node:

    def __init__(self, state:Cube, parent:Self=None, direction:int=-1,side:int=-1, path_cost:int=0, heuristic:float=0):
        '''initializes a node with all necesary properties, where the parent is a Node and the state is a Cube.
        the action is an int that indicates the rotation that, when performed on the parent's state, results in this state.
        a heuristic value may be given for A* search. otherwise, the value defaults to 0.'''
        self.parent = parent
        self.rotation_side = side
        self.rotation_direction = direction
        self.state = state
        self.path_cost = path_cost
        self.total_cost = path_cost + heuristic

    def __lt__(self, other:Self):
        return self.total_cost < other.total_cost
