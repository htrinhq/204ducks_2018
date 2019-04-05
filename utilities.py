##
## EPITECH PROJECT, 2019
## 204ducks_2018
## File description:
## utilities
##

from sys import stderr

def error(str: str) -> None:
    """Exits with str on error output."""
    stderr.write(str)
    exit(84)


def usage() -> None:
    """Displays usage."""
    print('USAGE\n\t./204ducks a\n')
    print('DESCRIPTION\n\ta\tconstant')
