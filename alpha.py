import pyfiglet
from rich.console import Console
from rich.align import Align
print(pyfiglet.figlet_format("SKANDER I9LIDS"))
console = Console()
text = Align.center("[bold red] Developed by Benabbes Ahmed Yacine [/bold red]", width=60)
console.print(text)
