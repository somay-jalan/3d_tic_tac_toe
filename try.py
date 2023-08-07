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

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, PathPatch
import numpy as np
from mpl_toolkits.mplot3d import Axes3D 
import mpl_toolkits.mplot3d.art3d as art3d
import matplotlib
matplotlib.use('Qt5Agg')

cmap = plt.get_cmap('spring') #define the colors of the plot 
colors = [cmap(i) for i in np.linspace(0.1, 0.9, 5+1)]  

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

X=[[0,2,4,0,0,2,2,4,4],[0,2,4,0,0,2,2,4,4],[0,2,4,0,0,2,2,4,4]]
Y=[[0,0,0,2,4,2,4,2,4],[0,0,0,2,4,2,4,2,4],[0,0,0,2,4,2,4,2,4]]
Z=[[0,0,0,0,0,0,0,0,0],[2,2,2,2,2,2,2,2,2],[4,4,4,4,4,4,4,4,4]]
sizes=[1,1,1,1,1,1,1,1,1]

fig = plt.figure() #open a figure 
ax=fig.add_subplot(projection='3d') #make it 3d
plotter3D(X,Y,Z,sizes,"pink") #generate the cubes from the data set 
ax.set_xlim3d(0, 5) #set the plot ranges 
ax.set_ylim3d(0, 5)
ax.set_zlim3d(0, 5)
try_again=True
club_3d=list()
for i in range(0,3):
    tempk=[]
    for j in range(0,3):
        tempj=["-","-","-"]
        tempk.append(tempj)
    club_3d.append(tempk)
print(club_3d)

             
while try_again:
    user_input=input("Enter your play:")
    if(user_input=="quit"):
         try_again=False
    user_input=user_input.split(",")
    
    X=[[int(user_input[0])*2]]
    Y=[[int(user_input[1])*2]]
    Z=[[int(user_input[2])*2]]
    if(int(user_input[3])==0):
        plotter3D(X,Y,Z,sizes,"red")
    else:
         plotter3D(X,Y,Z,sizes,"blue")    
    plt.pause(0.05)
plt.show()
