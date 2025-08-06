from typing import Set, Iterable, Any

from tcod.context import Context
from tcod.console import Console

from actions import QuitAction, MoveAction
from entity import Entity
from input_handlers import EventHandler
from world_map import WorldMap

class Engine:
  def __init__(self, entities: Set[Entity], event_handler: EventHandler, player: Entity, world_map: WorldMap):
    self.entities = entities
    self.event_handler = event_handler
    self.player = player
    self.world_map = world_map
  def handle_events(self, events: Iterable[Any]) -> None:
    for event in events:
      action = self.event_handler.dispatch(event)
      if action is None:
        continue
      if isinstance(action, MoveAction):
        if self.world_map.tiles["walkable"][self.player.x + action.dx, self.player.y + action.dy]:
          self.player.move(dx=action.dx, dy=action.dy)
      elif isinstance(action, QuitAction):
        raise SystemExit()
  def render(self, console: Console, context: Context) -> None:
    self.world_map.render(console)
    for entity in self.entities:
      console.print(x=entity.x, y=entity.y, text=entity.char, fg=entity.color)
    context.present(console)
    console.clear()
