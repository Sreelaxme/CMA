import math
import random

class RowVectorFloat:
    def __init__(self,elements:list=[]):
        self.elements = elements

    def __str__(self):
        ans = ""
        for i in self.elements:
            ans+= str(i)+" "
        return ans

    def __len__(self):
        return len(self.elements)
    def __getitem__(self,index):
        return self.elements[index]
    def __setitem__(self,index,val):
        self.elements[index] = val

    def __rmul__(self,val):
        if(type(val) == float,int):
            self.elements = [x*val for x in self.elements]
            return RowVectorFloat(self.elements)
        else:
            raise Exception("Invalid multiplication")
    def __add__(self,val):
        if(isinstance(val,RowVectorFloat)):
            if(len(val)==len(self.elements)):
                ans = [x+y for x, y in zip(self.elements, val.elements)]
                return RowVectorFloat(ans)
            else:
                raise Exception("Invalid addition")
        else:
            raise Exception("Difference types")
    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return RowVectorFloat([x / other for x in self.elements])
        else:
            raise Exception("Invalid division")
    def __sub__(self, other):
        if isinstance(other, RowVectorFloat):
            if len(other) == len(self.elements):
                return RowVectorFloat([x - y for x, y in zip(self.elements, other.elements)])
            else:
                raise Exception("Invalid subtraction: Vectors have different lengths")
        else:
            raise Exception("Invalid subtraction: Unsupported operand type")
