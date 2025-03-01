from cube import Cube
from Search import Search

def main():
    cube = Cube()
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
    searcher = Search()
    '''
    for i in range(15):
        for k in range(20):
            cube.reset()
            cube.randomize(i)
            print(cube)
            heuristic = searcher.heuristic(cube.rubik)
            assert heuristic<=i
    '''
    
if __name__ == "__main__":
    main()