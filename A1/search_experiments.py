import time
from cube import Cube
from Search import Search

cubes = []
for i in range(20):
    cubes.append(Cube())
search = Search()
depth = 1
while True:

    for i in range(20):
        cubes[i].reset()
        cubes[i].randomize(depth)

    print("\n\nDepth",depth,":")
    #run A* tests first - shortest
    
    print("\nA* tests:",flush=True)
    print("Nodes Expanded,Wall Time,Nodes on Queue,Solution")
    for i in range(20):
        start = time.time()
        solution = search.deepening_A_star(cubes[i])
        end = time.time()
        print(solution[1],",",end-start,",",solution[2],",",solution[0])
    
    print("\nIDS tests:",flush=True)
    print("Nodes Expanded,Wall Time,Nodes on Queue,Solution")
    for i in range(20):
        start = time.time()
        solution = search.iterative_deepening(cubes[i])
        end = time.time()
        print(solution[1],",",end-start,",",solution[2],",",solution[0])
        
    print("\nBFS tests:",flush=True)
    print("Nodes Expanded,Wall Time,Nodes on Queue,Solution")
    for i in range(20):
        start = time.time()
        solution = search.breadth_first(cubes[i])
        end = time.time()
        print(solution[1],",",end-start,",",solution[2],",",solution[0])
    depth+=1