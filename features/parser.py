import csv


def pretty_func(variable: str = "") -> bool:
    if variable != "":
        return True
    else:
        return False

def print_something() -> None:
    print(f"Jestem {__name__}")