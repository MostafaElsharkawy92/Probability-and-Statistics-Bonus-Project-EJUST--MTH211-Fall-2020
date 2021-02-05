# -*- coding: utf-8 -*-
"""
"""
from numpy import random , std
from math import inf , sqrt
import matplotlib.pyplot as plt

def crash(n):
    data=[]
    for i in range (n):
        t=0
        fail=0
        t_fail=sorted([ random.exponential(30),random.exponential(30)])## generate failure times and sort them 
        t_repair=inf
        
        while True:
            if t_fail[0]<t_repair: ## if a machine failed before the next repair time 
                t=t_fail[0]
                fail+=1
                t_fail[0]=t+random.exponential(30)
                t_fail=sorted(t_fail)
                
                if fail==3 :
                    break ## 3 machines failed so the system crashed 
                
            
                elif fail==1:
                    t_repair=t+random.normal(6,0.5)   ## only one car failed so we generate the next repair time
            
            if t_repair<=t_fail[0]:  ## if a machine is repaired before the next fail time
                t=t_repair
                fail-=1
                if fail==1:
                    t_repair=t+random.normal(6,0.5) 
                
                elif fail==0:
                    t_repair=inf
            
        data.append(t)
    x_bar=sum(data)/n
    s=std(data)
    print(x_bar-1.96*s/sqrt(n),"<= E(T) <=",x_bar+1.96*s/sqrt(n)) ## at Confidence interval 95% ,Z(0.025)=1.96
    plt.hist(data,bins=100, density=True)
    
crash(1000000)
