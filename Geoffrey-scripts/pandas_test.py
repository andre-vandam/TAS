import pandas as pd
import numpy as np
import scipy as sp
import os.path
import matplotlib.pyplot as plt
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D

data = np.genfromtxt('3',
                          delimiter=',',
                          skip_header=5,
                          skip_footer=1,
                          dtype=str)

# FUNCTIONS
#---------------------------------------------------------------------------
# Save Function
def save_csv(filename, DataFrame):
    i = 0
    while True:
        if os.path.isfile(filename) == True:
            FileExistsError()

            while True:
                ans = input("Would you like to change it yourself (Y/N)? ")

                if ans == 'Y':
                    filename = input("New filename: ")

                    if os.path.isfile(filename) == False:
                        break

                    else:
                        ans = 'N'; return ans

                elif ans == 'N':

                    while True:
                        i += 1
                        filename = str(filename) + "(" + str(i) + ")"

                        if os.path.isfile(filename) == False:
                            break
                        else:
                            continue

                    break

                else:
                    print('Input not recognised')
        elif os.path.isfile(filename) == False:
            DataFrame.to_csv(filename)
            break

# Functions for array of vectors       #i.e: [[x0,y0,z0],
def arr_vec_dot(arr1, arr2):                # [x1,y1,z1],
    arr_dots = []                           # [x2,y2,z2],
    for vec1,vec2 in zip(arr1,arr2):        # [x3,y3,z3],
        dot = np.dot(vec1,vec2)
        arr_dots.append(dot)
    return np.array(arr_dots)

def arr_vec_length(arr):
    arr_lengths = []
    for vec in arr:
        length = np.sqrt(arr_vec_dot(vec, vec))
        arr_lengths.append(length)
    return np.array(arr_lengths)

def arr_vec_angle(arr1, arr2):
    arr_angles = []

    for vec1,vec2 in zip(arr1,arr2):
        try:
            angle = np.arccos(np.dot(vec1, vec2) / (np.sqrt(np.dot(vec1, vec1)) * np.sqrt(np.dot(vec2, vec2))))
            arr_angles.append(np.rad2deg(angle))
        except RuntimeWarning:
            print(np.dot(vec1, vec2),np.sqrt(np.dot(vec1, vec1)),np.sqrt(np.dot(vec2, vec2)))

    return np.array(arr_angles)

# DataFrame
#---------------------------------------------------------------------------

# Columns to be used for DataFrame
columns = ['?',"u_x","u_y","u_z","?","sos",'?',"?","?","?","Time-stamp"]

# Creating DataFrame
df = pd.DataFrame(data, columns =columns )



# DataFrame Manipulation (first time running data)
#---------------------------------------------------------------------------

# Delete all rows with '' for u_x
df = df[df.u_x != '']

# Delete Columns with '?'
del df['?']

# Setting Data Types (this slows processing)
df['Time-stamp'] = df['Time-stamp'].apply(pd.to_datetime)
df[['u_x','u_y','u_z','sos']] = df[['u_x','u_y','u_z','sos']].apply(pd.to_numeric)

print(df.u_x)

# FUNCTIONS
#---------------------------------------------------------------------------

# Assigning the components of ux,uy,uz to an array for V
V = df[['u_x','u_y','u_z']].values

# Setting Uxy (component of velocity in xy-plane)
Uxy = df[['u_x','u_y']].values
Uxy = np.insert(Uxy, [2], [0], axis = 1)

# Calculating array of thetas using function
Theta = arr_vec_angle(Uxy,V)
df['Theta'] = Theta

# plt.plot(df["Time-stamp"],df['Theta'])
# plt.show()

save_csv('test',df)


# while True:
#     input("Would you like to")


# 3D PLOT ANIMATION

# Preamble


# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(0, max(V[:,0])), ylim = (0, max(V[:,1])))
line, = ax.plot([], [], lw=2)


# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    return line,

# animation function.  This is called sequentially
def animate(i):
    x = V[:,0];    y = V[:,1]
    line.set_data(x, y)
    return line,

print(df)

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=20, blit=True)

# save the animation as an mp4.  This requires ffmpeg or mencoder to be
# installed.  The extra_args ensure that the x264 codec is used, so that
# the video can be embedded in html5.  You may need to adjust this for
# your system: for more information, see
# http://matplotlib.sourceforge.net/api/animation_api.html
anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

ax.set_xlabel('Ux')
ax.set_ylabel('Uy')
# ax.set_xlabel('Uz')

ax.w_xaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))

plt.show()


# STATIC PLOT
# ax = fig.add_subplot(111, projection = '3d')
# x = V[0,0]
# y = V[0,1]
# z = V[0,2]

# ax.plot([0,x],[0,y],[0,z])
#
# ax.plot([0,x],[0,0],[0,0])
# ax.plot([0,0],[0,y],[0,0])
# ax.plot([0,0],[0,0],[0,z])
#
# ax.plot([0,x],[0,y],[0,0])

# Set the background color of the pane YZ
# ax.scatter(x, y, z, marker='o')

# plt.show()



