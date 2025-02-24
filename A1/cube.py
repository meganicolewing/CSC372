import random

TOP = 0
FRONT = 2
LEFT = 1
BOTTOM = 3
BACK = 5
RIGHT = 4

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
                self.rubik[side].append([])
                for j in range(2):
                    self.rubik[side][i].append([])
                    self.rubik[side][i][j] = (side)
        
    def __str__(self):
        '''all values from each side of rubik: 
        the top first, then a layer with the left, front, right, and back, then a layer with the bottom'''
        spacing = "    "
        print_string=""
        for i in range(2):
            print_string+=spacing+str(self.rubik[TOP][i][0])+" "+str(self.rubik[TOP][i][1])+"\n"
        for i in range(0,6):
            if i!=TOP and i!=BOTTOM:
                print_string+=str(self.rubik[i][0][0]) + " " + str(self.rubik[i][0][1]) + " "
        print_string+="\n"
        for i in range(0,6):
            if i!=TOP and i!=BOTTOM:
                print_string+=str(self.rubik[i][1][0])+" "+str(self.rubik[i][1][1])+" "
        print_string+="\n"
        for i in range(2):
            print_string+=spacing+str(self.rubik[BOTTOM][i][0])+" "+str(self.rubik[BOTTOM][i][1])+"\n"
        return print_string

    def interaction(self):
        '''gives user interaction for the cube. runs a loop of options until the user decides to exit.
        can call rotate, randomize, reset, is_solved, and print the cube'''
        user_input = 0
        while user_input!=6:
            print("1: Rotate a side")
            print("2: Randomize the cube")
            print("3: Check if the cube is solved")
            print("4: Reset the cube")
            print("5: Print the cube")
            print("6: Exit")
            user_input = int(input("What would you like to do?"))
            if(user_input==1):
                print(TOP,": top")
                print(LEFT,": left")
                print(FRONT,": front")
                print(BOTTOM,": bottom")
                print(RIGHT,": right")
                print(BACK,": back")
                side = int(input("Which side would you like to rotate?"))
                print("0: clockwise")
                print("1: counterclockwise")
                clockwise = (int(input("Do you want to turn the side clockwise or counterclockwise?")))==0
                self.rotate(side, clockwise)
                print(self)
            elif(user_input == 2):
                num = int(input("How many turns would you like to randomize?"))
                self.randomize(num)
                print(self)
            elif(user_input==3):
                if(self.is_solved()):
                    print("The cube is solved!")
                else:
                    print("The cube is not solved")
            elif(user_input==4):
                self.reset()
                print(self)
            elif(user_input==5):
                print(self)

    def clone(self):
        '''returns a Cube that is a deep copy of rubik'''
        new_cube = Cube()
        for side in range(6):
            for i in range(2):
                for j in range(2):
                    new_cube.rubik[side][i][j] = self.rubik[side][i][j]
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
        previous_turn = [-1,-1]
        for i in range(num):
            side = random.randint(0,2)
            direction = (random.randint(0,1)==0)
            while side==previous_turn[0] and direction!=previous_turn[1]:
                side = random.randint(0,2)
                direction = (random.randint(0,1)==0)
            self.rotate(side,direction)
            previous_turn = [side, direction]

    def rotate(self, side:int, clockwise:bool=True) -> None:
        '''rotates rubik one turn, then prints the current state. 
        the side to be rotated is denoted by input side:
        0-top, 1-left, 2-front, 3-right, 4-back, 5-bottom
        rotates the side clockwise or counterclockwise based on input clockwise
        '''
        self.rotate_side(side)
        if side==TOP or side == BOTTOM:
            self.rotate_top()
        elif side == LEFT or side == RIGHT:
            self.rotate_left()
        elif side == FRONT or side == BACK:
            self.rotate_front()
        
        #to turn counterclockwise, make the clockwise turn three total times
        if not clockwise:
            self.rotate(side, True)
            self.rotate(side,True)

    def rotate_front(self) -> None:
        '''rotates the front side of rubik one turn clockwise. used as a helper function.'''
        top_left = self.rubik[TOP][1][0]
        top_right = self.rubik[TOP][1][1]
        #set the top
        self.rubik[TOP][1][0] = self.rubik[LEFT][1][1]
        self.rubik[TOP][1][1] = self.rubik[LEFT][0][1]
        #set the left
        self.rubik[LEFT][1][1] = self.rubik[BOTTOM][0][1]
        self.rubik[LEFT][0][1] = self.rubik[BOTTOM][0][0]
        #set the bottom
        self.rubik[BOTTOM][0][1]=self.rubik[RIGHT][0][0]
        self.rubik[BOTTOM][0][0]=self.rubik[RIGHT][1][0]
        #set the right
        self.rubik[RIGHT][0][0]=top_left
        self.rubik[RIGHT][1][0]=top_right
    
    def rotate_top(self) -> None:
        '''rotates the top side of rubik one turn clockwise. used as a helper function.'''
        back_left = self.rubik[BACK][0][1]
        back_right = self.rubik[BACK][0][0]
        #set the back
        self.rubik[BACK][0][1] = self.rubik[LEFT][0][1]
        self.rubik[BACK][0][0] = self.rubik[LEFT][0][0]
        #set the left
        self.rubik[LEFT][0][1] = self.rubik[FRONT][0][1]
        self.rubik[LEFT][0][0] = self.rubik[FRONT][0][0]
        #set the front
        self.rubik[FRONT][0][1]=self.rubik[RIGHT][0][1]
        self.rubik[FRONT][0][0]=self.rubik[RIGHT][0][0]
        #set the right
        self.rubik[RIGHT][0][1]=back_left
        self.rubik[RIGHT][0][0]=back_right

    def rotate_left(self) -> None:
        '''rotates the left side of rubik one turn clockwise. used as a helper function.'''
        '''rotates the top side of rubik one turn clockwise. used as a helper function.'''
        top_left = self.rubik[TOP][0][0]
        top_right = self.rubik[TOP][1][0]
        #set the top
        self.rubik[TOP][0][0] = self.rubik[BACK][1][1]
        self.rubik[TOP][1][0] = self.rubik[BACK][0][1]
        #set the back
        self.rubik[BACK][0][1] = self.rubik[BOTTOM][1][0]
        self.rubik[BACK][1][1] = self.rubik[BOTTOM][0][0]
        #set the bottom
        self.rubik[BOTTOM][1][0]=self.rubik[FRONT][1][0]
        self.rubik[BOTTOM][0][0]=self.rubik[FRONT][0][0]
        #set the front
        self.rubik[FRONT][1][0]=top_right
        self.rubik[FRONT][0][0]=top_left
    
    def rotate_side(self, side) -> None:
        '''rotates the given side of rubik once clockwise. used as a helper function.'''
        temp = self.rubik[side][0][0]
        self.rubik[side][0][0] = self.rubik[side][1][0]
        self.rubik[side][1][0] = self.rubik[side][1][1]
        self.rubik[side][1][1] = self.rubik[side][0][1]
        self.rubik[side][0][1] = temp