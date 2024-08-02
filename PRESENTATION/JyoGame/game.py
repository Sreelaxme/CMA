import pygame
from grid import Grid
from search import *
 
  
pygame.init()
 
display_width = 800
display_height = 600

class Colors:
    ORANGE = (255,100,100)
    GREEN = (0,255,0)
    GREENISH = (0,150,0)
    BLUE = (0,0,255)
    BLUEISH = (0,0,150)
    RED = (255,0,0)

 
screen = pygame.display.set_mode((display_width, display_height))



grid = Grid()
cellLength = 10

def GameToGrid(x,y): 
    return (x//cellLength, y//cellLength)

def GridToGame(x,y):
    return (x*cellLength, y*cellLength)

def GridCell(x,y):
    x,y = GridToGame(x,y)
    return (x, y, cellLength, cellLength)

def GridCellCenter(x,y):
    return (x+cellLength//2, y+cellLength//2)


start = (0,0)
end = (0,0)

search = AStar(grid)

pathNodes = []
frontier = set()
expanded = set()

def updateFronter(node):
    frontier.add(node)
    Draw()

def updateExpanded(node):
    expanded.add(node)
    Draw()


## Draw borders
for x in range(display_width//cellLength):
    grid[x,0] = GridCell(x,0)
    grid[x,display_height//cellLength - 1] = GridCell(x,display_height//cellLength - 1)

for y in range(display_height//cellLength):
    grid[0,y] = GridCell(0,y)
    grid[display_width//cellLength - 1,y] = GridCell(display_width//cellLength - 1,y)
 


def Draw():
    # Draw grid
    for obj in grid.objToPos:
        pygame.draw.rect(screen, Colors.ORANGE, pygame.Rect(*obj))

    # Draw target and search
    pygame.draw.circle(screen, Colors.GREEN, GridCellCenter(*GridToGame(*start)), cellLength//2)
    pygame.draw.circle(screen, Colors.BLUE, GridCellCenter(*GridToGame(*end)), cellLength//2)

    for pt in frontier:
        pygame.draw.rect(screen, Colors.GREENISH, pygame.Rect(*GridCell(*pt)))

    for pt in expanded:
        pygame.draw.rect(screen, Colors.RED, pygame.Rect(*GridCell(*pt)))

    # Draw Path
    if search.targetFound:
        for node in pathNodes:
            pos = GridToGame(*node)
            pygame.draw.circle(screen, Colors.BLUEISH, GridCellCenter(*pos), cellLength/3)
    
 
    pygame.display.update()


while True:
    screen.fill((255,255,255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (
            event.type == pygame.KEYDOWN and (
                event.key == pygame.K_ESCAPE or
                event.key == pygame.K_q
                )
            ):
            pygame.quit()
            quit()

        # Move target and start
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                end = GameToGrid(*pygame.mouse.get_pos())
                
            if event.key == pygame.K_e:
                start = GameToGrid(*pygame.mouse.get_pos())

            if event.key == pygame.K_RETURN:
                frontier.clear()
                expanded.clear()
                pathNodes = []
                search.RunSearch(start, end, [updateExpanded], [updateFronter])
                pathNodes = search.GetPathNodes()


    # On click
    if pygame.mouse.get_pressed()[0]:
        mousePos = pygame.mouse.get_pos()
        mouseGridPos = GameToGrid(*mousePos)
        grid[mouseGridPos] = GridCell(*mouseGridPos)

    # On right click
    if pygame.mouse.get_pressed()[2]:
        mousePos = pygame.mouse.get_pos()
        mouseGridPos = GameToGrid(*mousePos)
        if grid[mouseGridPos] != None: 
            grid[mouseGridPos] = None

    Draw()