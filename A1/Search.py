from queue import PriorityQueue

class Search:

    @staticmethod
    def breadth_first(cube):
        '''performs BFS using a priority queue to find the solution for the cube passed in'''
        pass

    @staticmethod
    def iterative_deepening(cube):
        '''performs iterative deepening DFS using recursion to find the solution for the cube passed in'''
        pass

    @staticmethod
    def deepening_A_star(cube):
        '''performs iterative deepening A* using recursion to find the solution for the cube passed in. 
        h(n) for each node is as stated in the heuristic function below'''
        pass

    @staticmethod
    def __depth_first(cube, max_depth:int):
        '''performs DFS to the limited depth as given in max_depth. returns a solution or NULL'''
        pass

    @staticmethod
    def __A_star(cube,max_depth:int):
        '''performs A* to the limited depth as given in max_depth. returns a solution or NULL'''
        pass

    @staticmethod
    def __heuristic(cube):
        pass