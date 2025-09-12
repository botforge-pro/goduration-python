[![Tests](https://github.com/botforge-pro/goduration-python/actions/workflows/test.yml/badge.svg)](https://github.com/botforge-pro/goduration-python/actions/workflows/test.yml)

# goduration-python

Go-style duration parsing for Python.

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

