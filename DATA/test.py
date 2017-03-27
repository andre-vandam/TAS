import numpy as np
import pygame

# Data array creation from data.txt
data = np.genfromtxt('Gill Log [WM1]-4', delimiter =',', skip_header=5, skip_footer=1, dtype=str)

#timestamp = column 10
#Ux = col 1
#uy = col 2
#uz = col 3

# Time stamp string sectioning (removal of date)
for i in range(len(data[:,10])):
    time = data[i,10]
    time = time[11:]
    data[i,10] = time

# Function to calculate time interval between two time-stamps
def timedifference(t1, t2):
    t1 = t1
    t2 = t2

    # Calculation of time interval between two time-stamps
    for i in range(2):
        dh = float(t2[:-6]) - float(t1[:-6])
        dm = float(t2[2:-3]) - float(t1[2:-3])
        ds = float(t2[5:]) - float(t1[5:])

        Dt = dh*60*60 + dm*60 + ds #[s]

        return Dt

def scale(scale, ux, uy):
    x_vec = ux * scale
    y_vec = uy * scale

    return x_vec,y_vec


# Preamble to
center_pos = (240,240)
black_col = (0,0,0)

def vector(vector, scale):
    vectorscaled = float(vector)*scale
    return vectorscaled

def main():
    """ Game setup and loop """
    pygame.init()
    surface_sz = 480

    # Creating surface of size (width, height)
    main_surface = pygame.display.set_mode((surface_sz, surface_sz))

    # Creation of x and y axis for vector reference frame
    line_xaxis = pygame.draw.line(main_surface, black_col, center_pos, (240, 140))
    line_yaxis = pygame.draw.line(main_surface, black_col, center_pos, (340, 240))
    scale = 10
    # time_0 = data[]
    i = 0

    # while True:
    #     ev = pygame.event.poll()
    #     if __name__ == '__main__':
    #
    #         for i in range(len(data[:,10])):
    #
    #             if ev.type ==pygame.QUIT:
    #                 break
    #             #Update of objects and data structures here.
    #             line_ux = pygame.draw.line(main_surface, black_col, center_pos, (240 + vector(data[i,1],scale), 240))
    #             line_uy = pygame.draw.line(main_surface, black_col, center_pos, (240, 240 + vector(data[i,2],scale)))
    #
    #             # Draw everything from scratch on each frame
    #             # Background colour
    #             main_surface.fill((0,200,255))
    #
    #             main_surface.fill(black_col, line_xaxis)
    #             main_surface.fill(black_col, line_yaxis)
    #
    #             # timedif = timedifference()
    #             # pygame.time.wait(1000*)
    #             pygame.display.flip()
    #
    #         i =+ 1
    #
    #
    # pygame.quit()

main()


# from math import pi as pi
# from math import sqrt as sqrt
# from math import sin as sin
# import matplotlib.pyplot as plt
# import pygame
# import numpy as np
# import os
#
# #Pendulum characteristics
# T = np.arange(51,66,1) #[oscillation per min]
# T = 1/(T/60.)            #[period]
# g = 9.80665 #[m/s^2]
# L = g*(T/(2*pi))**2
#
# #Initial conditions
# theta = np.array(15*[pi/4])
# t = 0.
# dt = 0.01 #[s]
# omega = np.array(15*[0])
# alpha = (g*np.sin(theta))/L
# x = L*np.sin(theta)
# y = L*np.cos(theta)
# meter = 1500 #pix
#
# #Pygame
# tublue = (50,200,255)
# black = (0,0,0)
# red = (255,0,0)


# def pendulum(theta, omega, alpha, t, x, y):
#
#     t = t + dt
#     alpha = -(g*np.sin(theta))/L
#
#     omega = omega + alpha*dt
#     theta = theta + omega*dt
#
#     x = L*np.sin(theta)
#     y = L*np.cos(theta)
#
#     return theta, omega, alpha, t, x, y

# ttab = []
# thetatab = []
# omegatab = []
# alphatab = []
# xtab = []
# ytab = []
#
# pygame.init()
#
# gameDisplay = pygame.display.set_mode((800,600))
# pygame.display.set_caption('Pendulum Animation')
# ball = pygame.transform.scale(pygame.image.load("sphere(1).png"),(20,20))
#
# ballrect = ball.get_rect()
#
# gameExit = False
#
# while not gameExit:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             gameExit = True
#
#     clock = pygame.time.Clock()
#
#     theta, omega, alpha, t, x, y = pendulum(theta, omega, alpha, t, x, y)
#     gameDisplay.fill(tublue)
#
#     for i in range(0,15):
#         ballrect.center = (400 + meter * (x[i]), meter * (y[i]))
#
#         pygame.draw.aaline(gameDisplay, black, (400, 10), (400 + meter * (x[i]), meter * (y[i]) ), 1)
#         gameDisplay.blit(ball, ballrect)
#
#     pygame.display.update()
#
#     clock.tick(100)
