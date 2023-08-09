# import matplotlib.pyplot as plt
# import numpy as np
# import matplotlib


# matplotlib.use('Qt5Agg')
# def f(x,y):
#     return x
# fig = plt.figure()
# ax = fig.add_subplot(projection='3d')

# # # Make data
# # u = np.linspace(0, 2 * np.pi, 100)
# # v = np.linspace(0, np.pi, 100)
# # x = 10 * np.outer(np.cos(u), np.sin(v))
# # y = 10 * np.outer(np.sin(u), np.sin(v))
# # z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))
# x=np.linspace(0,1)
# y=np.linspace(0,1)
# X, Y = np.meshgrid(x, y)
# Z = f(X, Y)
# print(Z)
# ax.contour3D(X, Y, Z, 50, cmap='binary')
# plt.show()

# Import all the necessary libraries and packages in the code
# import matplotlib.pyplot as plt
# import numpy as np
# import matplotlib
# matplotlib.use('Qt5Agg')

# # Defining the user-defined cubes() function
# def cubes(side,color_x,color_y,color_z):
#     # Defining the size of the axes
#     x, y, z = np.indices((5, 5, 5))
#     # Defining the length of the sides of the cubes
#     cube = (x < side) & (y < side) & (z < side)
#     color_true=(x==color_x)&(y==color_y)&(z==color_z)
#     color_false=(x < side) & (y < side) & (z < side)
#     print(color_true)
#     # Defining the shape of the figure to be a cube
#     voxelarray = cube
#     # Defining the colors for the cubes
#     colors = np.empty(voxelarray.shape, dtype=object)
#     # Defining the color of the cube
#     colors[color_false]='white'
#     colors[color_true] = 'purple'
#     print(colors)
#     # Defining the axes and the figure object
#     ax = plt.figure(figsize=(9, 9)).add_subplot(projection='3d',xmargin=1,ymargin=1)
#     # Plotting the cube in the figure
#     ax.voxels(voxelarray , facecolors=colors,alpha=0.5)
#     # Defining the title of the graph
#     plt.title("Three dimensional cubes")
#     # Displaying the graph
#     plt.show()
# # Defining the main() function
# def main():
#     # Defining the side of the cube
#     sides = 1
#     # Calling the cubes () function
#     cubes(sides,0,0,0)
# # Calling the main () function
# if __name__ == "__main__":
#     main ()

import tkinter as Tk
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, PathPatch
import numpy as np
from mpl_toolkits.mplot3d import Axes3D 
import mpl_toolkits.mplot3d.art3d as art3d
from matplotlib.backend_bases import MouseButton

cmap = plt.get_cmap('spring') #define the colors of the plot 
colors = [cmap(i) for i in np.linspace(0.1, 0.9, 5+1)]  

def check_exist(i,j,k):
    if 0<=i<=2 and 0<=j<=2 and 0<=k<=2:
        return True
    else:
        return False

def check_3d_cube(cube_3d,turn):
    exists=list()
    for i in range(0,3):
        for j in range(0,3):
            for k in range(0,3):
                if cube_3d[i][j][k]==turn:
                    if(check_exist(i-1,j,k)):
                        if(cube_3d[i-1][j][k]==turn):
                            if(check_exist(i-2,j,k)):
                                if(cube_3d[i-2][j][k]==turn):
                                    exists.append([i,j,k])
                                    exists.append([i-2,j,k])
                    if(check_exist(i,j-1,k)):
                        if(cube_3d[i][j-1][k]==turn):
                            if(check_exist(i,j-2,k)):
                                if(cube_3d[i][j-2][k]==turn):
                                    exists.append([i,j,k])
                                    exists.append([i,j-2,k])
                    if(check_exist(i,j,k-1)):
                        if(cube_3d[i][j][k-1]==turn):
                            if(check_exist(i,j,k-2)):
                                if(cube_3d[i][j][k-2]==turn):
                                    exists.append([i,j,k])
                                    exists.append([i,j,k-2])


def cube(a,b,c,l,color): #plots a cube of side l at (a,b,c)  
        for ll in [0,l]:
            for i in range(3):
                dire= ["x","y","z"]
                xdire = [b,a,a] 
                ydire = [c,c,b]
                zdire = [a,b,c]
                side = Rectangle((xdire[i],ydire[i]),height=1,width=1,edgecolor='black',facecolor=color,alpha=0.5)
                ax.add_patch(side)
                art3d.pathpatch_2d_to_3d(side, z=zdire[i]+ll, zdir=dire[i])

def plotter3D(X,Y,Z,sizes,color): #run cube(a,b,c,l) over the whole data set 
    for iX in range(len(X)):
        x = X[iX]
        y = Y[iX]
        z = Z[iX]
        for ix in range(len(x)): 
            cube(x[ix],y[ix],z[ix],sizes[iX],color)

X=[[0,3,6,0,0,3,3,6,6],[0,3,6,0,0,3,3,6,6],[0,3,6,0,0,3,3,6,6]]
Y=[[0,0,0,3,6,3,6,3,6],[0,0,0,3,6,3,6,3,6],[0,0,0,3,6,3,6,3,6]]
Z=[[0,0,0,0,0,0,0,0,0],[3,3,3,3,3,3,3,3,3],[6,6,6,6,6,6,6,6,6]]
sizes=[1,1,1,1,1,1,1,1,1]

fig = plt.figure() #open a figure 
ax=fig.add_subplot(projection='3d') #make it 3d
plotter3D(X,Y,Z,sizes,"pink") #generate the cubes from the data set 
ax.set_xlim3d(0, 7) #set the plot ranges 
ax.set_ylim3d(0, 7)
ax.set_zlim3d(0, 7)
try_again=True
cube_3d=list()
for i in range(0,3):
    tempk=[]
    for j in range(0,3):
        tempj=["-","-","-"]
        tempk.append(tempj)
    cube_3d.append(tempk)
print(cube_3d)
plt.pause(0.05)
turn=0
while try_again:

    user_input=input("Enter your play:")
    if(user_input=="quit"):
        try_again=False
    user_input=list(user_input)
    if(len(user_input)<3):
        print("wrong input")
        continue
    for i in range(0,3):
        user_input[i]=int(user_input[i])
    # print(user_input[0]>2,user_input[1]>2,user_input[2]>2)
    # print(user_input[0]>2 or user_input[1]>2 or user_input [2]>2)

    if(user_input[0]>2 or user_input[1]>2 or user_input [2]>2):
        print("try again wrong input")
        continue
    if(cube_3d[user_input[0]][user_input[1]][user_input[2]]!="-"):
        print("cube already colored")
        continue
    else:
        cube_3d[user_input[0]][user_input[1]][user_input[2]]=turn
    print(cube_3d)
    X=[[(user_input[0])*3]]
    Y=[[(user_input[1])*3]]
    Z=[[(user_input[2])*3]]
    if(turn==0):
        plotter3D(X,Y,Z,sizes,"red")
    else:
         plotter3D(X,Y,Z,sizes,"blue")   
    if(turn==1):
        turn=0
    else:
        turn=1 
    plt.pause(0.05)
plt.show()