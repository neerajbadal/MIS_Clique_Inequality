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
     
    
    numberOfRectangles = 100
    
    recs_ranges = np.arange(1,numberOfRectangles)
    quant = (np.log2(recs_ranges))*(recs_ranges-np.log2(recs_ranges))
    
#     plt.plot(recs_ranges,quant,marker='o',label='l')
#     plt.plot(recs_ranges,recs_ranges,marker='o',label='N')
#     plt.legend()
#     plt.show()
    
    
    widthRange = [30,40]
    heightRange = np.array([20,30])
    
    result_array = []
    outDataFile = "D:/Mtech/FY/SEM2/Latex_Assignment/proj_out_greedy_approx_v2_1.dat"
    
#     for nr_ in range(5,35):[5,6,7,8,9,10,11,12,13,14,15,19,22,23,24,25,26,27,28,29,30,31]
    for nr_ in [29,30,31]:
        numberOfRectangles = nr_
        print("-----nr--",nr_)
        for j in range(0,1):
            print("-----nr--",nr_,".............",j)
            fig,ax = plt.subplots(nrows=1, ncols=2)
            plt.axes(ax[0])
            currentAxis = plt.gca()
            planeXRange = np.array([1500.0,1560.0])
            planeYRange = np.array([1500.0,1560.0])
            input_rectangles = []
            
            groupSize  = np.log2(numberOfRectangles) - 1 
    
            totalGroups = numberOfRectangles / groupSize
            
            groupSize = int(groupSize)
            
            print(groupSize,".....",totalGroups)
            totalGroups = int(np.ceil(totalGroups))
            recs_covered = 0
            maxXVal = -3000
            maxYVal = -3000
            groupsToAddlist = np.arange(0,totalGroups).tolist()
            i = 0
#             for i in groupsToAddlist:
            while i < totalGroups:    
                
                
                if numberOfRectangles - recs_covered < groupSize:
                    recs_to_be_generated = numberOfRectangles - recs_covered
                else:
                    recs_to_be_generated = groupSize
                
                
                if i%2==0 and i!=0:
                    planeXRange[0] = maxXVal -20
                    planeXRange[1] = maxXVal + 40
#                     planeYRange[0] = maxYVal - 1
#                     planeYRange[1] = maxYVal + 10
#                     heightRange = [5,10]
                else:
                    planeXRange = planeXRange + 60
#                     heightRange = [20,30]
#                     planeYRange[0] = 1500
#                     planeYRange[1] = 1560

#                 planeXRange = planeXRange + 40
                planeYRange = planeYRange
                
                for j_ in range(0,recs_to_be_generated):
                    recs_covered += 1
                    
                    
#                     print(planeXRange)

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
                    
                    
        #             if x_val + width_ > planeXRange
                    
        #             currentAxis.add_patch(Rectangle((x_val, y_val), width_, height_,
        #                               alpha=1, fill=None))
                
                    tempRect = [y_val+height_,y_val,x_val,x_val+width_,recs_covered-1]
                    if maxXVal < x_val+width_:
                        maxXVal = x_val+width_
                    if maxYVal < y_val+height_:
                        maxYVal = y_val+height_
                    
                    input_rectangles.append(tempRect)
                
                '''here we wiil write new logic'''
                if (i == totalGroups-1) and (numberOfRectangles - recs_covered > 0):
                    print("inside change see**************")
                    stillRemaining = numberOfRectangles - recs_covered
                    groups_to_add = int(np.ceil(stillRemaining / groupSize))
                    totalGroups = totalGroups + groups_to_add
#                 newExtendListt = np.arange(totalGroups,totalGroups + groups_to_add).tolist()
#                 groupsToAddlist.extend(newExtendListt)
#                 print(groupsToAddlist)
                i+=1
                
                
                
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
             
            MISForData = MIS_MemoryEff.prepareMISDat(input_rectangles,totalGroups) 
            print("MIS = ", MISForData[0])
             
            MISForData_greedy = greedyApproxMIS.prepareGreedyMIS(input_rectangles)
            print("MIS = ", MISForData_greedy[0])
             
             
            heuristicMIS_forData = ApproxMIS.heuristicMISI(input_rectangles)
            
#             plt.suptitle(" n = "+str(numberOfRectangles)+" Max clique(q) = "+str(maxCliqueForData[0])+" MIS(I) = "+str(MISForData[0])+
#                          " approx MIS = "+str(heuristicMIS_forData[0])
            
#             result_array.append([nr_,maxCliqueForData[0],MISForData[0],heuristicMIS_forData[0],np.log2(nr_),MISForData[0]/np.log2(nr_),
#                                 MISForData[0]*maxCliqueForData[0],heuristicMIS_forData[0]*maxCliqueForData[0]])
            
            
            
            
            with open(outDataFile, "a") as myfile:
#                 myfile.write(str(nr_)+"\t"+str(recs_covered)+"\n")
                myfile.write(str(nr_)+"\t"+str(maxCliqueForData[0])+
                             "\t"+str(MISForData[0])+"\t"+str(MISForData_greedy[0])+"\t"+
                             str(heuristicMIS_forData[0])+"\t"+str(recs_covered)+"\n")
            
#     result_array = np.array(result_array)
#     print(result_array)
#     outDataFile = "D:/Mtech/FY/SEM2/Latex_Assignment/proj_out_greedy_approx.dat"
#     np.savetxt(outDataFile,result_array,delimiter='\t')
        
    exit(0)
         
                
         
         
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
#             plt.suptitle(" n = "+str(numberOfRectangles)+" Max clique(q) = "+str(maxCliqueForData[0])+" MIS(I) = "+str(MISForData_greedy[0])
#             +" approx MIS = "+str(heuristicMIS_forData[0]))
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