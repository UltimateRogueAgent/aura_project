# Pytest Documentation

The pytest framework makes it easy to write small tests, yet scales to support complex functional testing for applications and libraries.

## Installation

### Basic Installation

```bash
pip install -U pytest
```

### Verify Installation

```bash
pytest --version
```

## Quick Start

### Your First Test

```python
# content of test_sample.py
def func(x):
    return x + 1

def test_answer():
    assert func(3) == 4
```

### Run Tests

```bash
# Run all tests
pytest

# Run with quiet output
pytest -q

# Run specific test file
pytest test_sample.py

# Run specific test
pytest test_sample.py::test_answer
```

## Writing Tests

### Basic Test Functions

```python
def test_passing():
    assert (1, 2, 3) == (1, 2, 3)

def test_failing():
    assert (1, 2, 3) == (3, 2, 1)

def test_with_message():
    assert 1 == 2, "This will fail with a custom message"
```

### Testing Exceptions

```python
import pytest

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0

def test_exception_message():
    with pytest.raises(ValueError, match="invalid literal"):
        int("abc")

def test_exception_info():
    with pytest.raises(ValueError) as exc_info:
        int("abc")
    assert "invalid literal" in str(exc_info.value)
```

### Grouping Tests in Classes

```python
class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "upper")

    def setup_method(self):
        """Setup method called before each test method"""
        self.value = 42

    def teardown_method(self):
        """Teardown method called after each test method"""
        pass
```

## Fixtures

### Basic Fixtures

```python
import pytest

@pytest.fixture
def sample_data():
    return {"name": "John", "age": 30}

def test_sample_data(sample_data):
    assert sample_data["name"] == "John"
    assert sample_data["age"] == 30
```

### Fixture Scopes

```python
@pytest.fixture(scope="function")  # Default, runs for each test
def function_fixture():
    return "function"

@pytest.fixture(scope="class")  # Runs once per test class
def class_fixture():
    return "class"

@pytest.fixture(scope="module")  # Runs once per module
def module_fixture():
    return "module"

@pytest.fixture(scope="session")  # Runs once per test session
def session_fixture():
    return "session"
```

### Fixture with Setup and Teardown

```python
@pytest.fixture
def database_connection():
    # Setup
    connection = create_database_connection()
    yield connection  # This is where the test runs
    # Teardown
    connection.close()

def test_database_query(database_connection):
    result = database_connection.execute("SELECT 1")
    assert result == 1
```

### Parametrized Fixtures

```python
@pytest.fixture(params=[1, 2, 3])
def number(request):
    return request.param

def test_number_squared(number):
    assert number ** 2 >= 1
```

### Auto-use Fixtures

```python
@pytest.fixture(autouse=True)
def setup_test_environment():
    """This fixture runs automatically for every test"""
    print("Setting up test environment")
    yield
    print("Cleaning up test environment")
```

## Parametrization

### Parametrizing Test Functions

```python
import pytest

@pytest.mark.parametrize("input,expected", [
    (1, 2),
    (2, 3),
    (3, 4),
])
def test_increment(input, expected):
    assert input + 1 == expected

@pytest.mark.parametrize("x", [0, 1])
@pytest.mark.parametrize("y", [2, 3])
def test_combinations(x, y):
    assert x < y
```

### Parametrizing with IDs

```python
@pytest.mark.parametrize("input,expected", [
    (1, 2),
    (2, 3),
    (3, 4),
], ids=["one", "two", "three"])
def test_with_ids(input, expected):
    assert input + 1 == expected
```

### Complex Parametrization

```python
@pytest.mark.parametrize("test_input,expected", [
    pytest.param("3+5", 8, id="addition"),
    pytest.param("2+4", 6, id="addition2"),
    pytest.param("6*9", 54, id="multiplication"),
    pytest.param("6*7", 42, marks=pytest.mark.slow),
])
def test_eval(test_input, expected):
    assert eval(test_input) == expected
```

## Markers

### Built-in Markers

```python
import pytest

@pytest.mark.skip(reason="Not implemented yet")
def test_not_implemented():
    pass

@pytest.mark.skipif(sys.version_info < (3, 8), reason="Requires Python 3.8+")
def test_python38_feature():
    pass

@pytest.mark.xfail(reason="Known bug")
def test_known_bug():
    assert False

@pytest.mark.xfail(strict=True)
def test_strict_xfail():
    pass  # This must fail or the test will fail
```

### Custom Markers

