from typing import Optional


def setCommand(cmd: str,  issuer: Optional[str] = None, priority: Optional[int] = 0):
    print(cmd, priority, issuer)


setCommand(cmd="run", priority=1)
setCommand(cmd="run")
setCommand(cmd="run", priority=1, issuer="lek")
