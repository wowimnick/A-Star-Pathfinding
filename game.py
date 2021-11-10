import sys
import pygame
from pygame import event

w = 1400
h = 800

GRAY = (100, 100, 100)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

nodesx = []
nodesy = []
startnode = []
endnode = []
wall = []
neighbors = []
move = []

display = pygame.display.set_mode((w, h))
pygame.init()
surface = pygame.display.set_mode((w, h))

surface.fill((2, 0, 50))

nodeSize = 20
for x in range(0, w, nodeSize):  # Loops through the GUI width in steps of 20 and appends the values in the nodesx array
    for y in range(0, h, nodeSize):  # Same as above but for y, appends in nodesy array
        node = pygame.Rect(x, y, nodeSize, nodeSize)

        pygame.draw.rect(surface, BLACK, node, 1)  # Draws the grid
        nodesx.append(x)
        nodesy.append(y)

while True:
    pygame.display.flip()
    for event in pygame.event.get():
        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            for x, y in zip(nodesx, nodesy):
                if x - 0 < pos[0] < x + 20 and y - 0 < pos[1] < y + 20:
                    startnode.append(x)
                    startnode.append(y)
                    if len(startnode) == 2:
                        node2 = pygame.Rect(x, y, nodeSize, nodeSize)
                        pygame.draw.rect(surface, GREEN, node2, 1)
                    elif len(startnode) > 2:
                        node2 = pygame.Rect(startnode[0], startnode[1], nodeSize, nodeSize)
                        pygame.draw.rect(surface, BLACK, node2, 1)
                        startnode.clear()
                        neighbors.clear()

        elif pygame.mouse.get_pressed()[2]:
            pos = pygame.mouse.get_pos()
            for x, y in zip(nodesx, nodesy):
                if x - 0 < pos[0] < x + 20 and y - 0 < pos[1] < y + 20:
                    endnode.append(x)
                    endnode.append(y)
                    print(f"Endnode: {endnode}. Startnode {startnode}.")
                    print("Distance: " + str((endnode[0]-startnode[0])/20))
                    if len(endnode) == 2:
                        node2 = pygame.Rect(x, y, nodeSize, nodeSize)
                        pygame.draw.rect(surface, RED, node2, 1)
                    elif len(endnode) > 2:
                        node2 = pygame.Rect(endnode[0], endnode[1], nodeSize, nodeSize)
                        pygame.draw.rect(surface, BLACK, node2, 1)
                        endnode.clear()

        if pygame.mouse.get_pressed()[1]:
            pos = pygame.mouse.get_pos()
            for x, y in zip(nodesx, nodesy):
                if x - 0 < pos[0] < x + 20 and y - 0 < pos[1] < y + 20:
                    wall.append(x)
                    wall.append(y)
                    node2 = pygame.Rect(x, y, nodeSize, nodeSize)
                    pygame.draw.rect(surface, WHITE, node2, 3)

    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
