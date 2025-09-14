from typing import Tuple

import numpy as np # type: ignore

# tile graphics struct compatible with Console.rgb
graphic_data = np.dtype(
  [
    ("ch", np.int32),
    ("fg", "3B"),
    ("bg", "3B"),
  ]
)

# tile struct used for static tile data
tile_data = np.dtype(
  [
    ("walkable", np.bool), # True if this tile can be walked over
    ("transparent", np.bool), # True if this tile doesn't block FOV
    ("dark", graphic_data), # graphics for when this tile is not in FOV
  ]
)

def new_tile(
  *,
  walkable: int,
  transparent: int,
  dark: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
) -> np.ndarray:
  return np.array((walkable, transparent, dark), dtype=tile_data)

void = new_tile(
  walkable=True,
  transparent=True,
  dark=(ord(" "), (255, 255, 255), (0x12, 0x0E, 0x14)),
)
floor = new_tile(
  walkable=True,
  transparent=True,
  dark=(ord(" "), (255, 255, 255), (0x23, 0x17, 0x2D)),
)
wall = new_tile(
  walkable=False,
  transparent=False,
  dark=(ord(" "), (255, 255, 255), (0x5C, 0x4F, 0x7D)),
)