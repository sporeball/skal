from __future__ import annotations
import random
from typing import TYPE_CHECKING, Iterator, Tuple

if TYPE_CHECKING:
  from procgen import Room

import numpy as np
import tcod

import tile

class WorldMap:
  def __init__(self, width: int, height: int):
    self.width = width
    self.height = height
    self.tiles = np.full((width, height), fill_value=tile.void, order="F")
  def neighbors(self, x: int, y: int) -> list[Tuple[int, int]]:
    return [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1), (x - 1, y), (x + 1, y), (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)]
  def void_neighbors(self, x: int, y: int) -> Iterator[Tuple[int, int]]:
    for nx, ny in self.neighbors(x, y):
      if np.array_equal(self.tiles[nx, ny], tile.void):
        yield nx, ny
  def place_room(self, room: Room) -> None:
    self.tiles[room.outer] = tile.wall
    self.tiles[room.inner] = tile.floor
  def dig_tunnel(self, r1: Room, r2: Room) -> None:
    # 0 < R < 0.5 :: horizontal, then vertical
    # 0.5 <= R < 1.0 :: vertical, then horizontal
    R = random.random()
    # room centers
    x1, y1 = r1.center
    x2, y2 = r2.center
    # find corner
    if R < 0.5:
      corner_x, corner_y = x2, y1
    else:
      corner_x, corner_y = x1, y2
    # find lines of sight
    l1 = tcod.los.bresenham((x1, y1), (corner_x, corner_y)).tolist()
    l2 = tcod.los.bresenham((corner_x, corner_y), (x2, y2)).tolist()
    # dig tunnel
    for x, y in l1 + l2:
      self.tiles[x, y] = tile.floor
      # for vx, vy in self.void_neighbors(x, y):
      #   self.tiles[vx, vy] = tile.wall
  def in_bounds(self, x: int, y: int) -> bool:
    return 0 <= x < self.width and 0 <= y < self.height
  def render(self, console: tcod.console.Console) -> None:
    console.rgb[0:self.width, 0:self.height] = self.tiles["dark"]