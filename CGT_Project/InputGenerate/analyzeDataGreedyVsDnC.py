'''
Created on 20-Apr-2020

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
    
#     outDataFile = "D:/Mtech/FY/SEM2/Latex_Assignment/proj_out_greedy_approx_v3.dat"
    outDataFile = "D:/Mtech/FY/SEM2/Latex_Assignment/rect_greedy_dnc.dat"
#     outDataFile ="D:/Mtech/FY/SEM2/Latex_Assignment/proj_out_greedy_approx_v12.dat"
    dataArray = np.loadtxt(outDataFile) 
    print(dataArray.shape)
#     print(dataArray)
    
    
#     plt.scatter(dataArray[300:330,2],dataArray[300:330,3],marker='o',label='MIS')
#     plt.plot(dataArray[:,0]/dataArray[:,6],marker='o',label='Approx-MIS')
#     plt.legend()
#     plt.show()
    
    
#     tempMul = dataArray[:,1] * dataArray[:,2]
    
    
#     plt.plot(dataArray[:,0],tempMul,marker='o')
# #     plt.plot(np.array(list(da_pd.groupby(0)['e'].mean())),marker='o')
#     plt.xlabel(r"$|\mathcal{R}|$",fontsize=18)
#     plt.ylabel(r"$\omega(\mathcal{R}) * \gamma(\mathcal{R})$",fontsize=20)
#     plt.title(r"$\omega(\mathcal{R}) * \gamma(\mathcal{R})$ for $|\mathcal{R}| \in [5,32]$",
#               fontsize=22,y=1.01)
#     ax = plt.gca()
#     ax.tick_params(axis = 'both', which = 'major', labelsize = 18)
#     ax.tick_params(axis = 'both', which = 'minor', labelsize = 18)
#     plt.show()
#     
#     
#     tempMul =  dataArray[:,0] / tempMul
#     plt.plot(dataArray[:,0],tempMul,marker='o')
# #     plt.plot(np.array(list(da_pd.groupby(0)['e'].mean())),marker='o')
#     plt.xlabel(r"$|\mathcal{R}|$",fontsize=18)
#     plt.ylabel(r"$\frac{|\mathcal{R}|}{\omega(\mathcal{R}) * \gamma(\mathcal{R})}$",fontsize=20)
#     plt.title(r"$\frac{|\mathcal{R}|}{\omega(\mathcal{R}) * \gamma(\mathcal{R})}$ for $|\mathcal{R}| \in [5,32]$",
#               fontsize=22,y=1.01)
#     ax = plt.gca()
#     ax.tick_params(axis = 'both', which = 'major', labelsize = 18)
#     ax.tick_params(axis = 'both', which = 'minor', labelsize = 18)
#     plt.show()
    
    da_pd = pd.DataFrame(data=dataArray,index=dataArray[:,0])
#     print(da_pd.groupby(0)[1].median())
    
    da_pd.sort_index(inplace=True)
    
#     plt.plot(da_pd[0],da_pd[2],marker='+',label=r'Greedy $\gamma(\mathcal{R})$')
#     plt.plot(da_pd[0],da_pd[3],marker='*',label=r'DnC $\gamma(\mathcal{R})$')
    plt.plot(da_pd[0],da_pd[1]*da_pd[2],marker='+',label=r'Greedy  $\omega(\mathcal{R})$*$\gamma(\mathcal{R})$')
    plt.plot(da_pd[0],da_pd[1]*da_pd[3],marker='*',label=r'DnC  $\omega(\mathcal{R})$*$\gamma(\mathcal{R})$')
    plt.xlabel(r"$|\mathcal{R}|$",fontsize=18)
    plt.ylabel(r"$\omega(\mathcal{R})$*$\gamma(\mathcal{R})$",fontsize=20)
    plt.title(r"$\omega(\mathcal{R})$*$\gamma(\mathcal{R})$ for $|\mathcal{R}| \in [10,9000]$ from random inputs",
              fontsize=22,y=1.01)
    ax = plt.gca()
    ax.tick_params(axis = 'both', which = 'major', labelsize = 18)
    ax.tick_params(axis = 'both', which = 'minor', labelsize = 18)
    plt.legend()
    plt.show()
       
    exit(0)

    cons_val = da_pd[1]*da_pd[2].values
    da_pd = da_pd.assign(e=cons_val)
    
    cons_val = da_pd[1]*da_pd[3].values
    da_pd = da_pd.assign(f=cons_val)
    
    da_pd = da_pd.reset_index()
    
    idx_ = da_pd.groupby(0)['e'].idxmin()
    
    
    
    pd_greedy = da_pd.loc[idx_]
    print(pd_greedy[:50])
#     exit(0)
#     cons_val = new_pd[1]*new_pd[2].values
#     cons_val =  new_pd[0] / new_pd['e'] 
#     new_pd = new_pd.assign(f=cons_val)
    
    idx_ = da_pd.groupby(0)['f'].idxmin()
    
    pd_dnc = da_pd.loc[idx_]
    
    cons_val =  pd_greedy[0] / pd_greedy['e'] 
    pd_greedy = pd_greedy.assign(c=cons_val)

    cons_val =  pd_dnc[0] / pd_dnc['f'] 
    pd_dnc = pd_dnc.assign(c=cons_val)
    
    plt.plot(pd_greedy[0],pd_greedy['c'],marker='o',label='greedy')
    plt.plot(pd_greedy[0],pd_dnc['c'],marker='o',label='DnC')
    plt.xlabel(r"$|\mathcal{R}|$",fontsize=18)
    plt.ylabel(r"$\frac{|\mathcal{R}|}{\omega(\mathcal{R}) * \gamma(\mathcal{R})}$",fontsize=20)
    plt.title(r"(Greedy vs DnC MIS) maximum $\frac{|\mathcal{R}|}{\omega(\mathcal{R}) * \gamma(\mathcal{R})}$ for $|\mathcal{R}| \in [10,9000]$ from random inputs"+
               "",
              fontsize=22,y=1.01)
    ax = plt.gca()
    ax.tick_params(axis = 'both', which = 'major', labelsize = 18)
    ax.tick_params(axis = 'both', which = 'minor', labelsize = 18)
    plt.legend()
    plt.show()
    
    
    exit(0)
#     plt.plot(new_pd[0],new_pd[2],marker='o',label='Greedy-MIS')
#     plt.plot(new_pd[0],new_pd[3],marker='o',label='DnC-MIS')
    
    plt.plot(new_pd[0],new_pd['f'],marker='o')
    plt.xlabel(r"$|\mathcal{R}|$",fontsize=18)
    plt.ylabel(r"$\frac{|\mathcal{R}|}{\omega(\mathcal{R}) * \gamma(\mathcal{R})}$",fontsize=20)
    plt.title(r"maximum $\frac{|\mathcal{R}|}{\omega(\mathcal{R}) * \gamma(\mathcal{R})}$ for $|\mathcal{R}| \in [5,24]$ from random inputs",
              fontsize=22,y=1.01)
    ax = plt.gca()
    ax.tick_params(axis = 'both', which = 'major', labelsize = 18)
    ax.tick_params(axis = 'both', which = 'minor', labelsize = 18)
    plt.show()
    plt.legend()
    plt.show()
    
    
    
#     print(da_pd)
#     print(da_pd.groupby(0).groups.keys())
    
    exit(0)
    
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