'''
Created on 31-Mar-2020

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
from MIS import computeMIS
from MIS import ApproxMIS
from MIS import greedyApproxMIS,greedyMISII
import numpy as np
import numpy.lib.recfunctions as rfn
class MyLocator(AutoLocator):
    def view_limits(self, vmin, vmax):
        multiplier = 5.0
        vmin = multiplier * np.floor(vmin / multiplier)
        vmax = multiplier * np.ceil(vmax / multiplier)
        return vmin, vmax
if __name__ == "__main__":
    numberOfRectangles = 20
    planeXRange = [1500.0,1590.0]
    planeYRange = [1500.0,1590.0]
    
#     widthRange = [4,30]
#     heightRange = [4,10]
    
    widthRange = [5,20]
    heightRange = np.array([5,15])
    
    result_array = []
    
#     for nr in range(5,26):
    for j in range(0,5):
        fig,ax = plt.subplots(nrows=1, ncols=3)
        plt.axes(ax[0])
        currentAxis = plt.gca()
        input_rectangles = []
        sideLength = (np.ceil(np.sqrt(180*numberOfRectangles)))
#         planeXRange = np.array([1500.0,1500.0+sideLength])
#         planeYRange = np.array([1500.0,1500.0+sideLength])
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
            
            
            perturb_ = (float(i+1) / numberOfRectangles) * random.randint(2,5) 
                
            width_ = random.randint(widthRange[0],widthRange[1]) + perturb_ 
            height_ = random.randint(heightRange[0],heightRange[1]) + perturb_
            
#             width_ = random.randint(widthRange[0],widthRange[1])
#             height_ = random.randint(heightRange[0],heightRange[1])
            
            
            tempRect = [y_val+height_,y_val,x_val,x_val+width_,i]
            input_rectangles.append(tempRect)
                    
        
        print(input_rectangles)
        input_rectangles = np.array(input_rectangles)
#         input_rectangles = [[1512, 1505, 1518, 1535, 0], [1532, 1522, 1515, 1528, 1], [1528, 1516, 1524, 1540, 2], [1526, 1511, 1516, 1529, 3], [1540, 1526, 1515, 1530, 4], [1525, 1510, 1505, 1519, 5], [1533, 1525, 1520, 1531, 6], [1525, 1513, 1513, 1521, 7], [1531, 1518, 1505, 1515, 8], [1540, 1529, 1519, 1527, 9], [1515, 1510, 1516, 1535, 10]]
#         input_rectangles = np.array(input_rectangles)
        
#         input_rectangles = [[1549, 1542, 1526, 1533, 0], [1534, 1526, 1521, 1541, 1], [1546, 1535, 1528, 1545, 2], [1547, 1538, 1522, 1532, 3], [1555, 1544, 1505, 1520, 4], [1523, 1516, 1531, 1551, 5], [1527, 1521, 1539, 1548, 6], [1553, 1541, 1533, 1542, 7]]
#         input_rectangles = np.array(input_rectangles)

#         input_rectangles = [[1551, 1539, 1516, 1531, 0], [1557, 1542, 1520, 1536, 1], [1522, 1513, 1510, 1522, 2], [1521, 1516, 1506, 1520, 3], [1530, 1518, 1510, 1521, 4], [1545, 1538, 1526, 1540, 5], [1534, 1525, 1510, 1527, 6], [1546, 1535, 1520, 1529, 7]]
#         input_rectangles =[[1552, 1538, 1518, 1536, 0], [1533, 1528, 1524, 1538, 1], [1550, 1545, 1510, 1527, 2], [1554, 1547, 1518, 1538, 3], [1547, 1541, 1549, 1569, 4], [1559, 1544, 1531, 1536, 5], [1519, 1507, 1546, 1566, 6], [1515, 1509, 1525, 1532, 7], [1537, 1531, 1537, 1553, 8], [1558, 1551, 1519, 1526, 9], [1547, 1534, 1517, 1532, 10], [1518, 1510, 1519, 1532, 11]]

#         input_rectangles =[[1538, 1527, 1505, 1521, 0], [1517, 1508, 1514, 1525, 1], [1543, 1529, 1528, 1533, 2], [1541, 1529, 1526, 1543, 3], [1523, 1517, 1520, 1533, 4], [1512, 1506, 1530, 1539, 5], [1536, 1521, 1517, 1532, 6], [1531, 1522, 1523, 1531, 7], [1533, 1526, 1518, 1524, 8], [1544, 1530, 1525, 1530, 9], [1544, 1535, 1525, 1535, 10], [1527, 1522, 1524, 1541, 11], [1534, 1522, 1511, 1519, 12], [1545, 1534, 1513, 1530, 13], [1522, 1509, 1513, 1522, 14]]
        
#         input_rectangles = [[1540.2666666666667, 1528, 1529, 1540.2666666666667, 0], [1528.6666666666667, 1523, 1537, 1554.6666666666667, 1], [1560.4, 1551, 1523, 1537.4, 2], [1525.5333333333333, 1511, 1525, 1537.5333333333333, 3], [1562.0, 1552, 1517, 1530.0, 4], [1557.8, 1550, 1525, 1531.8, 5], [1551.3333333333333, 1537, 1520, 1537.3333333333333, 6], [1541.6, 1535, 1537, 1544.6, 7], [1547.2, 1534, 1506, 1522.2, 8], [1523.3333333333333, 1510, 1547, 1569.3333333333333, 9], [1540.4666666666667, 1534, 1544, 1560.4666666666667, 10], [1554.0, 1540, 1512, 1532.0, 11], [1537.7333333333333, 1523, 1520, 1538.7333333333333, 12], [1545.8666666666666, 1530, 1536, 1557.8666666666666, 13], [1566.0, 1548, 1543, 1555.0, 14]]
#         input_rectangles = [[1519.1333333333334, 1510, 1533, 1545.1333333333334, 0], [1557.2666666666667, 1548, 1535, 1551.2666666666667, 1], [1518.0, 1510, 1542, 1554.0, 2], [1521.0666666666666, 1505, 1513, 1521.0666666666666, 3], [1521.3333333333333, 1514, 1526, 1547.3333333333333, 4], [1560.8, 1554, 1517, 1529.8, 5], [1526.4, 1520, 1531, 1537.4, 6], [1547.0666666666666, 1537, 1518, 1524.0666666666666, 7], [1541.4, 1529, 1512, 1520.4, 8], [1548.0, 1539, 1534, 1550.0, 9], [1540.9333333333334, 1524, 1531, 1553.9333333333334, 10], [1529.6, 1521, 1528, 1536.6, 11], [1522.3333333333333, 1506, 1533, 1550.3333333333333, 12], [1532.8666666666666, 1519, 1521, 1540.8666666666666, 13], [1560.0, 1540, 1544, 1556.0, 14]]

#         input_rectangles = [[1564.1333333333334, 1552, 1545, 1563.1333333333334, 0], [1527.5333333333333, 1517, 1513, 1521.5333333333333, 1], [1561.6, 1550, 1520, 1530.6, 2], [1558.0666666666666, 1551, 1508, 1517.0666666666666, 3], [1552.0, 1537, 1516, 1537.0, 4], [1541.2, 1534, 1531, 1537.2, 5], [1559.3333333333333, 1552, 1508, 1517.3333333333333, 6], [1562.0666666666666, 1547, 1541, 1558.0666666666666, 7], [1545.2, 1536, 1510, 1526.2, 8], [1544.6666666666667, 1537, 1544, 1562.6666666666667, 9], [1557.4666666666667, 1544, 1535, 1543.4666666666667, 10], [1533.2, 1520, 1540, 1560.2, 11], [1558.7333333333333, 1549, 1549, 1555.7333333333333, 12], [1554.6666666666667, 1544, 1539, 1559.6666666666667, 13], [1552.0, 1539, 1508, 1524.0, 14]]

        input_rectangles = np.array(input_rectangles)
        ''' partition R into y-intervals '''
        y_intervals = []
        for i_ in range(0,len(input_rectangles)):
            y_intervals.append([input_rectangles[i_,0],input_rectangles[i_,2],input_rectangles[i_,3],1,i_])
            y_intervals.append([input_rectangles[i_,1],input_rectangles[i_,2],input_rectangles[i_,3],2,i_])
            
        y_intervals = np.array(y_intervals)
#         print(y_intervals)
        
        names=('a','b','c','d','e')
        dt = np.dtype([(n,np.float) for n in names])
        y_intervals = np.array(y_intervals)
    
        y_intervals = rfn.unstructured_to_structured(y_intervals, dt)
        
        
        maxCliqueForData = computeMaxClique.computeMaxClique(y_intervals)
        print(maxCliqueForData)
        
#         MISForData = MIS_MemoryEff.prepareMISDat(input_rectangles) 
#         print("MIS = ", MISForData[0])
        
        MISForData = computeMIS.prepareMISDat(input_rectangles)
        print("MIS = ", MISForData[0])
        
        MISForData_greedy = greedyMISII.prepareGreedyMIS(input_rectangles)
        print("MIS greedy = ", MISForData_greedy[0])
        
#         MISForData = MISForData_greedy
        
        heuristicMIS_forData = ApproxMIS.heuristicMISI(input_rectangles)
#         greedyMISII.prepareGreedyMISDI(input_rectangles)
        plt.suptitle(" n = "+str(numberOfRectangles)+" Max clique(q) = "+str(maxCliqueForData[0])+" MIS(I) = "+str(MISForData[0])
                  +" approx MIS = "+str(heuristicMIS_forData[0]))
        
#         exit(0)
        
        mis_rectangles = input_rectangles[list(MISForData[1])]
        
        
        
        for i in range(0,len(mis_rectangles)):
            x_val = mis_rectangles[i,2]
            y_val = mis_rectangles[i,0]
            
            width_ = mis_rectangles[i,3] - mis_rectangles[i,2]
            height_ = mis_rectangles[i,1] - mis_rectangles[i,0]
    
    
            currentAxis.add_patch(Rectangle((x_val, y_val), width_, height_,
                              alpha=0.4, edgecolor='black',facecolor='green'))
            
        
        
        for i in range(0,len(input_rectangles)):
            x_val = input_rectangles[i,2]
            y_val = input_rectangles[i,0]
            
            width_ = input_rectangles[i,3] - input_rectangles[i,2]
            height_ = input_rectangles[i,1] - input_rectangles[i,0]
    
            
            currentAxis.add_patch(Rectangle((x_val, y_val), width_, height_,
                            alpha=1, edgecolor='black',fill=None))
            if maxCliqueForData[1] is not None:
                circle_ = plt.Circle((maxCliqueForData[1][0]-0.3,maxCliqueForData[1][1]+0.3), 0.3, color='red')
                
                currentAxis.add_artist(circle_)
            
            currentAxis.annotate(str(i), (x_val, y_val), color='b', weight='bold', 
                fontsize=10, ha='center', va='center')
        
        plt.title("MIS brute force shaded, Clique shown as Red dot ",fontsize=16)
        ax[0].xaxis.set_major_locator(MyLocator())
        ax[0].yaxis.set_major_locator(MyLocator())
        ax[0].autoscale()
        
        
        plt.axes(ax[1])
        currentAxis = plt.gca()
        
        
        approx_rectangles = input_rectangles[list(MISForData_greedy[1])]
        for i in range(0,len(approx_rectangles)):
            x_val = approx_rectangles[i,2]
            y_val = approx_rectangles[i,0]
            
            width_ = approx_rectangles[i,3] - approx_rectangles[i,2]
            height_ = approx_rectangles[i,1] - approx_rectangles[i,0]
    
    
            currentAxis.add_patch(Rectangle((x_val, y_val), width_, height_,
                              alpha=0.1, edgecolor='black',facecolor='red'))
        
        
        
        
#         input_rectangles = np.delete(input_rectangles,MISForData[1],axis=0)
#         input_rectangles = np.delete(input_rectangles,heuristicMIS_forData[1],axis=0)
        
    
        
        for i in range(0,len(input_rectangles)):
            x_val = input_rectangles[i,2]
            y_val = input_rectangles[i,0]
            
            width_ = input_rectangles[i,3] - input_rectangles[i,2]
            height_ = input_rectangles[i,1] - input_rectangles[i,0]
    
    
            currentAxis.add_patch(Rectangle((x_val, y_val), width_, height_,
                              alpha=1, edgecolor='black',fill=None))
            
            currentAxis.annotate(str(i), (x_val, y_val), color='b', weight='bold', 
                fontsize=10, ha='center', va='center')
        
        ax[1].xaxis.set_major_locator(MyLocator())
        ax[1].yaxis.set_major_locator(MyLocator())
        ax[1].autoscale()
        
#         plt.title("MIS Approx Greedy. (max.) shaded "
#                   ,fontsize=18)
        
        plt.title("MIS Approx Greedy. shaded "
                  ,fontsize=18)
        
        plt.axes(ax[2])
        currentAxis = plt.gca()
        
        
        approx_rectangles = input_rectangles[list(heuristicMIS_forData[1])]
        for i in range(0,len(approx_rectangles)):
            x_val = approx_rectangles[i,2]
            y_val = approx_rectangles[i,0]
            
            width_ = approx_rectangles[i,3] - approx_rectangles[i,2]
            height_ = approx_rectangles[i,1] - approx_rectangles[i,0]
    
    
            currentAxis.add_patch(Rectangle((x_val, y_val), width_, height_,
                              alpha=0.1, edgecolor='black',facecolor='red'))
        
        
        
        
#         input_rectangles = np.delete(input_rectangles,MISForData[1],axis=0)
#         input_rectangles = np.delete(input_rectangles,heuristicMIS_forData[1],axis=0)
        
    
        
        for i in range(0,len(input_rectangles)):
            x_val = input_rectangles[i,2]
            y_val = input_rectangles[i,0]
            
            width_ = input_rectangles[i,3] - input_rectangles[i,2]
            height_ = input_rectangles[i,1] - input_rectangles[i,0]
    
    
            currentAxis.add_patch(Rectangle((x_val, y_val), width_, height_,
                              alpha=1, edgecolor='black',fill=None))
            
            currentAxis.annotate(str(i), (x_val, y_val), color='b', weight='bold', 
                fontsize=10, ha='center', va='center')
        
        ax[2].xaxis.set_major_locator(MyLocator())
        ax[2].yaxis.set_major_locator(MyLocator())
        ax[2].autoscale()
        
#         plt.title("MIS Approx Greedy Min. Simplicial shaded "
#                   ,fontsize=18)
        plt.title("MIS Approx DnC shaded "
                  ,fontsize=18)
        
        plt.suptitle(" n = "+str(numberOfRectangles)+" [Max clique(q) = "+str(maxCliqueForData[0])+"] [MIS(I) = "+str(MISForData[0])
                  +"] [approx MIS  greedy = "+str(MISForData_greedy[0]) + 
                  "] [approx MIS  DnC = "+str(heuristicMIS_forData[0])+"]",fontsize=22)
        plt.show()