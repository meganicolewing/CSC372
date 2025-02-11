class Cube:
    '''
    Contains six sides of a rubik's cube, allowing for the cube to be manipulated and displayed
    '''
    def __init__(self, front, left, right, top, bottom, back):
        '''creates the rubik's cube, setting each side of the cube to the given input'''
        self.front = front
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom
        self.back = back

    def __str__(self):
        '''all values from each side of the cube: 
        the top first, then a layer with the left, front, right, and back, then a layer with the bottom'''

    def reset(self):
        '''resets the cube to a solved state, then prints this out'''

    def is_solved(self):
        '''returns true if the cube is solved, false if not'''

    def rotate(self, side, clockwise)
        '''rotates the cube one turn, then prints the current state. 
        the side to be rotated is denoted by input side:
        1-front, 2-top, 3-left, 4-right, 5-back, 6-bottom
        direction of the turn is determined by input clockwise: 
        true-clockwise, false-counterclockwise
        '''

    def rotate_front_clockwise(self):
        '''rotates the front side of the cube one turn clockwise'''
    
    def rotate_front_counterclockwise(self):
        '''rotates the front side of the cube one turn counterclockwise'''
    
    def rotate_back_clockwise(self):
        '''rotates the back side of the cube one turn clockwise'''
    
    def rotate_back_counterclockwise(self):
        '''rotates the back side of the cube one turn counterclockwise'''
    
    def rotate_top_clockwise(self):
        '''rotates the top side of the cube one turn clockwise'''
    
    def rotate_top_counterclockwise(self):
        '''rotates the top side of the cube one turn counterclockwise'''
    
    def rotate_bottom_clockwise(self):
        '''rotates the bottom side of the cube one turn clockwise'''
    
    def rotate_bottom_counterclockwise(self):
        '''rotates the bottom side of the cube one turn counterclockwise'''
    
    def rotate_left_clockwise(self):
        '''rotates the left side of the cube one turn clockwise'''
    
    def rotate_left_counterclockwise(self):
        '''rotates the left side of the cube one turn counterclockwise'''
    
    def rotate_right_clockwise(self):
        '''rotates the right side of the cube one turn clockwise'''
    
    def rotate_right_counterclockwise(self):
        '''rotates the right side of the cube one turn counterclockwise'''
    

    
    