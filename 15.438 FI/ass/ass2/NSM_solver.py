# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 22:51:59 2021

@author: Songhao
"""
import numpy as np
import matplotlib.pyplot as plt
def evaluate(T,theta_0,theta_1,theta_2,lam):
    return theta_0 + (theta_1+theta_2)* (1-np.exp(-T/lam)) / (T/lam) - theta_2*np.exp(-T/lam)

def num_grad(var,T,theta_0,theta_1,theta_2,lam,eps = 0.001):
    if var == 'theta_0':
        return (evaluate(T,(1+eps)*theta_0,theta_1,theta_2,lam) - evaluate(T,(1-eps)*theta_0,theta_1,theta_2,lam)) / (2*eps*theta_0)
    elif var == 'theta_1':
        return (evaluate(T,theta_0,(1+eps)*theta_1,theta_2,lam) - evaluate(T,theta_0,(1-eps)*theta_1,theta_2,lam)) / (2*eps*theta_1)
    elif var == 'theta_2':
        return (evaluate(T,theta_0,theta_1,(1+eps)*theta_2,lam) - evaluate(T,theta_0,theta_1,(1-eps)*theta_2,lam)) / (2*eps*theta_2)
    elif var == 'lam':
        return (evaluate(T,theta_0,theta_1,theta_2,(1+eps)*lam) - evaluate(T,theta_0,theta_1,theta_2,(1-eps)*lam)) / (2*eps*lam)


def solver(T,r):
    theta_0, theta_1, theta_2, lam = 0.068858693,-0.06155679,-0.045504313,1.902166121
    #theta_0, theta_1, theta_2, lam = 0.003803082, 3E-5,0.161234489,9.373235454
    
    for t in range(10000):
        pred = np.zeros(len(T))
        grad_theta_0 = np.zeros(len(T))
        grad_theta_1 = np.zeros(len(T))
        grad_theta_2 = np.zeros(len(T))
        grad_lam = np.zeros(len(T))
        
        for i in range(len(T)):
            pred[i] = evaluate(T[i],theta_0,theta_1,theta_2,lam)
            grad_theta_0[i] = num_grad("theta_0", T[i], theta_0, theta_1, theta_2, lam)
            grad_theta_1[i] = num_grad("theta_1", T[i], theta_0, theta_1, theta_2, lam)
            grad_theta_2[i] = num_grad("theta_2", T[i], theta_0, theta_1, theta_2, lam)
            grad_lam[i]     = num_grad("lam", T[i], theta_0, theta_1, theta_2, lam)
        
        MSE = np.sum(np.square(pred - r))
        if t % 1000 == 0:
            print('iteration: ' + str(t) + '| MSE: ' + str(MSE))
        theta_0 = theta_0 - 0.001 * ((pred - r) * grad_theta_0).sum()
        theta_1 = theta_1 - 0.001 * ((pred - r) * grad_theta_1).sum()
        theta_2 = theta_0 - 0.001 * ((pred - r) * grad_theta_2).sum()
        lam     = lam     - 0.001 * ((pred - r) * grad_lam).sum()
    
    
    return theta_0,theta_1,theta_2,lam

T = np.array([1,2,3,4,5,6,7,8,9,10,15,20,25])
r = np.array([1.2443,1.8727,2.4110,2.9665,3.4454,3.8557,4.1996,4.4677,4.6528,4.7107,5.7160,5.9517,5.9315])/100


result = [0.068858693,-0.06155679,-0.045504313,1.902166121]
geng_result = [0.003803082,3E-05,0.161234489,9.373235454]
pred = np.zeros(len(T))
init = np.zeros(len(T))
for i in range(13):
    pred[i] = evaluate(T[i],result[0],result[1],result[2],result[3])

print(np.sum(np.square(pred - r)))


#%%
plt.plot(T,r,label = 'real')
plt.plot(T,pred,label = 'pred')

plt.legend()
plt.show()