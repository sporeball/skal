from typing import Tuple

import tile
from world_map import WorldMap

class Room:
  """
  A rectangular room.
  `x1` is the top left corner of the outside wall.
  `width` and `height` include the outside wall.
  """
  def __init__(self, x: int, y: int, width: int, height: int):
    self.x1 = x
    self.y1 = y
    self.x2 = x + width
    self.y2 = y + height
  @property
  def outer(self) -> Tuple[slice, slice]:
    return slice(self.x1, self.x2), slice(self.y1, self.y2)
  @property
  def inner(self) -> Tuple[slice, slice]:
    return slice(self.x1 + 1, self.x2 - 1), slice(self.y1 + 1, self.y2 - 1)
  @property
  def center(self) -> Tuple[int, int]:
    return int((self.x1 + self.x2 - 1) / 2), int((self.y1 + self.y2 - 1) / 2)

def generate_world_map(map_width: int, map_height: int) -> WorldMap:
  wm = WorldMap(map_width, map_height)
  r1 = Room(x=1, y=1, width=7, height=7)
  r2 = Room(x=10, y=15, width=9, height=9)
  wm.place_room(r1)
  wm.place_room(r2)
  wm.dig_tunnel(r1, r2)
  return wm