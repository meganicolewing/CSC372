import random


class Cube:
    '''
    Contains six sides of a rubik's cube, allowing for the cube to be manipulated and displayed
    '''
    def __init__(self):
        '''creates the rubik's cube in a solved state'''
        self.cube = []
        for side in range(6):
            self.cube.append([])
            for i in range(2):
                self.cube.append([])
                for j in range(2):
                    self.cube[side][i][j] = side
        
    def __str__(self):
        '''all values from each side of the cube: 
        the top first, then a layer with the left, front, right, and back, then a layer with the bottom'''

    def clone(self):
        '''returns a deep copy of the cube'''
        new_cube = Cube()
        for side in range(6):
            for i in range(2):
                for j in range(2):
                    new_cube[side][i][j] = self.cube[side][i][j]

    def reset(self):
        '''resets the cube to a solved state'''
        for side in range(6):
            for i in range(2):
                for j in range(2):
                    self.cube[side][i][j] = side

    def is_solved(self):
        '''returns true if the cube is solved (each side has one color), false if not'''
        already_found = []
        for side in range(6):
            curr = self.cube[side][0][0]
            if curr in already_found:
                return False
            already_found.append(curr)
            for i in range(2):
                for j in range(2):
                    if(self.cube[side][i][j]!=curr):
                        return False
        return True

    def randomize(self, num):
        '''completes num turns on random sides of the cube'''
        for i in range(num):
            side = random.randint(0,6)
            self.rotate(side)

    def rotate(self, side):
        '''rotates the cube one turn, then prints the current state. 
        the side to be rotated is denoted by input side:
        0-top, 1-left, 2-front, 3-right, 4-back, 5-bottom
        direction of the turn is determined by input clockwise: 
        true-clockwise, false-counterclockwise
        '''
        self.rotate_side(side)
        if side==0:
            self.rotate_top()
        elif side == 1:
            self.rotate_left()
        elif side == 2:
            self.rotate_front()
        elif side == 3:
            self.rotate_left()
        elif side == 4:
            self.rotate_back()
        else:
            self.rotate_bottom()

    def rotate_front(self):
        '''rotates the front side of the cube one turn clockwise'''
    
    def rotate_back(self):
        '''rotates the back side of the cube one turn clockwise'''
    
    def rotate_top(self):
        '''rotates the top side of the cube one turn clockwise'''

    def rotate_bottom(self):
        '''rotates the bottom side of the cube one turn clockwise'''
    
    def rotate_left(self):
        '''rotates the left side of the cube one turn clockwise'''
    
    def rotate_right(self):
        '''rotates the right side of the cube one turn clockwise'''

    def rotate_side(self, side):
        '''rotates the given side once clockwise'''
        temp = self.cube[side][0][0]
        self.cube[side][0][0] = self.cube[side][1][0]
        self.cube[side][1][0] = self.cube[side][1][1]
        self.cube[side][1][1] = self.cube[side][0][1]
        self.cube[side][0][1] = temp