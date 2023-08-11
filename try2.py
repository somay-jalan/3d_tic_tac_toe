import plotly.graph_objects as go
import numpy as np 
import ipywidgets
def cubes(size, pos_x, pos_y, pos_z, color):
    info_x=pos_x//3
    # create points
    x, y, z = np.meshgrid(
        np.linspace(pos_x-size/2, pos_x+size/2, 2), 
        np.linspace(pos_y-size/2, pos_y+size/2, 2), 
        np.linspace(pos_z-size/2, pos_z+size/2, 2),
    )
    x = x.flatten()
    y = y.flatten()
    z = z.flatten()
    return go.Mesh3d(x=x, y=y, z=z, alphahull=1, flatshading=True, color=color,opacity=0.5, lighting={'diffuse': 0.1, 'specular': 2.0, 'roughness': 0.5})
fig = go.Figure()
# set edge length of cubes
size = 1

# add outer cube

# add inner center cube
for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
                f=go.FigureWidget(fig.add_trace(cubes(size,i*3,j*3,k*3, "pink")))

fig.show()