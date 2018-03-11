# -*- coding:utf-8 -*-
'''
Created on  
@author: yzw
'''

from numpy import random
import numpy as np
import matplotlib.pyplot as plt
from math import pi,sin
import copy
class Gas():
    def __init__(self,popsize,chrosize,xrangemin,xrangemax):
        self.popsize =popsize
        self.chrosize =chrosize
        self.xrangemin =xrangemin
        self.xrangemax =xrangemax
        self.crossrate =0.8
        self.mutationrate =0.01
    def initialpop(self):
        pop = random.randint(0,2,size =(self.popsize,self.chrosize))
        return pop
    def fun(self,x1):
        return x1*sin(10*pi*x1)+2.0
    def get_fitness(self,x):       
        fitness = []
        for x1 in x:
           fitness.append(self.fun(x1))
        return fitness         
    def selection(self,popsel,fitvalue):
        new_fitvalue = []
        totalfit = sum(fitvalue)
        accumulator = 0.0
        for val in fitvalue:
            new_val =(val*1.0/totalfit)            
            accumulator += new_val
            new_fitvalue.append(accumulator)            
        ms = []
        for i in xrange(self.popsize):
            ms.append(random.random()) 
        ms.sort()
        fitin = 0
        newin = 0
        newpop = popsel
        while newin < self.popsize:
            if(ms[newin] < new_fitvalue[fitin]):
                newpop[newin] = popsel[fitin]
                newin = newin + 1
            else:
                fitin = fitin + 1
        pop = newpop
                
        return pop
    
    def crossover(self,pop):
        for i in xrange(self.popsize-1):
            if(random.random()<self.crossrate):
                singpoint =random.randint(0,self.chrosize)
                temp1 = []
                temp2 = []
                temp1.extend(pop[i][0:singpoint])
                temp1.extend(pop[i+1][singpoint:self.chrosize])
                temp2.extend(pop[i+1][0:singpoint])
                temp2.extend(pop[i][singpoint:self.chrosize])
                pop[i]=temp1
                pop[i+1]=temp2

        return pop
    
    def mutation(self,pop):
        for i in xrange(self.popsize):
            if (random.random()< self.mutationrate):
                mpoint = random.randint(0,self.chrosize-1)
                if(pop[i][mpoint]==1):
                    pop[i][mpoint] = 0
                else:
                    pop[mpoint] =1

        return pop
    def elitism(self,pop,popbest,nextbestfit,fitbest):
        if nextbestfit-fitbest <0:           
            pop_worst =nextfitvalue.index(min(nextfitvalue))
            pop[pop_worst] = popbest
        return pop          
                                 
    def get_declist(self,chroms):
        step =(self.xrangemax - self.xrangemin)/float(2**self.chrosize-1)
        self.chroms_declist =[]
        for i in xrange(self.popsize):
            chrom_dec =self.xrangemin+step*self.chromtodec(chroms[i])  
            self.chroms_declist.append(chrom_dec)      
        return self.chroms_declist
    def chromtodec(self,chrom):
        m = 1
        r = 0
        for i in xrange(self.chrosize):
            r = r + m * chrom[i]
            m = m * 2
        return r

if __name__ == '__main__':
    generation = 100
    mainGas =Gas(100,10,-1,2)
    pop =mainGas.initialpop() 
    pop_best = []
    #average = []
    for i in xrange(generation): 
        declist =mainGas.get_declist(pop)
        fitvalue =mainGas.get_fitness(declist)
        popbest = pop[fitvalue.index(max(fitvalue))]
        popbest =copy.deepcopy(popbest)
        fitbest = max(fitvalue)
        pop_best.append(fitbest)
        #average.append(sum(fitvalue)/len(fitvalue))       
        ################################
        mainGas.selection(pop,fitvalue)  
        mainGas.crossover(pop)
        mainGas.mutation(pop)  
        ################################
        nextdeclist = mainGas.get_declist(pop)
        nextfitvalue =mainGas.get_fitness(nextdeclist)        
        nextbestfit = max(nextfitvalue) 
        ################################
        mainGas.elitism(pop,popbest,nextbestfit,fitbest)                        
    print max(pop_best)
    t = [x for x in xrange(generation)]
    s = pop_best
    plt.plot(t,s)
    plt.show()
    plt.close()