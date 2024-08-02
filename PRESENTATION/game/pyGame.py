# Simple pygame program

# Import and initialize the pygame library
import pygame
from collections import deque
import random 
import sys
from tkinter import messagebox, Tk
import math


size = (width,height) = 640,480
pygame.init()

win = pygame.display.set_mode(size)
pygame.display.set_caption("Path finding ")
clock = pygame.time.Clock()

cols , rows = 64,48
w = 10
h = 10
grid = []
queue , visited = deque(), []
path = []
openSet, closeSet = [], []
bfspath = []

class Spot :
    def __init__(self,i,j):
        self.x , self.y = i,j
        self.f,self.g,self.h = 0,0,0
        self.neighbors = []
        self.prev = None
        self.wall = False
        self.visited = False
        # if random.randint(0,100) < 20:
        #     self.wall = True

    def show(self,win,col):
        if self.wall == True:
            col = (0,0,0)
        # top left corners , and wifht and height of rectangle
        pygame.draw.rect(win,col,(self.x*w,self.y*h,w-1,h-1)) 
    
    def add_neighbors(self,grid):
        if self.x < cols - 1:
            self.neighbors.append(grid[self.x+1][self.y])
        if self.x > 0 :
            self.neighbors.append(grid[self.x-1][self.y])
        if self.y < rows - 1:
            self.neighbors.append(grid[self.x][self.y+1])
        if self.y > 0 :
            self.neighbors.append(grid[self.x][self.y-1])
        #Add Diagonals
        # if self.x < cols - 1 and self.y < rows - 1:
        #     self.neighbors.append(grid[self.x+1][self.y+1])
        # if self.x < cols - 1 and self.y > 0:
        #     self.neighbors.append(grid[self.x+1][self.y-1])
        # if self.x > 0 and self.y < rows - 1:
        #     self.neighbors.append(grid[self.x-1][self.y+1])
        # if self.x > 0 and self.y > 0:
        #     self.neighbors.append(grid[self.x-1][self.y-1])


def clickWall(pos,state):
    i = pos[0]//w
    j = pos[1]//h
    grid[i][j].wall = state

def place(pos):
    i = pos[0] // w 
    j = pos[1] // h 
    # what should i return
    return i,j

def heuristics(a, b):
    return math.sqrt((a.x - b.x)**2 + abs(a.y - b.y)**2)

for i in range(cols):
    arr = []
    for j in range(rows):
        arr.append(Spot(i,j))
    grid.append(arr)

for i in range(cols):
    for j in range(rows):
        grid[i][j].add_neighbors(grid)

start = grid[cols//2][rows//2]
end = grid[cols-1][rows - cols//2]
# start = None
# end = None 
queue.append(start)
start.visited = True
openSet.append(start)

def main():
    flag = False
    astarFlag = False
    noFlag = True
    startFlag = False
    def bfs():
        nonlocal flag, noFlag
        while queue:
            
            current = queue.popleft()
            if current == end:
                temp = current
                while temp.prev:
                    bfspath.append(temp.prev)
                    temp = temp.prev 
                if not flag:
                    flag = True
                    print("DoneBFS")
                elif flag:
                    continue
            if flag == False:
                for i in current.neighbors:
                    if not i.visited and not i.wall:
                        i.visited = True
                        i.prev = current
                        queue.append(i)

        if noFlag and not flag:
            Tk().wm_withdraw()
            messagebox.showinfo("No Solution", "There was no solution" )
            noFlag = False
    
        
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                if pygame.mouse.get_pressed(3)[0]:
                    clickWall(pygame.mouse.get_pos(),True)
                if pygame.mouse.get_pressed(3)[2]:
                    clickWall(pygame.mouse.get_pos(),False)
            if event.type == pygame.MOUSEMOTION:
                if pygame.mouse.get_pressed(3)[0]:
                    clickWall(pygame.mouse.get_pos(),True)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    startFlag = True       

        if startFlag:
            bfs()
            
            if len(openSet) > 0:
                # print("entered")
                winner = 0
                for i in range(len(openSet)):
                    if openSet[i].f < openSet[winner].f:
                        winner = i

                current = openSet[winner]
                # print(current.x, current.y)
                if current == end:
                    temp = current
                    while temp.prev:
                        path.append(temp.prev)
                        temp = temp.prev 
                    if not astarFlag:
                        astarFlag = True
                        print("Done")
                    elif astarFlag:
                        continue

                if astarFlag == False:
                    openSet.remove(current)
                    closeSet.append(current)

                    for neighbor in current.neighbors:
                        if neighbor in closeSet or neighbor.wall:
                            continue
                        tempG = current.g + 1

                        newPath = False
                        if neighbor in openSet:
                            if tempG < neighbor.g:
                                neighbor.g = tempG
                                newPath = True
                        else:
                            neighbor.g = tempG
                            newPath = True
                            openSet.append(neighbor)
                        
                        if newPath:
                            neighbor.h = heuristics(neighbor, end)
                            neighbor.f = neighbor.g + neighbor.h
                            neighbor.prev = current

            else:
                if noFlag:
                    Tk().wm_withdraw()
                    messagebox.showinfo("No Solution astar", "There was no solution" )
                    noFlag = False

    
    
        # win.fill((0, 20, 20))
        # for i in range(cols):
        #     for j in range(rows):
        #         spot = grid[i][j]
        #         spot.show(win, (255, 255, 255))
        #         if spot in path:
        #             spot.show(win, (25, 120, 250))
        #         if spot in astarPath:
        #             spot.show(win, (25, 120, 250))
                    
        #         if spot == start:
        #             spot.show(win, (0, 255, 0))
        #         if spot == end:
        #             spot.show(win, (0, 120, 255))
        win.fill((0, 20, 20))
        for i in range(cols):
            for j in range(rows):
                spot = grid[i][j]
                spot.show(win, (255, 255, 255))
                try:

                    if spot == start:
                        spot.show(win,(255,20,147))
                except Exception:
                    pass
                if spot in bfspath:
                    spot.show(win, (0, 255, 0))
                if flag and spot in path:
                    spot.show(win, (25, 120, 250))
                
                # elif spot in closeSet:
                #     spot.show(win, (255, 0, 0))
                # elif spot in openSet:
                #     spot.show(win, (0, 255, 0))
                try:
                    if spot == end:
                        spot.show(win, (0, 120, 255))
                except Exception:
                    pass
        
           
        pygame.display.flip()

main()