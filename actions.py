from __future__ import annotations # postpone
from typing import TYPE_CHECKING

if TYPE_CHECKING:
  from engine import Engine
  from entity import Entity

class Action:
  def perform(self, engine: Engine, entity: Entity) -> None:
    """
    Perform this action with the objects needed to determine its scope.
    This method must be overridden by all subclasses.
    """
    raise NotImplementedError()

class QuitAction(Action):
  def perform(self, engine: Engine, entity: Entity) -> None:
    raise SystemExit()

class MoveAction(Action):
  def __init__(self, dx: int, dy: int):
    super().__init__()
    self.dx = dx
    self.dy = dy
  def perform(self, engine: Engine, entity: Entity) -> None:
    dest_x = entity.x + self.dx
    dest_y = entity.y + self.dy

    if not engine.world_map.in_bounds(dest_x, dest_y):
      return
    if not engine.world_map.tiles["walkable"][dest_x, dest_y]:
      return

    entity.move(self.dx, self.dy)