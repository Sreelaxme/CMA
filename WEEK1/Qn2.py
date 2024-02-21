import math
import matplotlib.pyplot as plt
import random as random

class Dice:
    def __init__(self, sides = 6):
        if type(sides)!=int or sides < 4:
            raise Exception("Cannot consturct the dice")
        self.sides = sides
        self.pd = [1/self.sides] * self.sides
        self.calculateCDF()
    
    def setProb(self,prob):
        if len(prob)!=self.sides or sum(prob) != 1:
            raise Exception("Invalid Probability distribution")
        self.pd = list(prob)
        self.calculateCDF()

    def calculateCDF(self):
        self.cdf = [0]
        for p in self.pd:
            self.cdf.append(p+self.cdf[-1])

    def __str__(self):
        return "A dice with " + str(self.sides) + " and probability distribution " + str(self.pd)
    
    def roll(self,n,barWidth = 0.4):
        expected = [n*i for i in self.pd]
        obtained = [0] * self.sides
        for i in range(n):
            roll = random.random()
            for i in range(self.sides):
                
                if self.cdf[i]<roll < self.cdf[i+1]:
                    obtained[i]+=1
        

        plt.bar(range(self.sides),expected,barWidth,label = 'expected')
        plt.bar([i+0.4 for i in range(self.sides)], obtained, barWidth, label='Actual')
        plt.xticks([r + barWidth/2 for r in range(self.sides)], [i+1 for i in range(self.sides)])
        plt.xlabel('Sides')
        plt.ylabel('Occurrences')
        plt.title('Outcome of ' + str(n) + ' throws of ' + str(self.sides) + ' sided dice')
        plt.legend()
        plt.show()
        

if __name__ == "__main__":
    d = Dice(4)
    # d.setProb((0.1, 0.2, 0.3,0.4))
    d.roll(100)
    print(d)