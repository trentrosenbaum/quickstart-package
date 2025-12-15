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

## Building the Package

To build distribution packages (wheel and source distribution):

```bash
# Install the build tool
uv pip install build

# Build the package
python -m build
```

This creates two files in the `dist/` directory:
- `quickstart_package-0.1.0-py3-none-any.whl` (wheel)
- `quickstart_package-0.1.0.tar.gz` (source distribution)

## Installing the Built Package

### From a wheel file

```bash
pip install dist/quickstart_package-0.1.0-py3-none-any.whl
```

Or with uv:

```bash
uv pip install dist/quickstart_package-0.1.0-py3-none-any.whl
```

### Usage

Once installed, you can use the package in your Python code:

```python
from quickstart_package import hello, goodbye

# Greet someone
print(hello())          # Output: Hello, World!
print(hello("Python"))  # Output: Hello, Python!

# Say goodbye
print(goodbye())          # Output: Goodbye, World!
print(goodbye("Python"))  # Output: Goodbye, Python!
```

### Uninstalling

To remove the installed package:

```bash
pip uninstall quickstart-package
```

Or with uv:

```bash
uv pip uninstall quickstart-package
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
