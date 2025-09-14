from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
  from procgen import Room

import numpy as np
from tcod.console import Console

import tile

class WorldMap:
  def __init__(self, width: int, height: int):
    self.width = width
    self.height = height
    self.tiles = np.full((width, height), fill_value=tile.floor, order="F")
  def place_room(self, room: Room) -> None:
    self.tiles[room.outer] = tile.wall
    self.tiles[room.inner] = tile.floor
  def in_bounds(self, x: int, y: int) -> bool:
    return 0 <= x < self.width and 0 <= y < self.height
  def render(self, console: Console) -> None:
    console.rgb[0:self.width, 0:self.height] = self.tiles["dark"]