```python
# pytest.ini or pyproject.toml
[tool.pytest.ini_options]
markers = [
    "slow: marks tests as slow",
    "integration: marks tests as integration tests",
    "unit: marks tests as unit tests",
]

# In test files
@pytest.mark.slow
def test_slow_operation():
    time.sleep(1)

@pytest.mark.integration
def test_database_integration():
    pass

# Run only specific markers
# pytest -m slow
# pytest -m "not slow"
# pytest -m "slow and integration"
```

## Configuration

### pytest.ini

```ini
[pytest]
minversion = 6.0
addopts = -ra -q --strict-markers --strict-config
testpaths = tests
python_files = tests.py test_*.py *_tests.py
python_classes = Test*
python_functions = test_*
markers =
    slow: marks tests as slow (deselect with '-m "not slow"')
    integration: marks tests as integration tests
    unit: marks tests as unit tests
```

### pyproject.toml

```toml
[tool.pytest.ini_options]
minversion = "6.0"
addopts = "-ra -q --strict-markers --strict-config"
testpaths = ["tests"]
python_files = ["tests.py", "test_*.py", "*_tests.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]
markers = [
    "slow: marks tests as slow (deselect with '-m \"not slow\"')",
    "integration: marks tests as integration tests",
    "unit: marks tests as unit tests",
]
```

### setup.cfg

```ini
[tool:pytest]
minversion = 6.0
addopts = -ra -q --strict-markers --strict-config
testpaths = tests
python_files = tests.py test_*.py *_tests.py
python_classes = Test*
python_functions = test_*
```

## Command Line Options

### Common Options

```bash
# Verbose output
pytest -v

# Quiet output
pytest -q

# Stop after first failure
pytest -x

# Stop after N failures
pytest --maxfail=2

# Run last failed tests
pytest --lf

# Run failed tests first
pytest --ff

# Show local variables in tracebacks
pytest -l

# Show available fixtures
pytest --fixtures

# Collect tests without running
pytest --collect-only

# Run tests in parallel (requires pytest-xdist)
pytest -n auto
```

### Selecting Tests

```bash
# Run specific test file
pytest test_mod.py

# Run specific test function
pytest test_mod.py::test_func

# Run specific test method in class
pytest test_mod.py::TestClass::test_method

# Run tests by keyword
pytest -k "test_method or test_other"

# Run tests by marker
pytest -m slow

# Run tests matching pattern
pytest test_*.py
```

## Assertions

### Basic Assertions

```python
def test_assertions():
    # Basic assertions
    assert 1 == 1
    assert 1 != 2
    assert 1 < 2
    assert 2 > 1
    assert 1 <= 1
    assert 1 >= 1

    # Boolean assertions
    assert True
    assert not False

    # Membership assertions
    assert 1 in [1, 2, 3]
    assert 4 not in [1, 2, 3]

    # String assertions
    assert "hello" in "hello world"
    assert "hello".startswith("he")
    assert "world".endswith("ld")
```

### Advanced Assertions

```python
import pytest
from pytest import approx

def test_advanced_assertions():
    # Approximate equality for floats
    assert 0.1 + 0.2 == approx(0.3)
    assert [0.1 + 0.2, 0.2 + 0.4] == approx([0.3, 0.6])

    # Dictionary comparison
    assert {"a": 0.1 + 0.2, "b": 0.2 + 0.4} == approx({"a": 0.3, "b": 0.6})

    # Custom tolerance
    assert 1.0001 == approx(1.0, abs=1e-3)
    assert 1.1 == approx(1.0, rel=0.1)
```

## Temporary Files and Directories

### Using tmp_path Fixture

```python
def test_create_file(tmp_path):
    # tmp_path is a pathlib.Path object
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "hello.txt"
    p.write_text("content")
    assert p.read_text() == "content"
    assert len(list(tmp_path.iterdir())) == 1

def test_create_temporary_file(tmp_path):
    file = tmp_path / "test.txt"
    file.write_text("Hello, World!")
    assert file.exists()
    assert file.read_text() == "Hello, World!"
```

### Using tmpdir Fixture (Legacy)

```python
def test_tmpdir(tmpdir):
    # tmpdir is a py.path.local object
    p = tmpdir.mkdir("sub").join("hello.txt")
    p.write("content")
    assert p.read() == "content"
    assert len(tmpdir.listdir()) == 1
```

## Monkeypatching

### Basic Monkeypatching

