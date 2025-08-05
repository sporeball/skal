#!/usr/bin/env python3
import tcod

from actions import MoveAction, QuitAction
from entity import Entity
from input_handlers import EventHandler

def main() -> None:
  columns = 40
  rows = 30

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

  with tcod.context.new(
    columns=columns,
    rows=rows,
    tileset=tileset,
    title="Skål",
  ) as context:
    root_console = tcod.console.Console(columns, rows, order="F")
    while True:
      root_console.print(x=player.x, y=player.y, text=player.char, fg=player.color)
      context.present(root_console)
      root_console.clear()
      for event in tcod.event.wait():
        action = event_handler.dispatch(event)
        if action is None:
          continue
        if isinstance(action, MoveAction):
          player.move(dx=action.dx, dy=action.dy)
        elif isinstance(action, QuitAction):
          raise SystemExit()

if __name__ == "__main__":
  main()