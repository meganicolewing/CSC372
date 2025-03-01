from queue import PriorityQueue
from Node import Node
from cube import Cube

#actions
#direction = action%2
#side = (action//2)%3
TOP_CW = 0
TOP_CC = 1
LEFT_CW = 2
LEFT_CC = 3
FRONT_CW = 4
FRONT_CW = 5

class Search:

    #untested!!
    def breadth_first(self,cube:Cube) -> tuple[list[tuple[int,int]],int,int]:
        '''performs BFS using a priority queue to find the solution for the cube passed in
        returns a solution node, the number of nodes expanded, and the number of nodes left on the queue'''
        frontier = PriorityQueue()
        initial_node = Node(cube)
        nodes_expanded = 0
        nodes_on_queue = 1
        frontier.put((initial_node.path_cost,initial_node))
        while not frontier.empty():
            expanding = frontier.get()[1]
            nodes_on_queue-=1
            if expanding.state.is_solved():
                solution = self.__get_solution(expanding)
                return solution,nodes_expanded,nodes_on_queue
            nodes_expanded+=1
            for i in range(0,6):
                direction = i%2
                side = (i//2)%3
                if not(direction!=expanding.rotation_direction and side==expanding.rotation_side):
                    next_state = expanding.state.clone()
                    next_state.rotate(side,direction)
                    next_node = Node(next_state,expanding,direction,side,expanding.path_cost+1)
                    frontier.put((next_node.path_cost,next_node))
                    nodes_on_queue+=1
        return None,nodes_expanded,nodes_on_queue


    #add a count of the number of nodes left on the stack?
    #untested!!
    def iterative_deepening(self,cube:Cube) -> tuple[list[tuple[int,int]],int] :
        '''performs iterative deepening DFS using recursion to find the solution for the cube passed in'''
        solution = None
        max_depth = 0
        nodes_expanded=[0]
        while solution == None:
            max_depth+=1
            initial_node = Node(cube)
            solution = self.__depth_first(initial_node,max_depth,nodes_expanded)
        sequence = self.__get_solution(solution)
        return sequence,nodes_expanded[0]

    def deepening_A_star(self,cube:Cube) -> tuple[list[tuple[int,int]],int,int]:
        '''performs iterative deepening A* using a priority queue to find the solution for the cube passed in. 
        h(n) for each node is as stated in the heuristic function below'''
        nodes_expanded = 0
        depth = 1
        while True:
            frontier = PriorityQueue()
            initial_node = Node(cube)
            nodes_on_queue = 1
            frontier.put((initial_node.total_cost,initial_node))
            while not frontier.empty():
                expanding = frontier.get()[1]
                if expanding.total_cost>depth:
                    depth = expanding.total_cost
                    break
                nodes_on_queue-=1
                if expanding.state.is_solved():
                    solution = self.__get_solution(expanding)
                    return solution,nodes_expanded,nodes_on_queue
                nodes_expanded+=1
                for i in range(0,6):
                    direction = i%2
                    side = (i//2)%3
                    if not(direction!=expanding.rotation_direction and side==expanding.rotation_side):
                        next_state = expanding.state.clone()
                        next_state.rotate(side,direction)
                        heuristic = self.__heuristic(next_state.rubik)
                        next_node = Node(next_state,expanding,direction,side,expanding.path_cost+1,heuristic)
                        frontier.put((next_node.total_cost,next_node))
                        nodes_on_queue+=1


    def __depth_first(self,node:Node, max_depth:int,nodes_expanded:list[int]) -> Node:
        '''uses recursion to perform DFS to the limited depth as given in max_depth.
        node is the current node of the search tree, nodes_expanded is used to track the total number of nodes explored so far
        returns a solution node or None'''
        if node.total_cost>max_depth:
            return None
        if node.state.is_solved():
            return node
        nodes_expanded[0]+=1
        for i in range(0,6):
            direction = i%2
            side = (i//2)%3
            if not(direction!=node.rotation_direction and side==node.rotation_side):
                next_state = node.state.clone()
                next_state.rotate(side,direction)
                next_node = Node(next_state,node,direction,side,node.path_cost+1)
                solution = self.__depth_first(next_node,max_depth,nodes_expanded)
                if solution!=None:
                    return solution
        return None

    #relic, definct after switch from recursion to PQ
    def __A_star(self,node:Node,max_depth:int,nodes_expanded:int=0):
        '''uses recursion to perform A* to the limited depth as given in max_depth.
        h(n) for each node is as stated in the heuristic function below
        node is the current node of the search tree, nodes_expanded is used to track the total number of nodes explored so far
        returns a tuple: [solved node,nodes_expanded]. if no solution, the solved node will be null'''
        if node.total_cost>max_depth:
            return [None,nodes_expanded]

    def __heuristic(self,cube:list[list[list[int]]]) -> float:
        '''calculates heuristic for the given cube.
        estimates a minimum of the number of moves required to solve the cube'''
        cube_data = self.__analyze_cube(cube)
        #print(cube_data)
        goal_colors = self.__set_goal(cube_data)
        #print(goal_colors)
        hn = 0
        for i in range(6):
            inverse_side = i+3
            if inverse_side>5:
                inverse_side = inverse_side%3
            for j in range(2):
                for k in range(2):
                    color = cube[i][j][k]
                    if color != goal_colors[i]:
                        hn+=1
                        if color == goal_colors[inverse_side]:
                            hn+=1
        hn = hn/8
        #print(hn)
        return hn
                       


    def __analyze_cube(self,cube:Cube) -> dict:
        side_count = {}
        for i in range(6):
            for color in range(6):
                side_count[(i,color)]=0
            for j in range(2):
                for k in range(2):
                    color = cube[i][j][k]
                    side_count[(i,color)]+=1
        return side_count

    def __set_goal(self,cube_data:dict) -> list[int]:
        goals = [-1,-1,-1,-1,-1,-1]
        while -1 in goals:
            (best_side,best_color) = max(cube_data,key=cube_data.get)
            cube_data[(best_side,best_color)]=0
            if goals[best_side]==-1:
                goals[best_side]=best_color
                inverse_side = best_side+3
                inverse_color = best_color+3
                if inverse_side>5:
                    inverse_side = inverse_side%3
                if inverse_color>5:
                    inverse_color = inverse_color%3
        return goals


    def __get_solution(self,solved:Node) -> list[tuple[int,int]]:
        '''generates a solution sequence based on the given Node, which is a solved Node
        returns a list of tuples: [rotation side, rotation direction]'''
        solution = []
        while solved.parent!=None:
            solution.insert(0,[solved.rotation_side,solved.rotation_direction])
            solved = solved.parent
        return solution