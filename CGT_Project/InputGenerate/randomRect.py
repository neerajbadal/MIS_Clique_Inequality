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
#     rc('text', usetex=True)
#     rc('font', family='serif')
    
    outDataFile = "D:/Mtech/FY/SEM2/Latex_Assignment/proj_out.dat"
    dataArray = np.loadtxt(outDataFile) 
    print(dataArray.shape)
    
#     plt.scatter(dataArray[300:330,2],dataArray[300:330,3],marker='o',label='MIS')
#     plt.plot(dataArray[:,0]/dataArray[:,6],marker='o',label='Approx-MIS')
#     plt.legend()
#     plt.show()
    
    
    tempMul = dataArray[:,1] * dataArray[:,2]
    tempMul =  dataArray[:,0] / tempMul
    
    plt.plot(np.arange(0,len(tempMul)),tempMul,marker='o')
    plt.show()
    exit(0)
    
    da_pd = pd.DataFrame(data=dataArray,index=dataArray[:,0])
    print(da_pd.groupby(0)[1].median())
    print(da_pd.groupby(0).groups.keys())
    
    cons_val = da_pd[0]/da_pd[6].values
    mis_by_approx = da_pd[2]/da_pd[1].values
    da_pd = da_pd.assign(e=cons_val)
    da_pd = da_pd.assign(f=mis_by_approx)
    
    
#     print(da_pd)
#     print(cons_val)
#     exit(0)
    
    nr_clique = np.array(list(da_pd.groupby(0)[1].max())) 
    nr_vals = list(da_pd.groupby(0).groups.keys())
    nr_mis = np.array(list(da_pd.groupby(0)[2].mean()))
    nr_approx_mis = np.array(list(da_pd.groupby(0)[3].mean())) 
    nr_approx_ratio = np.array(list(da_pd.groupby(0)[5].mean()))
    nr_mis_cliq_min =  np.array(list(da_pd.groupby(0)[6].min()))
    nr_mis_cliq_mean =  np.array(list(da_pd.groupby(0)[6].mean()))
    nr_mis_cliq_max =  np.array(list(da_pd.groupby(0)[6].max()))
    
    nr_ag_g = np.array(list(da_pd.groupby(0)['f'].median()))
    
    
    nr_i = 5
    print(da_pd)
#     for nr_instances in range(0,len(dataArray),30):
#         plt.plot(np.array(list(da_pd['e'])),marker='o')
#         print(nr_instances,nr_i)
#         if nr_instances != len(dataArray):
#             print(nr_instances)
#             start_index = nr_instances
#             end_index =nr_instances + 30
#             const_dat = np.array(list(da_pd.iloc[start_index:end_index]['e']))
#             plt.plot(const_dat,marker='o',label=r"$|\mathcal{R}| = $"+str(nr_i))
#         nr_i += 1
#     plt.plot(np.array(list(da_pd['e'])),marker='o')
# #     plt.plot(np.array(list(da_pd.groupby(0)['e'].mean())),marker='o')
#     plt.xlabel("instance index",fontsize=18)
#     plt.ylabel(r"$\frac{|\mathcal{R}|}{\omega(\mathcal{R}) * \gamma(\mathcal{R})}$",fontsize=20)
#     plt.title(r"$\frac{|\mathcal{R}|}{\omega(\mathcal{R}) * \gamma(\mathcal{R})}$ for $|\mathcal{R}| \in [5,25]$ 30 instances each",
#               fontsize=22)
#     ax = plt.gca()
#     ax.tick_params(axis = 'both', which = 'major', labelsize = 18)
#     ax.tick_params(axis = 'both', which = 'minor', labelsize = 18)
#     plt.show()
#     exit(0)
#     print(np.array(list(da_pd[da_pd[0]==20][6])))
#     plt.plot(np.array(list(da_pd[da_pd[0]==15][6])),marker='o')
#     plt.xlabel("instance index",fontsize=18)
#     plt.ylabel(r"$\omega(\mathcal{R}) * \gamma(\mathcal{R})$",fontsize=20)
#     plt.title(r"$\omega(\mathcal{R}) * \gamma(\mathcal{R})$ for $|\mathcal{R}|$ = 15",
#               fontsize=22)
#     ax = plt.gca()
#     ax.tick_params(axis = 'both', which = 'major', labelsize = 18)
#     ax.tick_params(axis = 'both', which = 'minor', labelsize = 18)
#     plt.show()
    
    
    
    
#     plt.plot(nr_vals,nr_mis_cliq_min,marker='o',label='Min')
#     plt.plot(nr_vals,nr_mis_cliq_mean,marker='o',label='Mean')
#     plt.plot(nr_vals,nr_mis_cliq_max,marker='o',label='Max')
#     plt.xlabel("$|\mathcal{R}|$",fontsize=18)
#     plt.ylabel(r"$\omega(\mathcal{R}) * \gamma(\mathcal{R})$",fontsize=20)
#     plt.title(r"$\omega(\mathcal{R}) * \gamma(\mathcal{R})$ w.r.t $|\mathcal{R}|$",
#               fontsize=22)
#     ax = plt.gca()
#     ax.tick_params(axis = 'both', which = 'major', labelsize = 18)
#     ax.tick_params(axis = 'both', which = 'minor', labelsize = 18)
    
    
#     plt.scatter(np.array(list(da_pd[da_pd[0]==18][1])),np.array(list(da_pd[da_pd[0]==18][2])),marker='o',label=r"$\gamma(\mathcal{R})$")
#     plt.plot(np.array(list(da_pd['f'])),marker='o',label=r"approx $\gamma(\mathcal{R})$")
#     plt.plot(1/np.log2(np.array(list(da_pd[0]))),marker='o',label=r"$1/ \log n$")
    
