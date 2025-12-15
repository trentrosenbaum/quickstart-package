"""Tests for the quickstart package."""

from quickstart_package import __version__, goodbye, hello


def test_version() -> None:
    """Test that version is defined."""
    assert __version__ == "0.1.0"


def test_hello_default() -> None:
    """Test hello with default argument."""
    assert hello() == "Hello, World!"


def test_hello_with_name() -> None:
    """Test hello with custom name."""
    assert hello("Python") == "Hello, Python!"


def test_goodbye_default() -> None:
    """Test goodbye with default argument."""
    assert goodbye() == "Goodbye, World!"


def test_goodbye_with_name() -> None:
    """Test goodbye with custom name."""
    assert goodbye("Python") == "Goodbye, Python!"
