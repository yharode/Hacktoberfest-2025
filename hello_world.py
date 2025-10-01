# hello_world.py

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
    return f"Hello, {name}! 👋"


if __name__ == "__main__":
    # Example usage
    print(hello_world())
    print(hello_world("GitHub"))
    print(hello_world("Hacktoberfest Contributor"))
