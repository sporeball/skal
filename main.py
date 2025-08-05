#!/usr/bin/env python3
import tcod

def main() -> None:
  columns = 40
  rows = 30
  player_x = int(columns / 2) - 1
  player_y = int(rows / 2) - 1

  tileset = tcod.tileset.load_tilesheet(
    "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
  )

  with tcod.context.new(
    columns=columns,
    rows=rows,
    tileset=tileset,
    title="Skål",
  ) as context:
    root_console = tcod.console.Console(columns, rows, order="F")
    while True:
      root_console.print(x=player_x, y=player_y, text="@")
      context.present(root_console)
      for event in tcod.event.wait():
        if event.type == "QUIT":
          raise SystemExit()

if __name__ == "__main__":
  main()