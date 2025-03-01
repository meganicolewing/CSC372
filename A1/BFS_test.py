from cube import Cube
from Search import Search

searcher = Search()
cube = Cube()
cube.rotate(2,1)
cube.rotate(1,0)

searcher.breadth_first(cube)