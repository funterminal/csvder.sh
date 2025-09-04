import sys
import csv
from rich.console import Console
from rich.table import Table
from rich import box
from rich.panel import Panel
from rich.prompt import Prompt
from rich.layout import Layout
from rich.text import Text

console = Console()

def read_csv_file(file_path):
    try:
        with open(file_path, newline='', encoding='utf-8') as f:
            reader = list(csv.reader(f))
            if not reader:
                console.print(f"[bold yellow]Warning:[/bold yellow] The file '{file_path}' contains no data.")
                return [], []
            headers = reader[0]
            rows = reader[1:]
            return headers, rows
    except FileNotFoundError:
        console.print(f"[bold red]Error:[/bold red] File '{file_path}' not found.")
        sys.exit(1)
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        sys.exit(1)

def render_csv(file_path):
    headers, rows = read_csv_file(file_path)
    if not headers:
        return

    layout = Layout()
    layout.split(
        Layout(name="header", size=3),
        Layout(name="body"),
        Layout(name="footer", size=3)
    )

    layout["header"].update(Panel(Text("CSVDER - Lightweight CSV Renderer", justify="center", style="bold white on blue")))

    table = Table(show_header=True, header_style="bold magenta", box=box.DOUBLE_EDGE)
    for col in headers:
        table.add_column(col, overflow="fold")

    row_limit = 50
    for row in rows[:row_limit]:
        table.add_row(*row)

    layout["body"].update(table)
    layout["footer"].update(Panel(f"Showing first {min(row_limit, len(rows))} rows out of {len(rows)} | Columns: {len(headers)}", style="dim"))

    console.print(layout)

    while True:
        action = Prompt.ask("[bold green]What would you like to do next?[/bold green]", choices=["search", "head", "tail", "exit"])

        if action == "search":
            query = Prompt.ask("Enter text to search")
            results = [row for row in rows if any(query.lower() in cell.lower() for cell in row)]
            if not results:
                console.print(f"[italic red]No results found for '{query}'[/italic red]")
            else:
                preview = results[:row_limit]
                mini_table = Table(show_header=True, header_style="bold green", box=box.SIMPLE_HEAVY)
                for col in headers:
                    mini_table.add_column(col, overflow="fold")
                for row in preview:
                    mini_table.add_row(*row)
                console.print(Panel(mini_table, title=f"Search Results for '{query}'", border_style="green"))

        elif action == "head":
            n = int(Prompt.ask("How many rows from top?", default="5"))
            head_table = Table(show_header=True, header_style="bold blue", box=box.SIMPLE)
            for col in headers:
                head_table.add_column(col, overflow="fold")
            for row in rows[:n]:
                head_table.add_row(*row)
            console.print(Panel(head_table, title="Top Rows", border_style="blue"))

        elif action == "tail":
            n = int(Prompt.ask("How many rows from bottom?", default="5"))
            tail_table = Table(show_header=True, header_style="bold yellow", box=box.SIMPLE)
            for col in headers:
                tail_table.add_column(col, overflow="fold")
            for row in rows[-n:]:
                tail_table.add_row(*row)
            console.print(Panel(tail_table, title="Bottom Rows", border_style="yellow"))

        elif action == "exit":
            console.print("[bold green]Goodbye![/bold green]")
            break

def main():
    if len(sys.argv) != 3 or sys.argv[1] != "render" or not sys.argv[2].endswith(".csv"):
        console.print("[bold cyan]Usage:[/bold cyan] csvder render <filename>.csv")
        sys.exit(1)

    filename = sys.argv[2]
    render_csv(filename)

if __name__ == "__main__":
    main()