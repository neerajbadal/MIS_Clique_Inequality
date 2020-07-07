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
     
    
    numberOfRectangles = 100
    
    recs_ranges = np.arange(1,numberOfRectangles)
    quant = (np.log2(recs_ranges))*(recs_ranges-np.log2(recs_ranges))
    
#     plt.plot(recs_ranges,quant,marker='o',label='l')
#     plt.plot(recs_ranges,recs_ranges,marker='o',label='N')
#     plt.legend()
#     plt.show()
    
    
    widthRange = [5,20]
    heightRange = np.array([5,15])
    
    result_array = []
    outDataFile = "D:/Mtech/FY/SEM2/Latex_Assignment/proj_out_greedy_approx_v0_3.dat"
    for j in range(0,30):
        for nr_ in range(5,25,1):
            numberOfRectangles = nr_
            print("-----nr--",nr_)
    #         for j in range(0,1):
            print("-----nr--",nr_,".............",j)
#             fig,ax = plt.subplots(nrows=1, ncols=2)
#             plt.axes(ax[0])
#             currentAxis = plt.gca()
            
            sideLength = (np.ceil(np.sqrt(180*nr_)))
#             planeXRange = np.array([1500.0,1500.0+sideLength])
#             planeYRange = np.array([1500.0,1500.0+sideLength])
            planeXRange = np.array([1500.0,1860.0])
            planeYRange = np.array([1500.0,1860.0])
            input_rectangles = []
            for i in range(0,numberOfRectangles):
#                 x_val = random.randrange(planeXRange[0]+widthRange[0],planeXRange[1]-widthRange[1])
#                 y_val = random.randrange(planeYRange[0]+heightRange[0],planeYRange[1]-heightRange[1])
                
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
                
                
                perturb_ = (float(i+1) / numberOfRectangles) * random.randint(2,10) 
                
                width_ = random.randint(widthRange[0],widthRange[1]) + perturb_ 
                height_ = random.randint(heightRange[0],heightRange[1]) + perturb_
                
                
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
            
            MISForData = computeMIS.prepareMISDat(input_rectangles) 
            print("MIS = ", MISForData[0])
            
            MISForData_greedy = greedyMISII.prepareGreedyMIS(input_rectangles)
            print("MIS = ", MISForData_greedy[0])
            
            
            heuristicMIS_forData = ApproxMIS.heuristicMISI(input_rectangles)
            
#             plt.suptitle(" n = "+str(numberOfRectangles)+" Max clique(q) = "+str(maxCliqueForData[0])+" MIS(I) = "+str(MISForData[0])+
#                          " approx MIS = "+str(heuristicMIS_forData[0])+" greedy "+
#                                               str(MISForData_greedy[0]))
            
#             result_array.append([nr_,maxCliqueForData[0],MISForData[0],heuristicMIS_forData[0],np.log2(nr_),MISForData[0]/np.log2(nr_),
#                                 MISForData[0]*maxCliqueForData[0],heuristicMIS_forData[0]*maxCliqueForData[0]])
            
            
#             with open(outDataFile, "a") as myfile:
#                 myfile.write(str(nr_)+"\t"+str(maxCliqueForData[0])+
#                              "\t"+str(MISForData_greedy[0])+"\t"+
#                              str(heuristicMIS_forData[0])+"\n")
            
            
            with open(outDataFile, "a") as myfile:
                myfile.write(str(nr_)+"\t"+str(maxCliqueForData[0])+
                             "\t"+str(MISForData[0])+"\t"+
                             str(heuristicMIS_forData[0])+
                             "\t"+str(MISForData_greedy[0])+"\n")
            
#     result_array = np.array(result_array)
#     print(result_array)
#     outDataFile = "D:/Mtech/FY/SEM2/Latex_Assignment/proj_out_greedy_approx.dat"
#     np.savetxt(outDataFile,result_array,delimiter='\t')
         
#     exit(0)
#             for i in range(0,len(input_rectangles)):
#                 x_val = input_rectangles[i,2]
#                 y_val = input_rectangles[i,0]
#                     
#                 width_ = input_rectangles[i,3] - input_rectangles[i,2]
#                 height_ = input_rectangles[i,1] - input_rectangles[i,0]
#             
#                     
#                 currentAxis.add_patch(Rectangle((x_val, y_val), width_, height_,
#                                 alpha=1, edgecolor='black',fill=None))
#                     
#                 currentAxis.annotate(str(i), (x_val, y_val), color='b', weight='bold', 
#                     fontsize=10, ha='center', va='center')
#             
#             plt.title("MIS brute force shaded, Clique shown as Red dot ",fontsize=16)
#             ax[0].xaxis.set_major_locator(MyLocator())
#             ax[0].yaxis.set_major_locator(MyLocator())
#             ax[0].autoscale()
# #             plt.suptitle(" n = "+str(numberOfRectangles)+" Max clique(q) = "+str(maxCliqueForData[0])+" MIS(I) = "+str(MISForData_greedy[0])
# #             +" approx MIS = "+str(heuristicMIS_forData[0]))
#             plt.show()
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