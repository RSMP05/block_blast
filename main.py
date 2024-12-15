import sys
import pygame as pg
import settings
import sprites
import random
import blocks

pg.init()

screen = pg.display.set_mode(settings.WIN_SIZE)
pg.display.set_caption("Block Blast")
clock = pg.time.Clock()

def draw_element(color, x, y):
  if color == 0:
    screen.blit(sprites.EMPTY_SPRITE, ((x + 1) * settings.CELL_SIZE, (y + 2) * settings.CELL_SIZE))
  elif color == 1:
    screen.blit(sprites.RED_SPRITE, ((x + 1) * settings.CELL_SIZE, (y + 2) * settings.CELL_SIZE))
  elif color == 2:
    screen.blit(sprites.GREEN_SPRITE, ((x + 1) * settings.CELL_SIZE, (y + 2) * settings.CELL_SIZE))
  elif color == 3:
    screen.blit(sprites.BLUE_SPRITE, ((x + 1) * settings.CELL_SIZE, (y + 2) * settings.CELL_SIZE))
  elif color == 4:
    screen.blit(sprites.YELLOW_SPRITE, ((x + 1) * settings.CELL_SIZE, (y + 2) * settings.CELL_SIZE))

def draw_grid(grid):
  for y in range(len(grid)):
    for x in range(len(grid[y])):
      draw_element(grid[y][x], x, y)



def check_horizontal_line(grid, y, last_checked_time, current_time):
  if all(cell > 0 for cell in grid[y]):
    if last_checked_time == -1:
      last_checked_time = current_time
    if current_time - last_checked_time >= 200:
      for x in range(len(grid[y])):
        grid[y][x] = 0
      last_checked_time = -1
  return last_checked_time

def check_vertical_line(grid, x, last_checked_time, current_time):
  if all(grid[y][x] > 0 for y in range(len(grid))):
    if last_checked_time == -1:
      last_checked_time = current_time
    if current_time - last_checked_time >= 200:
      for y in range(len(grid)):
        grid[y][x] = 0
      last_checked_time = -1
  return last_checked_time

def main():
  running = True

  grid = [[0 for _ in range(8)] for _ in range(8)]

  curx, cury = 0, 0
  last_checked_time_h = [-1] * len(grid)
  last_checked_time_v = [-1] * len(grid[0])

  while running:
    current_time = pg.time.get_ticks()

    for event in pg.event.get():
      if event.type == pg.QUIT:
        running = False
      if event.type == pg.KEYDOWN:
        if event.key == pg.K_w and cury > 0:
          cury -= 1
        elif event.key == pg.K_s and cury < len(grid) - 1:
          cury += 1
        elif event.key == pg.K_a and curx > 0:
          curx -= 1
        elif event.key == pg.K_d and curx < len(grid[0]) - 1:
          curx += 1
        elif event.key == pg.K_l:
        	grid = [[0 for _ in range(8)] for _ in range(8)]
        elif event.key == pg.K_e:
        	blocks.add_block(grid, blocks.arr[random.randint(0, len(blocks.arr)-1)],random.randint(1,4), curx, cury)

    screen.fill(settings.BACKGROUND)

    draw_grid(grid)

    for row in range(len(grid)):
      last_checked_time_h[row] = check_horizontal_line(grid, row, last_checked_time_h[row], current_time)

    for col in range(len(grid[0])):
      last_checked_time_v[col] = check_vertical_line(grid, col, last_checked_time_v[col], current_time)

      blocks.initialise(curx, cury)

    pg.display.flip()
    clock.tick(settings.FPS)

  pg.quit()
  sys.exit()

if __name__ == "__main__":
  main()
