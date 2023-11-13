import pygame as pg


RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

DEAD = False
ALIVE = True


class GameOfLife(object):
    w_width, w_height = 600, 600
    r_width, r_height = 5, 5
    finished = False
    FPS = 60
    screen = pg.display.set_mode((w_width, w_height))

    def __init__(self) -> None:
        return

    def run(self) -> None:
        pg.init()
        pg.display.set_caption('Game of Life')
        x0 = 10
        y0 = 10

        clock = pg.time.Clock()
        t = 50
        while not self.finished:
            clock.tick(self.FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.finished = True
            self.screen.fill(BLACK)

            pg.draw.rect(self.screen, RED, (8, 8, 582, 582), 2)

            self.cell_size = 10
            self.height = 580
            self.width = 580
            self.c_height = self.height//self.cell_size
            self.c_width = self.width//self.cell_size
            self.cells_state = []
            for i in range(self.c_width):
                self.temp = []
                for j in range(self.c_height):
                    self.state = DEAD
                    self.temp.append(self.state)
                self.cells_state.append(self.temp)

            with open('cells.txt') as f:
                self.cells_state = f.readlines()
            for i in range(len(self.cells_state)):
                self.cells_state[i] = self.cells_state[i].split()
                for j in range(len(self.cells_state[i])):
                    self.cells_state[i][j] = int(self.cells_state[i][j])

            def Check_Index(i, j) -> bool:
                if i >= 0 and i < self.c_width and j >= 0 and j < self.c_height:
                    return True
                else:
                    return False
            for i in range(self.c_width):
                for j in range(self.c_height):
                    count = 0

                    if (Check_Index(i-1, j-1) and self.cells_state[i-1][j-1] == ALIVE):
                        count += 1

                    if (Check_Index(i, j-1) and self.cells_state[i][j-1] == ALIVE):
                        count += 1

                    if (Check_Index(i+1, j-1) and self.cells_state[i+1][j-1] == ALIVE):
                        count += 1

                    if (Check_Index(i-1, j) and self.cells_state[i-1][j] == ALIVE):
                        count += 1

                    if (Check_Index(i+1, j) and self.cells_state[i+1][j] == ALIVE):
                        count += 1

                    if (Check_Index(i-1, j+1) and self.cells_state[i-1][j+1] == ALIVE):
                        count += 1

                    if (Check_Index(i, j+1) and self.cells_state[i][j+1] == ALIVE):
                        count += 1

                    if (Check_Index(i+1, j+1) and self.cells_state[i+1][j+1] == ALIVE):
                        count += 1

                    if count != 2 and count != 3:
                        self.cells_state[i][j] = DEAD
                        count = 0
                    else:
                        count = 0

            def DrawCells() -> None:

                for i in range(self.c_width):
                    for j in range(self.c_height):
                        x2 = x0 + i*self.r_width
                        y2 = y0 + j*self.r_height
                        if self.cells_state[i][j] == DEAD:
                            pg.draw.rect(self.screen, BLACK, (x2, y2, 5, 5))
                        else:
                            pg.draw.rect(self.screen, GREEN, (x2, y2, 5, 5))

            DrawCells()
            pg.display.flip()
            pg.time.wait(t)
        pg.quit()
