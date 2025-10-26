# hello_world.py
import sys

def hello_world(name: str = "World") -> str:
    """
    Returns a friendly greeting message.

    Parameters:
    -----------
    name : str, optional
        The name of the person or thing to greet. Default is "World".

    Returns:
    --------
    str
        A greeting string.
    """
    if not isinstance(name, str):
        raise TypeError("name must be a string")
    name = name.strip() or "World"
    return f"Hello, {name}! 👋"


if __name__ == "__main__":
    if len(sys.argv) > 1:
        # If a name is passed as a command-line argument, greet it
        print(hello_world(" ".join(sys.argv[1:])))
    else:
        # Default usage examples
        print(hello_world())
        print(hello_world("GitHub"))
        print(hello_world("Hacktoberfest Contributor"))
