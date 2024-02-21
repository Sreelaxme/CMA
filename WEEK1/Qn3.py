import matplotlib.pyplot as plt
import random
import math
def estimatePi(n):
    sqCounts = 0
    circleCounts = 0
    ratios = []
    for i in range(n):
        pt = (random.uniform(-0.5,0.5),random.uniform(-0.5,0.5))
        if (pt[0]**2 + pt[1]**2 ) <= 0.5**2 : 
            circleCounts+=1
        sqCounts+=1
    
        ratios.append(4*circleCounts/sqCounts)

    plt.plot(ratios,label = 'estimation')
    plt.plot([math.pi]*len(ratios), label = 'value of pi')
    plt.title('Pi estimation')
    plt.xlabel('n')
    plt.ylabel('pi')
    plt.legend()
    plt.grid()
    plt.show()
if __name__== "__main__":

    estimatePi(2000000)