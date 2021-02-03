#to import MonteCarlo3D
from Functions import *
from matplotlib import pyplot as plt
import math
import random
#the function
def func(x,y,z):
    p = pow(z/2,2)+pow(y/1.5,2)+pow(x,2)
    return p
#Set of steps taken
step=[100,250,500,750,1000,2500,5000,7500,10000,25000]
Vol=[]
#For every step size
for m in step:
    j = 0; total = 0
    file1 = open('Monte Carlo for N=' + str(m) + '.txt', 'w+')
    #randomly plotting m steps
    while j<m:
        (x,y,z)=MonteCarlo3D(1,1.5,2)
        if func(x,y,z)<=1:
            total+=1
        j+=1
        #For writing in text file
        if func(x,y,z)<=1:
            file1.writelines(str(x) + " ")
            file1.writelines(str(y) + " ")
            file1.writelines(str(z) + '\n')
    #For finding volume.No of points in/ total no of points *total volume
    volume = (total/m)*24
    Vol.append(volume)

print("Volume for each step size",Vol)
#Comparing with analytical value
fig1 = plt.figure()
plt.axhline(y=12.56637, color='r', linestyle='-')
plt.plot(step,Vol, marker = 'o',markerfacecolor='blue')
plt.xlabel('Number of Iterations')
plt.ylabel('Volume obtained')
plt.title('Relation between Volume obtained and Number of Steps with analytical value')
plt.show()

fig2 = plt.figure()
#Actual volume = 12.56637
#Relation between Fractional Error and Number of Steps
for i in range(10):
    Vol[i]=abs(Vol[i]-12.56637)/12.56637
plt.plot(step, Vol, marker = 'o',markerfacecolor='blue')
plt.xscale("log")
plt.xlabel('Number of Iterations')
plt.ylabel('Fractional Error')
plt.title('Relation between Fractional Error and Number of Steps')
plt.show()

# Volume for each step size [11.040000000000001, 14.687999999999999, 12.624, 12.384, 12.744, 12.6432, 12.3312, 12.5792, 12.6024, 12.595200000000002]