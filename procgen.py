from __future__ import annotations
import random
from typing import Iterator, Tuple, TYPE_CHECKING

if TYPE_CHECKING:
  from entity import Entity

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
  def intersects(self, other: Room) -> bool:
    return self.x1 <= other.x2 and self.x2 >= other.x1 and self.y1 <= other.y2 and self.y2 >= other.y1

def generate_world_map(
  map_width: int,
  map_height: int,
  max_rooms: int,
  min_room_size: int,
  max_room_size: int,
  player: Entity,
) -> WorldMap:
  wm = WorldMap(map_width, map_height)
  rooms: list[Room] = []
  for _ in range(max_rooms):
    room_width = random.randint(min_room_size, max_room_size)
    room_height = random.randint(min_room_size, max_room_size)
    x = random.randint(0, map_width - room_width - 1)
    y = random.randint(0, map_height - room_height - 1)
    room = Room(x, y, room_width, room_height)
    if any(room.intersects(other_room) for other_room in rooms):
      continue
    wm.place_room(room)
    rooms.append(room)
    # if len(rooms) >= 2:
    #   wm.dig_tunnel(rooms[-2], rooms[-1])
  player.x, player.y = rooms[0].center
  return wm