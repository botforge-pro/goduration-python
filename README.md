[![Tests](https://github.com/botforge-pro/goduration-python/actions/workflows/test.yml/badge.svg)](https://github.com/botforge-pro/goduration-python/actions/workflows/test.yml)
[![Documentation](https://github.com/botforge-pro/goduration-python/actions/workflows/documentation.yml/badge.svg)](https://botforge-pro.github.io/goduration-python/goduration.html)

# goduration-python

Go-style duration parsing for Python.

## Installation

```bash
pip install git+https://github.com/botforge-pro/goduration-python
```

## Usage

```python
>>> import goduration
>>> goduration.parse('1m')
datetime.timedelta(seconds=60)
>>> goduration.parse('2h')
datetime.timedelta(seconds=7200)
>>> goduration.parse('2h30m')
datetime.timedelta(seconds=9000)
>>> goduration.parse('-8h')
datetime.timedelta(days=-1, seconds=57600)
```

## Documentation

The [API reference](https://botforge-pro.github.io/goduration-python/goduration.html) is generated from the public Python API and deployed by GitHub Actions.
