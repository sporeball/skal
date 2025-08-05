from typing import Optional
from actions import Action, QuitAction, MoveAction

import tcod.event

class EventHandler:
  def dispatch(self, event: tcod.event.Event) -> None:
    match event:
      case tcod.event.Quit():
        raise SystemExit()
      case tcod.event.KeyDown():
        action: Optional[Action] = None
        match event.sym:
          case tcod.event.KeySym.UP:
            action = MoveAction(dx=0, dy=-1)
          case tcod.event.KeySym.DOWN:
            action = MoveAction(dx=0, dy=1)
          case tcod.event.KeySym.LEFT:
            action = MoveAction(dx=-1, dy=0)
          case tcod.event.KeySym.RIGHT:
            action = MoveAction(dx=1, dy=0)
          case tcod.event.KeySym.ESCAPE:
            action = QuitAction()

        return action