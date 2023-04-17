# imports necessary for building CLI
import typer
from pathlib import Path
# import files needed for functionality
import scanner

cli = typer.Typer()

@cli.command()
def main(
    python_file = typer.Argument(...),
    #output_file = typer.Option(None),
    ):
    
    # blank line
    print()
    python_path = Path(python_file)

    # check if user provided python_file argument
    if python_path is None:
        print("\n\tNo input file was given.\n")
        raise typer.Abort()
    
    # check if python_file argument is a file
    if python_path.is_file():
        python_text = python_path.read_text()
    else:
        print("\n\tThis file does not exist.\n")
    scanner.scanner(python_text).scan()
    my_scanner = scanner.Scanner(python_text)
    my_scanner.scan()
    

