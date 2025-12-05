import typer
import os
from typing import Optional
from rich.console import Console
from .client import TuulClient
from .exceptions import TuulError

app = typer.Typer()
console = Console()

def get_client(api_key: Optional[str]) -> TuulClient:
    key = api_key or os.getenv("TUUL_API_KEY")
    if not key:
        console.print("[red]Error:[/red] TUUL_API_KEY not found.")
        raise typer.Exit(code=1)
    return TuulClient(api_key=key)

@app.command()
def generate(prompt: str, api_key: Optional[str] = None):
    """Test the Generative API."""
    client = get_client(api_key)
    try:
        with console.status("Generating response..."):
            resp = client.generative.create(prompt=prompt)
        console.print(f"[bold green]Response:[/bold green] {resp.content}")
        console.print(f"[dim]Usage: {resp.usage}[/dim]")
    except TuulError as e:
        console.print(f"[bold red]API Error:[/bold red] {e}")

if __name__ == "__main__":
    app()