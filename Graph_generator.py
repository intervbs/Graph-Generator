#!/usr/bin/env python3
'''Written by Jøran Lillegård 2022'''
import matplotlib.pyplot as plt
import numpy as np

def onclick(event):
    xy.append(f'x{int(event.xdata)}y{int(event.ydata)}')

def make_graph(size, prob, filename):
    '''Input the size, probability for the coordinate to be a wall and the filename
       It will output two files in the same directory that your terminal is in'''
    grid_size = (size, size)                              
    file = open(f'{filename}.txt', 'w')
    file_xtras = open(f'{filename}_xtras.txt', 'w')
    file_xtras.write('remove:')
    obstacle_prob = (f'0.{prob}')

    # Setting up the grid with bool values
    grid = np.random.random(grid_size) > float(obstacle_prob)
    locked = False

    # Draws the image and let the user select the start and end point graphicaly
    fig = plt.figure(figsize=(10,10))
    plt.imshow(grid, cmap='gray', interpolation='nearest')

    # Get the mouse coordinates
    fig.canvas.mpl_connect('button_press_event', onclick)
    plt.show()

    # Writing all the nodes and all its neighbours
    for y in range(len(grid)):
        for x in range(len(grid[y])):     
            if x >= 0 and y-1 >= 0:
                file.write(f'x{x}y{y};x{x}y{y-1};1\n')
            if x-1 >= 0 and y >= 0:
                file.write(f'x{x}y{y};x{x-1}y{y};1\n')
            if x <= len(grid)-1 and y+1 <= len(grid)-1:
                file.write(f'x{x}y{y};x{x}y{y+1};1\n')
            if x+1 <= len(grid)-1 and y <= len(grid)-1:
                file.write(f'x{x}y{y};x{x+1}y{y};1\n')
            if grid[y][x] == False:
                if locked == False:
                    file_xtras.write(f'x{x}y{y}')
                    locked = True
                else:
                    file_xtras.write(f';x{x}y{y}')

    # Writes the start and end coordinates
    file_xtras.write(f'\nstartvertex:{xy[0]}')
    file_xtras.write(f'\ntargetvertex:{xy[1]}')

    # Close all files before exiting
    file.close()
    file_xtras.close()

if __name__ == '__main__':
    # Asks the user for the grid size, filename and probability that a node is a wall
    size = int(input('Enter a size number between 1 - 200 ---> '))
    prob = int(input('Enter the probability for a node to be a wall (0-99) ---> '))
    filename = input('What do you want the filename to be called? ---> ')
    xy = []
    make_graph(size, prob, filename)
