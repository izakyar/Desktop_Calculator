from rich.console import Console
console = Console()

"""
Basic Output but richer, makes debugging easier and prettier
ToDO:
None... (yet...)
"""

def yay(msg: str) -> None:
    console.log(f"[green] [✓] [/] {msg}")
    return None

def nay(msg: str) -> None:
    console.log(f"[red] [✗] [/] {msg}")
    return None

def info(msg: str) -> None:
    console.log(f"[blue] (i) [/] {msg}")

def out(msg: str) -> None:
    console.log(f"[green] [✓] [/]\n {msg}")