```python
def test_monkeypatch_setattr(monkeypatch):
    # Set attribute
    monkeypatch.setattr("os.getcwd", lambda: "/fake/path")
    import os
    assert os.getcwd() == "/fake/path"

def test_monkeypatch_setenv(monkeypatch):
    # Set environment variable
    monkeypatch.setenv("USER", "testuser")
    import os
    assert os.environ["USER"] == "testuser"

def test_monkeypatch_delenv(monkeypatch):
    # Delete environment variable
    monkeypatch.delenv("PATH", raising=False)
    import os
    assert "PATH" not in os.environ
```

### Monkeypatching Classes and Methods

```python
class MyClass:
    def method(self):
        return "original"

def test_monkeypatch_method(monkeypatch):
    def mock_method(self):
        return "mocked"

    monkeypatch.setattr(MyClass, "method", mock_method)
    obj = MyClass()
    assert obj.method() == "mocked"
```

## Plugins

### Popular Plugins

```bash
# Coverage reporting
pip install pytest-cov
pytest --cov=myproject tests/

# Parallel test execution
pip install pytest-xdist
pytest -n auto

# HTML reports
pip install pytest-html
pytest --html=report.html

# Django integration
pip install pytest-django

# Flask integration
pip install pytest-flask

# Async support
pip install pytest-asyncio

# Mock integration
pip install pytest-mock
```

### Using pytest-mock

```python
def test_with_mock(mocker):
    # Mock a function
    mock_func = mocker.patch('mymodule.myfunction')
    mock_func.return_value = 42

    result = mymodule.myfunction()
    assert result == 42
    mock_func.assert_called_once()
```

## Async Testing

### Testing Async Functions

```python
import pytest
import asyncio

@pytest.mark.asyncio
async def test_async_function():
    async def async_func():
        await asyncio.sleep(0.1)
        return "done"

    result = await async_func()
    assert result == "done"

# Configure async mode in pytest.ini
[tool.pytest.ini_options]
asyncio_mode = "auto"
```

## Debugging

### Using pdb

```python
def test_with_pdb():
    import pdb; pdb.set_trace()
    assert 1 == 1
```

### Using pytest's built-in debugging

```bash
# Drop into pdb on failures
pytest --pdb

# Drop into pdb on first failure
pytest -x --pdb

# Use pdbpp if available
pip install pdbpp
pytest --pdb
```

### Capturing Output

```python
def test_output(capsys):
    print("hello")
    print("world", file=sys.stderr)

    captured = capsys.readouterr()
    assert captured.out == "hello\n"
    assert captured.err == "world\n"

def test_logging(caplog):
    import logging
    logging.warning("This is a warning")

    assert "This is a warning" in caplog.text
    assert caplog.records[0].levelname == "WARNING"
```

## Best Practices

### Test Organization

```text
project/
├── src/
│   └── myproject/
│       ├── __init__.py
│       └── module.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── unit/
│   │   └── test_module.py
│   └── integration/
│       └── test_integration.py
└── pytest.ini
```

### conftest.py

```python
# tests/conftest.py
import pytest

@pytest.fixture(scope="session")
def database():
    """Session-wide database fixture"""
    db = create_test_database()
    yield db
    db.cleanup()

@pytest.fixture
def client(database):
    """Test client fixture"""
    return create_test_client(database)

# Shared test data
@pytest.fixture
def sample_user():
    return {
        "username": "testuser",
        "email": "test@example.com",
        "age": 25
    }
```

### Naming Conventions

- Test files: `test_*.py` or `*_test.py`
- Test functions: `test_*`
- Test classes: `Test*`
- Test methods: `test_*`

### Writing Good Tests

```python
def test_user_creation():
    # Arrange
    user_data = {"name": "John", "email": "john@example.com"}

    # Act
    user = create_user(user_data)

    # Assert
    assert user.name == "John"
    assert user.email == "john@example.com"
    assert user.id is not None

def test_user_creation_with_invalid_email():
    # Test edge cases and error conditions
    with pytest.raises(ValueError, match="Invalid email"):
        create_user({"name": "John", "email": "invalid-email"})
```

### Performance Testing

```python
import time
import pytest

def slow_function():
    time.sleep(0.1)
    return "result"

@pytest.mark.timeout(1)  # Requires pytest-timeout
def test_performance():
    start = time.time()
    result = slow_function()
    end = time.time()

    assert result == "result"
    assert end - start < 0.2  # Should complete in less than 200ms
```

This documentation covers the essential features of pytest for writing and running tests in Python applications with comprehensive testing capabilities.
