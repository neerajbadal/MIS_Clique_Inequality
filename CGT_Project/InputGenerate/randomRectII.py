'''
Created on 11-Apr-2020

@author: Neeraj Badal
'''
'''
Created on 28-Mar-2020

@author: Neeraj Badal
'''
import random
from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.ticker import AutoLocator
from MaxCliqueRect import computeMaxClique
from MIS import computeMIS
from MIS import ApproxMIS
from MIS import greedyApproxMIS
import numpy as np
import numpy.lib.recfunctions as rfn
from anaconda_project.internal.conda_api import result
import pandas as pd
from matplotlib import rc
class MyLocator(AutoLocator):
    def view_limits(self, vmin, vmax):
        multiplier = 5.0
        vmin = multiplier * np.floor(vmin / multiplier)
        vmax = multiplier * np.ceil(vmax / multiplier)
        return vmin, vmax
if __name__ == "__main__":
    
    '''
    [#rects,clique,mis,approxMis,logn,g/logn,mis*cliq,approx*cliq]
    '''
     
    
    numberOfRectangles = 300
    planeXRange = [-30.0,30.0]
    planeYRange = [-30.0,30.0]
    
    widthRange = [4,30]
    heightRange = [4,10]
    
    result_array = []
    
    for nr_ in range(890,900,10):
        numberOfRectangles = nr_
        print("-----nr--",nr_)
        for j in range(0,1):
            print("-----nr--",nr_,".............",j)
            fig,ax = plt.subplots(nrows=1, ncols=2)
            plt.axes(ax[0])
            currentAxis = plt.gca()
            input_rectangles = []
            for i in range(0,numberOfRectangles):
                x_val = random.randrange(planeXRange[0]+widthRange[0],planeXRange[1]-widthRange[1])
                y_val = random.randrange(planeYRange[0]+heightRange[0],planeYRange[1]-heightRange[1])
                
                width_ = random.randint(widthRange[0],widthRange[1])
                height_ = random.randint(heightRange[0],heightRange[1])
                
                
    #             if x_val + width_ > planeXRange
                
    #             currentAxis.add_patch(Rectangle((x_val, y_val), width_, height_,
    #                               alpha=1, fill=None))
            
                tempRect = [y_val+height_,y_val,x_val,x_val+width_,i]
                input_rectangles.append(tempRect)
    #         ax.set_ylim([-60,60])
    #         ax.set_xlim([-60,60])
#             print(input_rectangles)
            
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
            print("clique completed ",maxCliqueForData)
            
            
            
            MISForData = greedyApproxMIS.prepareGreedyMIS(input_rectangles)
            print("MIS = ", MISForData[0])
            
            
            heuristicMIS_forData = ApproxMIS.heuristicMISI(input_rectangles)
            MISForData = heuristicMIS_forData 
            
#             plt.suptitle(" n = "+str(numberOfRectangles)+" Max clique(q) = "+str(maxCliqueForData[0])+" MIS(I) = "+str(MISForData[0])
#                       +" approx MIS = "+str(heuristicMIS_forData[0])
            
            result_array.append([nr_,maxCliqueForData[0],MISForData[0],heuristicMIS_forData[0],np.log2(nr_),MISForData[0]/np.log2(nr_),
                                 MISForData[0]*maxCliqueForData[0],heuristicMIS_forData[0]*maxCliqueForData[0]])
            
            
#     result_array = np.array(result_array)
#     print(result_array)
#     outDataFile = "D:/Mtech/FY/SEM2/Latex_Assignment/proj_out_greedy_approx.dat"
#     np.savetxt(outDataFile,result_array,delimiter='\t')
    exit(0)
        
#         mis_rectangles = input_rectangles[list(MISForData[1])]
#         
#         
#         
#         for i in range(0,len(mis_rectangles)):
#             x_val = mis_rectangles[i,2]
#             y_val = mis_rectangles[i,0]
#             
#             width_ = mis_rectangles[i,3] - mis_rectangles[i,2]
#             height_ = mis_rectangles[i,1] - mis_rectangles[i,0]
#     
#     
#             currentAxis.add_patch(Rectangle((x_val, y_val), width_, height_,
#                               alpha=0.4, edgecolor='black',facecolor='green'))
#             
#         
#         
#         for i in range(0,len(input_rectangles)):
#             x_val = input_rectangles[i,2]
#             y_val = input_rectangles[i,0]
#             
#             width_ = input_rectangles[i,3] - input_rectangles[i,2]
#             height_ = input_rectangles[i,1] - input_rectangles[i,0]
#     
#             
#             currentAxis.add_patch(Rectangle((x_val, y_val), width_, height_,
#                             alpha=1, edgecolor='black',fill=None))
#             if maxCliqueForData[1] is not None:
#                 circle_ = plt.Circle((maxCliqueForData[1][0]-0.3,maxCliqueForData[1][1]+0.3), 0.3, color='red')
#                 
#                 currentAxis.add_artist(circle_)
#             
#             currentAxis.annotate(str(i), (x_val, y_val), color='b', weight='bold', 
#                 fontsize=10, ha='center', va='center')
#         
#         plt.title("MIS brute force shaded, Clique shown as Red dot ",fontsize=16)
#         ax[0].xaxis.set_major_locator(MyLocator())
#         ax[0].yaxis.set_major_locator(MyLocator())
#         ax[0].autoscale()
#         
#         
#         plt.axes(ax[1])
#         currentAxis = plt.gca()
#         
#         
#         approx_rectangles = input_rectangles[list(heuristicMIS_forData[1])]
#         for i in range(0,len(approx_rectangles)):
#             x_val = approx_rectangles[i,2]
#             y_val = approx_rectangles[i,0]
#             
#             width_ = approx_rectangles[i,3] - approx_rectangles[i,2]
#             height_ = approx_rectangles[i,1] - approx_rectangles[i,0]
#     
#     
#             currentAxis.add_patch(Rectangle((x_val, y_val), width_, height_,
#                               alpha=0.1, edgecolor='black',facecolor='red'))
#         
#         
#         
#         
# #         input_rectangles = np.delete(input_rectangles,MISForData[1],axis=0)
# #         input_rectangles = np.delete(input_rectangles,heuristicMIS_forData[1],axis=0)
#         
#     
#         
#         for i in range(0,len(input_rectangles)):
#             x_val = input_rectangles[i,2]
#             y_val = input_rectangles[i,0]
#             
#             width_ = input_rectangles[i,3] - input_rectangles[i,2]
#             height_ = input_rectangles[i,1] - input_rectangles[i,0]
#     
#     
#             currentAxis.add_patch(Rectangle((x_val, y_val), width_, height_,
#                               alpha=1, edgecolor='black',fill=None))
#             
#             currentAxis.annotate(str(i), (x_val, y_val), color='b', weight='bold', 
#                 fontsize=10, ha='center', va='center')
#         
#         ax[1].xaxis.set_major_locator(MyLocator())
#         ax[1].yaxis.set_major_locator(MyLocator())
#         ax[1].autoscale()
#         
#         plt.title("MIS Approx. shaded "+
#                   " (I/logn) = "+'{:9.3f}'.format(MISForData[0]/np.log2(numberOfRectangles))
#                   ,fontsize=18)
#         
#         
#         plt.suptitle(" n = "+str(numberOfRectangles)+" Max clique(q) = "+str(maxCliqueForData[0])+" MIS(I) = "+str(MISForData[0])
#                   +" approx MIS = "+str(heuristicMIS_forData[0])
#                   ,fontsize=22)
#         plt.show()