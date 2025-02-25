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
    cube.randomize(2)
    searcher = Search()
    solution = searcher.breadth_first(cube)
    print(solution[0].path_cost)
    print(solution[1])

    solution = searcher.iterative_deepening(cube)
    print(solution[0].path_cost)
    print(solution[1])



if __name__ == "__main__":
    main()