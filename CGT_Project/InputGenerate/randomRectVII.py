'''
Created on 09-May-2020

@author: Neeraj Badal
'''
'''
Created on 18-Apr-2020

@author: Neeraj Badal
'''
'''
Created on 12-Apr-2020

@author: Neeraj Badal
'''
'''
Created on 11-Apr-2020

@author: Neeraj Badal
'''
'''
Created on 28-Mar-2020

@author: Neeraj Badal
'''
import sys
sys.path.append('D:/workspace/CGT_Project/')
import random
from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.ticker import AutoLocator
from MaxCliqueRect import computeMaxClique
from MIS import computeMIS, MIS_MemoryEff
from MIS import ApproxMIS
from MIS import greedyApproxMIS,greedyMISII
import numpy as np
import numpy.lib.recfunctions as rfn
from anaconda_project.internal.conda_api import result
import pandas as pd
from multiprocessing import Pool
from matplotlib import rc
class MyLocator(AutoLocator):
    def view_limits(self, vmin, vmax):
        multiplier = 5.0
        vmin = multiplier * np.floor(vmin / multiplier)
        vmax = multiplier * np.ceil(vmax / multiplier)
        return vmin, vmax
def computeVals(instanceVal):
    outDataFile = "D:/Mtech/FY/SEM2/Latex_Assignment/proj_out_greedy_approx_v4_"+\
                        str(instanceVal+1)+".dat"
    widthRange = [10,30]
    heightRange = np.array([10,25])
    for nr_ in range(7000,9001,200):
            numberOfRectangles = nr_
            print("-----nr--",nr_)
            print("-----nr--",nr_,".............",instanceVal)
            
            sideLength = (np.ceil(np.sqrt(180*nr_)))
            planeXRange = np.array([1500.0,1500.0+sideLength])
            planeYRange = np.array([1500.0,1500.0+sideLength])
            input_rectangles = []
            for i in range(0,numberOfRectangles):
                
                a = planeXRange[0]+widthRange[0]
                b = planeXRange[1]-widthRange[1]
                    
                if a < b:
                    x_val = random.randrange(a,b)
                else:
                    x_val = random.randrange(b,a)
                
                a = planeYRange[0]+heightRange[0]
                b = planeYRange[1]-heightRange[1]
                
                if a < b:
                    y_val = random.randrange(a,b)
                else:
                    y_val = random.randrange(b,a)
                
                
                width_ = random.randint(widthRange[0],widthRange[1])
                height_ = random.randint(heightRange[0],heightRange[1])
                
                
                tempRect = [y_val+height_,y_val,x_val,x_val+width_,i]
                input_rectangles.append(tempRect)
                        
            input_rectangles = np.array(input_rectangles)
            ''' partition R into y-intervals '''
            y_intervals = []
            for i_ in range(0,len(input_rectangles)):
                y_intervals.append([input_rectangles[i_,0],input_rectangles[i_,2],input_rectangles[i_,3],1,i_])
                y_intervals.append([input_rectangles[i_,1],input_rectangles[i_,2],input_rectangles[i_,3],2,i_])
                
            y_intervals = np.array(y_intervals)
#             print(y_intervals)
            
            names=('a','b','c','d','e')
            dt = np.dtype([(n,np.float) for n in names])
            y_intervals = np.array(y_intervals)
        
            y_intervals = rfn.unstructured_to_structured(y_intervals, dt)
            
            
            maxCliqueForData = computeMaxClique.computeMaxClique(y_intervals)
            print(maxCliqueForData)
            
#             MISForData = MIS_MemoryEff.prepareMISDat(input_rectangles,totalGroups) 
#             print("MIS = ", MISForData[0])
            
            MISForData_greedy = greedyMISII.prepareGreedyMIS(input_rectangles)
            print("MIS = ", MISForData_greedy[0])
            
            
            heuristicMIS_forData = ApproxMIS.heuristicMISI(input_rectangles)
            
            
            with open(outDataFile, "a") as myfile:
                myfile.write(str(nr_)+"\t"+str(maxCliqueForData[0])+
                             "\t"+str(MISForData_greedy[0])+"\t"+
                             str(heuristicMIS_forData[0])+"\n")
    
    

if __name__ == "__main__":
    
    '''
    [#rects,clique,mis,approxMis,logn,g/logn,mis*cliq,approx*cliq]
    '''
     
    
    widthRange = [10,30]
    heightRange = np.array([10,25])
    
    pool = Pool(3)
    L = pool.map(computeVals,range(0,10))
    pool.close()
    pool.join()

    
    
                
    exit(0)