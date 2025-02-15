import random


class Cube:
    '''
    Contains six sides of a rubik's cube, allowing for the cube to be manipulated and displayed
    '''
    def __init__(self):
        '''creates the rubik's cube in a solved state'''
        self.rubik = []
        for side in range(6):
            self.rubik.append([])
            for i in range(2):
                self.rubik.append([])
                for j in range(2):
                    self.rubik[side][i][j] = side
        
    def __str__(self):
        '''all values from each side of rubik: 
        the top first, then a layer with the left, front, right, and back, then a layer with the bottom'''
        print_string=""
        for i in range(2):
            print_string+="\t"+self.rubik[0][i][0]+" "+self.rubik[0][i][1]+"\n"
        for i in range(1,5):
            print_string+=self.rubik[i][0][0] + " " + self.rubik[i][0][1] + " "
        print_string+="\n"
        for i in range(1,5):
            print_string+=self.rubik[i][1][0]+" "+self.rubik[i][1][1]+" "
        for i in range(2):
            print_string+="\t"+self.rubik[5][i][0]+" "+self.rubik[5][i][1]+"\n"
        return print_string

    def clone(self):
        '''returns a Cube that is a deep copy of rubik'''
        new_cube = Cube()
        for side in range(6):
            for i in range(2):
                for j in range(2):
                    new_cube[side][i][j] = self.rubik[side][i][j]
        return new_cube

    def reset(self) -> None:
        '''resets rubik to a solved state'''
        for side in range(6):
            for i in range(2):
                for j in range(2):
                    self.rubik[side][i][j] = side

    def is_solved(self) -> bool:
        '''returns true if rubik is solved (each side has one color), false if not'''
        already_found = []
        for side in range(6):
            curr = self.rubik[side][0][0]
            if curr in already_found:
                return False
            already_found.append(curr)
            for i in range(2):
                for j in range(2):
                    if(self.rubik[side][i][j]!=curr):
                        return False
        return True

    def randomize(self, num:int) -> None:
        '''completes num turns on random sides of rubik'''
        for i in range(num):
            side = random.randint(0,5)
            self.rotate(side)

    def rotate(self, side:int, clockwise:bool=True) -> None:
        '''rotates rubik one turn, then prints the current state. 
        the side to be rotated is denoted by input side:
        0-top, 1-left, 2-front, 3-right, 4-back, 5-bottom
        rotates the side clockwise or counterclockwise based on input clockwise
        '''
        self.rotate_side(side)
        if side==0 or side == 5:
            self.rotate_top()
        elif side == 1 or side == 3:
            self.rotate_left()
        elif side == 2 or side == 4:
            self.rotate_front()
        
        #to turn counterclockwise, make the clockwise turn three total times
        if not clockwise:
            self.rotate(side, True)
            self.rotate(side,True)

    def rotate_front(self) -> None:
        '''rotates the front side of rubik one turn clockwise. used as a helper function.'''
        top_left = self.rubik[0][1][0]
        top_right = self.rubik[0][1][1]
        #set the top
        self.rubik[0][1][0] = self.rubik[1][1][1]
        self.rubik[0][1][1] = self.rubik[1][0][1]
        #set the left
        self.rubik[1][1][1] = self.rubik[5][0][1]
        self.rubik[1][0][1] = self.rubik[5][0][0]
        #set the bottom
        self.rubik[5][0][1]=self.rubik[3][0][0]
        self.rubik[5][0][0]=self.rubik[3][1][0]
        #set the right
        self.rubik[3][0][0]=top_left
        self.rubik[3][1][0]=top_right
    
    def rotate_top(self) -> None:
        '''rotates the top side of rubik one turn clockwise. used as a helper function.'''
        back_left = self.rubik[4][0][1]
        back_right = self.rubik[4][0][0]
        #set the back
        self.rubik[4][0][1] = self.rubik[1][0][1]
        self.rubik[4][0][0] = self.rubik[1][0][0]
        #set the left
        self.rubik[1][0][1] = self.rubik[5][0][1]
        self.rubik[1][0][0] = self.rubik[5][0][0]
        #set the front
        self.rubik[5][0][1]=self.rubik[3][0][1]
        self.rubik[5][0][0]=self.rubik[3][0][0]
        #set the right
        self.rubik[3][0][1]=back_left
        self.rubik[3][0][0]=back_right

    def rotate_left(self) -> None:
        '''rotates the left side of rubik one turn clockwise. used as a helper function.'''
        '''rotates the top side of rubik one turn clockwise. used as a helper function.'''
        top_left = self.rubik[0][0][0]
        top_right = self.rubik[0][1][0]
        #set the top
        self.rubik[0][0][0] = self.rubik[4][1][1]
        self.rubik[0][1][0] = self.rubik[4][0][1]
        #set the back
        self.rubik[4][0][1] = self.rubik[5][1][0]
        self.rubik[4][1][1] = self.rubik[5][0][0]
        #set the bottom
        self.rubik[5][1][0]=self.rubik[2][1][0]
        self.rubik[5][0][0]=self.rubik[2][0][0]
        #set the front
        self.rubik[2][1][0]=top_right
        self.rubik[2][0][0]=top_left
    
    def rotate_side(self, side) -> None:
        '''rotates the given side of rubik once clockwise. used as a helper function.'''
        temp = self.rubik[side][0][0]
        self.rubik[side][0][0] = self.rubik[side][1][0]
        self.rubik[side][1][0] = self.rubik[side][1][1]
        self.rubik[side][1][1] = self.rubik[side][0][1]
        self.rubik[side][0][1] = temp