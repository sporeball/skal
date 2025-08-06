import numpy as np
from tcod.console import Console

import tile

class WorldMap:
  def __init__(self, width: int, height: int):
    self.width = width
    self.height = height
    self.tiles = np.full((width, height), fill_value=tile.floor, order="F")
    self.tiles[20:23, 10] = tile.wall
  def in_bounds(self, x: int, y: int) -> bool:
    return 0 <= x < self.width and 0 <= y < self.height
  def render(self, console: Console) -> None:
    console.rgb[0:self.width, 0:self.height] = self.tiles["dark"]