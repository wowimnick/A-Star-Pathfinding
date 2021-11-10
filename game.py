import sys
import pygame
from pygame import event

GRAY = (100, 100, 100)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
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

                            if len(self.startnode) == 1:
                                node2 = pygame.Rect(x, y, self.nodeSize, self.nodeSize)
                                pygame.draw.rect(self.surface, GREEN, node2, 1)

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
                            print("Distance: " + str((self.endnode[0][0] - self.startnode[0][1]) / 20))

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
                            print(self.nodes)

                    for wall in self.walls:
                        for i, node in enumerate(self.nodes):
                            if wall == node:
                                self.nodes.pop(i)






            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()




if __name__ == "__main__":
    game = Game()
    game.drawgrid()
    game.game()
