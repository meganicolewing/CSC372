from cube import Cube
from Search import Search
import time

TOP = 0
FRONT = 2
LEFT = 1
BOTTOM = 3
BACK = 5
RIGHT = 4

def main():
    cube = Cube()
    interaction(cube)
    '''
    print(cube)
    assert(cube.is_solved())
    print(cube.is_solved())
    cube.rotate(0)
    print(cube)
    cube.rotate(2)
    print(cube)
    cube.rotate(1)
    print(cube)
    cube.rotate(1, False)
    cube.rotate(2, False)
    cube.rotate(0, False)
    print(cube)
    assert(cube.is_solved())
    cube.randomize(5)
    print(cube)
    copy = cube.clone()
    assert(copy!=cube)
    cube.reset()
    assert(cube.is_solved())
    cube.interaction()'''
    '''
    for i in range(15):
        for k in range(20):
            cube.reset()
            cube.randomize(i)
            print(cube)
            heuristic = searcher.heuristic(cube.rubik)
            assert heuristic<=i
    '''
def interaction(cube):
    '''gives user interaction for the cube. runs a loop of options until the user decides to exit.
    can call rotate, randomize, reset, is_solved, and print the cube
    you can also sove the cube, using BFS, IDDFS, or IDA*. these searches will print the 
    solution, number of nodes searched, number of nodes left on the queue, and the time (in seconds)'''
    user_input = 0
    while user_input!=7:
        print("1: Rotate a side")
        print("2: Randomize the cube")
        print("3: Check if the cube is solved")
        print("4: Reset the cube")
        print("5: Print the cube")
        print("6: Find a solution for the cube")
        print("7: Exit")
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
            cube.rotate(side, clockwise)
        elif(user_input == 2):
            num = int(input("How many turns would you like to randomize?"))
            cube.randomize(num)
        elif(user_input==3):
            if(cube.is_solved()):
                print("The cube is solved!")
            else:
                print("The cube is not solved")
        elif(user_input==4):
            cube.reset()
        elif(user_input==5):
            print(cube)
        elif(user_input==6):
            searcher = Search()
            print("0: Breadth First Search")
            print("1: Iterative Deepening Depth First Search")
            print("2: Iterative Deepening A*")
            algorithm = int(input("What search algorithm would you like to use?"))
            solution = []
            start = time.time()
            if algorithm == 0:
                solution = searcher.breadth_first(cube)
            elif algorithm==1:
                solution = searcher.iterative_deepening(cube)
            elif algorithm==2:
                solution = searcher.deepening_A_star(cube)
            end = time.time()
            print("Solution:",solution[0])
            print("Nodes Searched:",solution[1])
            print("Nodes Left:",solution[2])
            print("Time (Seconds):",end-start)

if __name__ == "__main__":
    main()