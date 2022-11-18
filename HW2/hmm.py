import numpy as np
import string
import time

class HMM:
    def __init__(self, A, B, pi):
        self.A = A
        self.B = B
        self.pi = pi
        self.N = len(pi)
        self.dic = list(string.ascii_uppercase)[:self.N]

        
    def baum_welch(self, observations):
        N = self.N
        alpha = self.forward(observations)[0]
        beta = self.backward(observations)[0]

        T = len(observations)

        xi = np.zeros((T,N,N),dtype='double')
        gamma = np.zeros((T,N),dtype='double')

        for t in range(T):
            for i in range(N):
                gamma[t][i] = (alpha[t][i]*beta[t][i])/sum((alpha[t][k]*beta[t][k] for k in range(N)))
                for j in range(N):
                    symbol_index = self.dic.index(observations[t])
                    xi[t][i][j] = (alpha[t][i]*self.A[i][j]*self.B[symbol_index][j]*beta[t+1][j])/sum(
                        (alpha[t][k]*beta[t][k]for k in range(N)))

        new_pi = gamma[0]

        new_A = np.zeros((N,N,2),dtype='double')
        for i in range(N):
            for j in range(N):
                new_A[i][j] = (sum((xi[t][i][j] for t in range(T))),sum((gamma[t][i] for t in range(T))))

        new_B = np.zeros((N,N,2),dtype='double')
        for i in range(N):
            for j in range(N):
                sum1 = 0
                sum2 = 0
                for t in range(T):
                    sum2 += gamma[t][j]
                    if observations[t] == self.dic[i]:
                        sum1 += gamma[t][j]
                new_B[i][j] = (sum1,sum2)
        return new_A, new_B, new_pi
    
    
    def forward(self, observation):
        N = self.N
        T = len(observation)

        alpha = np.zeros((T+1,N),dtype='double')
        alpha[0] = self.pi

        for i in range(T):
            for j in range(N):
                symbol_index = self.dic.index(observation[i])
                s = sum([alpha[i][k]*self.A[k][j] for k in range(N)])
                alpha[i+1][j] = s*self.B[symbol_index][j]    
                
        return alpha,sum(alpha[-1])
    
    
    def backward(self, observation):
        N = self.N
        T = len(observation)

        beta = np.zeros((T+1,N),dtype='double')
        beta[T] = np.ones(N,dtype='double')

        for i in range(T,0,-1):
            for j in range(N):
                symbol_index = self.dic.index(observation[i-1])
                beta[i-1][j] = sum(self.A[j][k]*self.B[symbol_index][k]*beta[i][k] for k in range(N))

        return beta,sum((self.pi[i]*beta[0][i] for i in range(N)))

    def train_model(self, data):
        N = self.N
        d_pi = np.zeros(N, dtype='double')
        d_A = np.zeros((N,N,2), dtype='double')
        d_B = np.zeros((N,N,2), dtype='double')

        for line in data:
            d = self.baum_welch(line)
            d_A += d[0]
            d_B += d[1]
            d_pi += d[2]

        new_pi = d_pi/len(data)
        new_A = np.zeros((N,N), dtype='double')
        new_B = np.zeros((N,N), dtype='double')

        for k in range(N):
            for j in range(N): 
                new_A[k][j] = d_A[k][j][0]/d_A[k][j][1]
                new_B[k][j] = d_B[k][j][0]/d_B[k][j][1]
        
        self.A = new_A
        self.B = new_B
        self.pi = new_pi
