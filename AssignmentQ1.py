#to import Random Walk
from Functions import *
from matplotlib import pyplot as plt
#Step sizes
ranges =[300, 500, 700, 900, 1100]
#Arrays for appending average values of all step sizes
R0=[]
Rrms0=[]
Xavg0=[]
Yavg0=[]
for k in ranges:
    #For each step sizes
    R = []
    Rrms = []
    Xavg = []
    Yavg = []
    #For 100 iterations of same step size
    for j in range(0,100):
        (xdist,ydist,rrms,a,b)=RandomWalk(k)
        if j<5:
            #Data file for first 5 iterations of every step size
            file1 = open('RandomWalk N='+str(k)+'-'+str(j+1)+'.txt','w+')
            for i in range(k):
                file1.writelines(str(a[i])+' ')
                file1.writelines(str(b[i])+' ')
                file1.writelines("\n")
            #Random walk plotting for every stepsize
            plt.plot(a,b, linewidth = 1,label = j+1)
            plt.xlabel('X- axis')
            plt.ylabel('Y- axis')
            plt.title('Random Walk for N='+str(k))
            plt.legend()
            file1.close()

        Xavg.append(xdist)
        Yavg.append(ydist)
        Rrms.append(math.sqrt(rrms/k))
        R.append(math.sqrt(pow(xdist,2)+pow(ydist,2)))
        del a,b
    xavg=0;yavg=0;rms=0;r=0
    #Taking average of all 100 iterations for each step
    for j in range(100):
        xavg+=Xavg[j]/100
        yavg+=Yavg[j]/100
        rms+=Rrms[j]/100
        r+=R[j]/100

    Xavg0.append(xavg)
    Yavg0.append(yavg)
    Rrms0.append(rms)
    R0.append(r)
    plt.show()
print("Values for each set")
print("Average displcement in X ",Xavg0)
print("Average displcement in Y ",Yavg0)
print("RMS value ",Rrms0)
print("Radial distance",R0)
#plot for RMS vs Root N
for d in range(5):
    ranges[d]=math.sqrt(ranges[d])
plt.plot(Rrms0,ranges, marker = 'o', markerfacecolor='blue', markersize=12)
plt.xlabel('Root of Number of Iterations')
plt.ylabel('RMS value of R')
plt.title('Relation between RMS value and root of Number of Steps')
plt.show()

# Values for each set
# Average displcement in X  [0.24188696596003678, 0.5596395558560645, 1.080549419301544, -1.1558922461958305, -2.5689785256999413]
# Average displcement in Y  [1.5497989552287472, 1.9589545825729902, 1.4460760011288532, -1.836271108634237, -0.4093122201093624]
# RMS value  [11.417701579729314, 15.177567524702944, 18.2080379513122, 20.415468257614766, 21.049937871105545]
# Radial distance [15.169627508394257, 21.20574282175243, 24.17519642888298, 27.937169496195665, 30.91329953443269]