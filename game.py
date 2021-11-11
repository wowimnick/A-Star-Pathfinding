import sys
import pygame
from pygame import event
import time
import numpy as np

GRAY = (100, 100, 100)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)


class Game:
    def __init__(self, w=1400, h=800, nodeSize=20):
        self.display = pygame.display.set_mode((w, h))
        pygame.init()
        self.surface = pygame.display.set_mode((w, h))
        self.nodeSize = nodeSize
        self.surface.fill((2, 0, 50))

        self.w = w
        self.h = h
        self.nodes = []
        self.startnode = []
        self.endnode = []
        self.walls = []
        self.neighbors = []
        self.move = []

    def drawgrid(self):
        for x in range(0, self.w,
                       self.nodeSize):  # Loops through the GUI width in steps of 20 and appends the values in the nodesx array
            for y in range(0, self.h, self.nodeSize):  # Same as above but for y, appends in nodesy array
                node = pygame.Rect(x, y, self.nodeSize, self.nodeSize)

                pygame.draw.rect(self.surface, BLACK, node, 1)  # Draws the grid
                self.nodes.append((x, y))
                # pygame.display.flip()

    def game(self):
        global event
        while True:
            pygame.display.flip()
            for event in pygame.event.get():
                if pygame.mouse.get_pressed()[0]:
                    pos = pygame.mouse.get_pos()
                    for x, y in self.nodes:
                        if x - 0 < pos[0] < x + 20 and y - 0 < pos[1] < y + 20:
                            self.startnode.append((x, y))
                            self.move.append((x, y))

                            if len(self.startnode) == 1:
                                node2 = pygame.Rect(x, y, self.nodeSize, self.nodeSize)
                                pygame.draw.rect(self.surface, GREEN, node2, 1)
                                game.algorithm()

                            elif len(self.startnode) > 1:
                                node2 = pygame.Rect(self.startnode[0][0], self.startnode[0][1], self.nodeSize,
                                                    self.nodeSize)
                                pygame.draw.rect(self.surface, BLACK, node2, 1)
                                self.startnode.clear()
                                self.neighbors.clear()

                elif pygame.mouse.get_pressed()[2]:
                    pos = pygame.mouse.get_pos()
                    for x, y in self.nodes:
                        if x - 0 < pos[0] < x + 20 and y - 0 < pos[1] < y + 20:
                            self.endnode.append((x, y))
                            print(f"Endnode: {self.endnode}. Startnode {self.startnode}.")
                            # print("Distance: " + str((self.endnode[0][0] - self.startnode[0][1]) / 20))

                            if len(self.endnode) == 1:
                                node2 = pygame.Rect(x, y, self.nodeSize, self.nodeSize)
                                pygame.draw.rect(self.surface, RED, node2, 1)

                            elif len(self.endnode) > 1:
                                node2 = pygame.Rect(self.endnode[0][0], self.endnode[0][1], self.nodeSize,
                                                    self.nodeSize)
                                pygame.draw.rect(self.surface, BLACK, node2, 1)
                                self.endnode.clear()

                if pygame.mouse.get_pressed()[1]:
                    pos = pygame.mouse.get_pos()
                    for x, y in self.nodes:
                        if x - 0 < pos[0] < x + 20 and y - 0 < pos[1] < y + 20:
                            self.walls.append((x, y))
                            node2 = pygame.Rect(x, y, self.nodeSize, self.nodeSize)
                            pygame.draw.rect(self.surface, WHITE, node2, 3)

                    # for wall in self.walls:
                    #   for i, node in enumerate(self.nodes):
                    #       if wall == node:
                    #           self.nodes.pop(i)

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def algorithm(self):
        while self.move != self.endnode:
            # self.nodes.pop(2)
            start = self.nodes.index(self.startnode[0])
            test = self.nodes.index(self.move[0])
            end = self.nodes.index(self.endnode[0])

            up = self.nodes[test - 1]
            down = self.nodes[test + 1]
            left = self.nodes[test + 40]
            right = self.nodes[test - 40]

            nodeup = pygame.Rect(up[0], up[1], self.nodeSize, self.nodeSize)
            nodedown = pygame.Rect(down[0], down[1], self.nodeSize, self.nodeSize)
            noderight = pygame.Rect(right[0], right[1], self.nodeSize, self.nodeSize)
            nodeleft = pygame.Rect(left[0], left[1], self.nodeSize, self.nodeSize)

            pygame.draw.rect(self.surface, BLUE, noderight, 1)
            pygame.draw.rect(self.surface, BLUE, nodeleft, 1)
            pygame.draw.rect(self.surface, BLUE, nodeup, 1)
            pygame.draw.rect(self.surface, BLUE, nodedown, 1)

            hcostup = abs((test - 1) - end) #+ ((test - 1) - start))  # Need to give the distance to endnode
            hcostdown = abs((test + 1) - end) #+ ((test + 1) - start))
            hcostleft = abs((test + 40) - end) #+ ((test + 40) - start))
            hcostright = abs((test - 40) - end) #+ ((test - 40) - start))

            self.neighbors.clear()
            self.move.clear()

            self.neighbors.append((hcostup, hcostdown, hcostleft, hcostright))
            print(self.neighbors)
            if np.amin(self.neighbors) == self.neighbors[0][0]:
                self.move.append(up)
            elif np.amin(self.neighbors) == self.neighbors[0][1]:
                self.move.append(down)
            elif np.amin(self.neighbors) == self.neighbors[0][2]:
                self.move.append(left)
            elif np.amin(self.neighbors) == self.neighbors[0][3]:
                self.move.append(right)

            nextmove = pygame.Rect(self.move[0][0], self.move[0][1], self.nodeSize, self.nodeSize)
            pygame.draw.rect(self.surface, RED, nextmove, 1)
            pygame.display.flip()

            time.sleep(0.01)


if __name__ == "__main__":
    game = Game()
    game.drawgrid()
    game.game()
