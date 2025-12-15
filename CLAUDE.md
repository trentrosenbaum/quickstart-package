# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Build and Development Commands

```bash
# Setup (requires pyenv and uv)
uv venv && source .venv/bin/activate
uv pip install -e ".[dev]"

# Run all tests
pytest

# Run tests with coverage
pytest --cov

# Run a single test file
pytest tests/test_main.py

# Run a specific test
pytest tests/test_main.py::test_hello_default

# Linting and formatting
ruff check .
ruff format .

# Type checking
mypy src
```

## Architecture

This is a Python package template using the src layout (`src/quickstart_package/`). It uses:
- **hatchling** as the build backend
- **uv** for package management
- **pyenv** for Python version management (Python 3.11+)
- **ruff** for linting/formatting
- **mypy** in strict mode for type checking
- **pytest** with coverage for testing

The package is configured with `py.typed` marker for PEP 561 type stub support.