#     plt.scatter(np.arange(0,len(dataArray)),np.array(list(da_pd[2])),marker='o',label=r"approx-$\gamma(\mathcal{R})$")
#     plt.plot(nr_vals,nr_mis_cliq_min,marker='o',label='Min')
    plt.plot(nr_vals,nr_ag_g,marker='o',label='Mean')
    plt.plot(nr_vals,1/np.log2(nr_vals),marker='o',label=r"$1/ \log n$")
#     plt.plot(nr_vals,nr_mis_cliq_max,marker='o',label='Max')
    plt.xlabel(r"$|\mathcal{R}|$",fontsize=18)
    plt.title(r"approx $ \gamma(\mathcal{R}) $ by $\gamma(\mathcal{R})$ aggregated",
              fontsize=22)
    ax = plt.gca()
    ax.tick_params(axis = 'both', which = 'major', labelsize = 18)
    ax.tick_params(axis = 'both', which = 'minor', labelsize = 18)
    plt.legend()
    
    
#     plt.plot(nr_vals,nr_mis,marker='o',label='MIS')
#     plt.plot(nr_clique,nr_mis,marker='o',label='MIS')
#     plt.plot(nr_vals,nr_approx_ratio,marker='o',label='MIS')
#     plt.plot(nr_vals,np.log2(nr_vals),marker='o',label='log-fit')
#     plt.legend()
    plt.show()
    
    
    exit(0)
    
    
    numberOfRectangles = 5
    planeXRange = [-30.0,30.0]
    planeYRange = [-30.0,30.0]
    
    widthRange = [4,30]
    heightRange = [4,10]
    
    result_array = []
    
    for nr_ in range(5,26):
        numberOfRectangles = nr_
        print("-----nr--",nr_)
        for j in range(0,30):
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
            print(input_rectangles)
            
            input_rectangles = np.array(input_rectangles)
            ''' partition R into y-intervals '''
            y_intervals = []
            for i_ in range(0,len(input_rectangles)):
                y_intervals.append([input_rectangles[i_,0],input_rectangles[i_,2],input_rectangles[i_,3],1,i_])
                y_intervals.append([input_rectangles[i_,1],input_rectangles[i_,2],input_rectangles[i_,3],2,i_])
                
            y_intervals = np.array(y_intervals)
            print(y_intervals)
            
            names=('a','b','c','d','e')
            dt = np.dtype([(n,np.float) for n in names])
            y_intervals = np.array(y_intervals)
        
            y_intervals = rfn.unstructured_to_structured(y_intervals, dt)
            
            
            maxCliqueForData = computeMaxClique.computeMaxClique(y_intervals)
            print(maxCliqueForData)
            
            MISForData = computeMIS.prepareMISDat(input_rectangles) 
            print("MIS = ", MISForData[0])
            
            heuristicMIS_forData = ApproxMIS.heuristicMISI(input_rectangles)
            
#             plt.suptitle(" n = "+str(numberOfRectangles)+" Max clique(q) = "+str(maxCliqueForData[0])+" MIS(I) = "+str(MISForData[0])
#                       +" approx MIS = "+str(heuristicMIS_forData[0])
            
            result_array.append([nr_,maxCliqueForData[0],MISForData[0],heuristicMIS_forData[0],np.log2(nr_),MISForData[0]/np.log2(nr_),
                                 MISForData[0]*maxCliqueForData[0],heuristicMIS_forData[0]*maxCliqueForData[0]])
            
            
    result_array = np.array(result_array)
    print(result_array)
    outDataFile = "D:/Mtech/FY/SEM2/Latex_Assignment/proj_out.dat"
    np.savetxt(outDataFile,result_array,delimiter='\t')
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