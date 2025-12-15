"   ""Quickstart package template."""

__version__ = "0.1.0"


def hello(name: str = "World") -> str:
    """Return a greeting message.

    Args:
        name: The name to greet.

    Returns:
        A greeting string.
    """
    return f"Hello, {name}!"


def goodbye(name: str = "World") -> str:
    """Return a farewell message.

    Args:
        name: The name to bid farewell.

    Returns:
        A farewell string.
    """
    return f"Goodbye, {name}!"
