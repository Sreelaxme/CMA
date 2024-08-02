import numpy as np
from scipy.fft import fft,ifft

def fastMultLargeNums(a,b):
    nDigits = len(str(a))+len(str(b))
    
    # extracting digits to list
    a_,b_=a,b
    xa,xb=[],[]
    for i in range(nDigits):
        xa.append(a_%10)
        xb.append(b_%10)
        a_//=10
        b_//=10
    
    # computing fft of both the lists
    xa=fft(xa)
    xb=fft(xb)
    
    # performing multiplication
    pdt = xa*xb
    
    # computing inverse fft
    pdt = ifft(pdt)
    ans = 0
    for i,v in enumerate(pdt):
        ans+=round(v.real) * (10**i)
        #    ^ -- we have to round() here so that the accuracy is preserved

    return int (ans)

if __name__ == "__main__":

    a = 2**10
    b = 2**10
    val= fastMultLargeNums(a,a)
    # val= fft_multiply(a,a)

    print(a*b)
    print(val)