import typer

app = typer.Typer()

@app.command()
def hello(name: str = typer.Option("Hello", "--greet", "-g", help = "Your name")):
    """Say hello"""
    typer.echo(f"Hello, {name}!")