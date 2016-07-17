import numpy as np 
from math import e
x = np.array([[1,0.697,0.460],
             [2,0.774,0.376],
             [3,0.634,0.264],
             [4,0.608,0.318],
             [5,0.556,0.215],
             [6,0.403,0.237],
             [7,0.481,0.149],
             [8,0.437,0.211],
             [9,0.666,0.091],
             [10,0.243,0.267],
             [11,0.245,0.057],
             [12,0.343,0.099],
             [13,0.639,0.161],
             [14,0.657,0.198],
             [15,0.360,0.370],
             [16,0.593,0.042],
             [17,0.719,0.103]])

y = np.array([1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0])

In = np.array([[0,0]])


V = np.random.random((2,4))

N_in = np.array([0,0,0,0])

N_Th = np.random.random(size=4)

N_out = np.array([0,0,0,0])

W = np.random.random(size=4)


O_Th = 0.3

E = np.array([0,0,0,0])

n1 = 0.5
n2 = 0.3
#Sigmod Function
def Sigmod(s):
    S = np.random.random(size=4)
    for j in range(4):
        t = -s[j]
        ac = e**(-s[j])
        S[j] = 1.0/(1+e**(-s[j]))
    return S
if __name__ == '__main__':
    while(True):
        #calculate each neuron input
        for h in range(17):
            In = x[h,1:3]
           
            N_in = np.dot(In,V)
    
        #calculate each neuron output
            N_out = Sigmod(N_in-N_Th)
             
        #calculate output layer input
    
            Out_Layer_input = (N_out*W).sum()
    
        #calculate output
            Out=1.0/(1+e**(-(Out_Layer_input-O_Th)))
    
        #calculate G_i
    
            G=Out*(1-Out)*(y[h]-Out)
    
        #caluate E_i
            E = N_out*(1-N_out)*W*G
    
        #caluate step update study speed n1 n2
    
            D_W=n1*G*N_out
            
            D_OTH = -n1*G
            In.shape=(1,2)
            InT = np.transpose(In)
            D_V = n2*InT*E 
            
            D_N_TH1 = -n2*E
    
        #update parameter
            V = V+D_V
            
            N_Th = N_Th + D_N_TH1
    
            W = W + D_W
    
            O_Th = O_Th + D_OTH
            
            print str(h)+str(Out)+str(y[h])
            
    print V
    print N_Th
    print W
    print O_Th
