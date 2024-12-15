import pygame as pg
import settings
pg.init()

EMPTY_SPRITE = pg.image.load("sprites/empty_sprite.png")
EMPTY_SPRITE = pg.transform.scale(EMPTY_SPRITE, (settings.CELL_SIZE, settings.CELL_SIZE))

RED_SPRITE = pg.image.load("sprites/red_sprite.png")
RED_SPRITE = pg.transform.scale(RED_SPRITE, (settings.CELL_SIZE, settings.CELL_SIZE))

GREEN_SPRITE = pg.image.load("sprites/green_sprite.png")
GREEN_SPRITE = pg.transform.scale(GREEN_SPRITE, (settings.CELL_SIZE, settings.CELL_SIZE))

BLUE_SPRITE = pg.image.load("sprites/blue_sprite.png")
BLUE_SPRITE = pg.transform.scale(BLUE_SPRITE, (settings.CELL_SIZE, settings.CELL_SIZE))

YELLOW_SPRITE = pg.image.load("sprites/yellow_sprite.png")
YELLOW_SPRITE = pg.transform.scale(YELLOW_SPRITE, (settings.CELL_SIZE, settings.CELL_SIZE))
