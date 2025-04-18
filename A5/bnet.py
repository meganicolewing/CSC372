from FullDistribution import FullDistribution
from RejectionSampling import RejctionSampling
import sys

def getVar(argument=str):
    variable = 0
    if argument[0]=="B":
        variable = 1
    elif argument[0] == "E":
        variable  = 2
    elif argument[0] == "A":
        variable = 3
    elif argument[0] == "J":
        variable = 4
    elif argument[0] == "M":
        variable = 5
    if argument[1] == "f":
        variable = variable*(-1)
    return variable    

def main():
    args = sys.argv[1:]
    ands = []
    given = []
    i = 0
    index_given = len(args)
    while i<len(args):
        if(args[i] == "given"):
            index_given = i+1
        else:
            var = getVar(args[i])
            ands.append(var)
        i = i+1
    while index_given<len(args):
        var = getVar(args[index_given])
        given.append(var)
        index_given=index_given+1
    full_joint = FullDistribution()
    print("full dist",full_joint.infer(ands,given))
    rej_sam = RejctionSampling()
    print("sampling",rej_sam.infer(ands,given,500000,10))



if __name__ == "__main__":
    main()