import numpy as np
from scipy.fft import fft,ifft

def fft_multiply(a,b):
    a = np.array(list(str(a)), dtype=int)
    b = np.array(list(str(b)), dtype=int)
    n = len(a)+len(b)-1
    X = fft(a)
    Y = fft(b)
    Z = ifft(X*Y)
    ans = 0
    for i,v in enumerate(Z):
        ans+=round(v.real)*(10**i)

    return int(ans)
    # Z = np.real(ifft(X*Y))
    # # z = ""
    # for i in Z:
    #     z+=str((int(i)))

    # return int(z)
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
    b = 2**20
    # val= fastMultLargeNums(a,a)
    val= fft_multiply(a,a)

    print(b)
    print(val)