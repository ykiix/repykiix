import pygame as pg
import random

pg.init()

WIDTH, HEIGHT = 300, 600
GRID_SIZE = 30
FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)

SHAPES = [[[1, 1, 1, 1]], [[1, 1, 1], [1]], [[1, 1, 1], [0, 0, 1]], [
    [1, 1, 1], [0, 1]], [[1, 1, 1], [1, 0]], [[1, 1], [1, 1]], [[1, 1, 0], [0, 1, 1]]]

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Tetris")
clock = pg.time.Clock()


def draw_grid():
    for x in range(0, WIDTH, GRID_SIZE):
        pg.draw.line(screen, WHITE, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, GRID_SIZE):
        pg.draw.line(screen, WHITE, (0, y), (WIDTH, y))


def draw_tetromino(tetromino, position, color):
    for y, row in enumerate(tetromino):
        for x, value in enumerate(row):
            if value:
                pg.draw.rect(screen, color, ((
                    position[0]+x)*GRID_SIZE, (position[1]+y)*GRID_SIZE, GRID_SIZE, GRID_SIZE))


def check_collision(tetromino, position, board):
    for y, row in enumerate(tetromino):
        for x, value in enumerate(row):
            if value and (position[0]+x < 0 or position[0]+x >= WIDTH//GRID_SIZE or position[1]+y >= HEIGHT//GRID_SIZE or board[position[1]+y][position[0]+x]):
                return True
    return False


def merge_tetromino(tetromino, position, board):
    for y, row in enumerate(tetromino):
        for x, value in enumerate(row):
            if value:
                board[position[1]+y][position[0]+x] = 1


def remove_completed_rows(board):
    completed_rows = [i for i, row in enumerate(board) if all(row)]
    for row in completed_rows:
        del board[row]
        board.insert(0, [0]*(WIDTH//GRID_SIZE))
    return len(completed_rows)


def draw_board(board):
    for y, row in enumerate(board):
        for x, value in enumerate(row):
            if value:
                pg.draw.rect(screen, WHITE, (x*GRID_SIZE, y *
                             GRID_SIZE, GRID_SIZE, GRID_SIZE))


def main():
    board = [[0]*(WIDTH//GRID_SIZE) for _ in range(HEIGHT//GRID_SIZE)]
    current_tetromino = random.choice(SHAPES)
    current_position = [WIDTH//(2*GRID_SIZE)-1, 0]
    current_color = random.choice(
        [RED, CYAN, MAGENTA, YELLOW, GREEN, BLUE, ORANGE])

    game_over = False
    while not game_over:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_over = True
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    new_position = [current_position[0]-1, current_position[1]]
                    if not check_collision(current_tetromino, new_position, board):
                        current_position = new_position
                elif event.key == pg.K_RIGHT:
                    new_position = [current_position[0]+1, current_position[1]]
                    if not check_collision(current_tetromino, new_position, board):
                        current_position = new_position
                elif event.key == pg.K_DOWN:
                    new_position = [current_position[0], current_position[1]+1]
                    if not check_collision(current_tetromino, new_position, board):
                        current_position = new_position
                elif event.key == pg.K_UP:
                    rotated_tetromino = list(zip(*reversed(current_tetromino)))
                    if not check_collision(rotated_tetromino, current_position, board):
                        current_tetromino = rotated_tetromino

        new_position = [current_position[0], current_position[1]+1]
        if not check_collision(current_tetromino, new_position, board):
            current_position = new_position
        else:
            merge_tetromino(current_tetromino, current_position, board)
            lines_cleared = remove_completed_rows(board)
            if lines_cleared > 0:
                print(f"Lines cleared: {lines_cleared}")
            current_tetromino = random.choice(SHAPES)
            current_position = [WIDTH//(2*GRID_SIZE)-1, 0]
            current_color = random.choice(
                [RED, CYAN, MAGENTA, YELLOW, GREEN, BLUE, ORANGE])

            if check_collision(current_tetromino, current_position, board):
                game_over = True

        screen.fill(BLACK)
        draw_grid()
        draw_tetromino(current_tetromino, current_position, current_color)
        draw_board(board)
        pg.display.flip()

        clock.tick(FPS)

    pg.quit()


if __name__ == "__main__":
    main()
