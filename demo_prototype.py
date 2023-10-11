import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 
import numpy as np
from tkinter import *
import PySide6
matplotlib.use('Qt5Agg')
axes = [3,3,3]
data = np.ones(axes)
alpha = 0.5
colors = np.empty(axes +[4])
color=0
turn=0
while input("Try:")!=0000:
    plt.close()
    colors[2]= [1, 0, color, alpha] # red
    print(colors)
    # colors[]
    # colors[1] = [0, 1, 0, alpha] # green
    # colors[2] = [0, 0, 1, alpha] # blue
    fig = plt.figure()
    color =1
    ax = fig.add_subplot(111, projection='3d')
    ax.set_facecolor("cyan")
    ax.voxels(data)
    # x=[0,1]
    # y=[0,1]
    # z=[0,1]
    ax.fill()
    plt.pause(0.05)
    turn+=1
plt.show()



cube=[]
for i in range(0,3):
    tempi=[]
    for j in range(0,3):
        tempj=[]
        for k in range(0,3):
            tempj.append("-")
        tempi.append(tempj)
    cube.append(tempi)
user_input=input("Enter place you want to add the 0 or 1 at (in 000,001,002) format. and then add 1 or 0 after that in a comma:")
user_input=user_input.split(",")
user_index=user_input[0]
cube[int(user_index[0])][int(user_index[1])][int(user_index[2])]=int(user_input[1])
print(cube)
print(cube)
