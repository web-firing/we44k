import pyfiglet
from rich.console import Console
from rich.align import Align

console = Console()
ascii_art = pyfiglet.figlet_format("SKANDER I9LIDS") 
console.print(ascii_art, style="bold red")


text = Align.center("[bold green]Developed by Benabbe Ahmed Yacine[/bold green]", width=60)
console.print(text)
