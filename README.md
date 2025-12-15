# quickstart-package

A quickstart Python package template using pyenv and uv.

## Prerequisites

- [pyenv](https://github.com/pyenv/pyenv) for Python version management
- [uv](https://github.com/astral-sh/uv) for fast Python package management

## Setup

1. Install the required Python version:
   ```bash
   pyenv install 3.12
   ```

2. Create and activate a virtual environment:
   ```bash
   uv venv
   source .venv/bin/activate  # On Unix/macOS
   # or
   .venv\Scripts\activate     # On Windows
   ```

3. Install the package in development mode with dev dependencies:
   ```bash
   uv pip install -e ".[dev]"
   ```

## Development

### Running tests

```bash
pytest
```

With coverage:

```bash
pytest --cov
```

### Linting and formatting

```bash
ruff check .
ruff format .
```

### Type checking

```bash
mypy src
```

## Project Structure

```
quickstart-package/
├── src/
│   └── quickstart_package/
│       ├── __init__.py
│       └── py.typed
├── tests/
│   ├── __init__.py
│   └── test_main.py
├── .gitignore
├── .python-version
├── pyproject.toml
└── README.md
```

## License

MIT
