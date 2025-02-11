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
        '''returns true if the cube is solved (each side has one color), false if not'''

    def rotate(self, side, clockwise):
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
    

    
    class Side:
        '''contains the values for a single side of a 2x2 Rubik's cube.
        you can print this side, check if this side is solved, 
        and rotate this side'''
        def __init__(self, top_left, top_right, bottom_left, bottom_right):
            self.top_left = top_left
            self.top_right = top_right
            self.bottom_left = bottom_left
            self.bottom_right = bottom_right

        def __str__(self):
            '''each color from this side, formatted like this:
            1 2
            3 4'''
            
        def rotate(self, clockwise):
            '''rotates the values of this side one turn, 
            either clockwise or counterclockwise, based on input clockwise'''

        def is_solved(self):
            '''returns true if all colors on this side are the same'''