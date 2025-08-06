#!/usr/bin/env python3
import tcod

from engine import Engine
from entity import Entity
from input_handlers import EventHandler
from world_map import WorldMap

def main() -> None:
  columns = 40
  rows = 30

  map_width = 40
  map_height = 30

  tileset = tcod.tileset.load_tilesheet(
    "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
  )

  event_handler = EventHandler()

  player = Entity(
    int(columns / 2),
    int(rows / 2),
    "@",
    (255, 255, 255),
  )
  entities = { player }

  world_map = WorldMap(map_width, map_height)

  engine = Engine(entities=entities, event_handler=event_handler, player=player, world_map=world_map)

  with tcod.context.new(
    columns=columns,
    rows=rows,
    tileset=tileset,
    title="Skål",
  ) as context:
    root_console = tcod.console.Console(columns, rows, order="F")
    while True:
      engine.render(console=root_console, context=context)
      events = tcod.event.wait()
      engine.handle_events(events)

if __name__ == "__main__":
  main()