from Qn2 import SquareMatrixFloat
import matplotlib.pyplot as plt

def errorVisualizer():
    m = 100
    b = [1,2,3,4]
    x = [i+1 for i in range(m)]
    s = SquareMatrixFloat(4)
    s.sampleSymmetric()
    while (not s.isDRDominant()):
        s.sampleSymmetric()
    print(s)
    (ej,xj) = s.jSolve(b, m)
    (egs,xgs) = s.gsSolve(b, m)
    print("Solution is by jSolve:",xj)
    print("Solution is by gsSolve:",xgs)

    #plotting the graph
    plt.plot(x,ej, color = "b", label = "jSolve")
    plt.plot(x,egs, color = "r", label = "gsSolve")
    plt.xlabel("iterations")
    plt.ylabel("error")
    plt.title("Comparison of error of jSolve and gsSolve in each iteration.")
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    errorVisualizer()