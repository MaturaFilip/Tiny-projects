import typer

app = typer.Typer()

@app.command()
def add(x: int, y: int):
    """Add two numbers."""
    typer.echo(f"Result: {x + y}")
