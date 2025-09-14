import pytest
from datetime import timedelta
from goduration import parse


@pytest.mark.parametrize(
    "input_str,expected",
    [
        ("1m", timedelta(minutes=1)),
        ("2h", timedelta(hours=2)),
        ("2h30m", timedelta(hours=2, minutes=30)),
        ("-8h", timedelta(hours=-8)),
        ("1s", timedelta(seconds=1)),
        ("30s", timedelta(seconds=30)),
        ("1m30s", timedelta(minutes=1, seconds=30)),
        ("300ms", timedelta(milliseconds=300)),
        ("1s500ms", timedelta(seconds=1, milliseconds=500)),
        ("500us", timedelta(microseconds=500)),
        ("500µs", timedelta(microseconds=500)),
        ("1000ns", timedelta(microseconds=1)),
        ("1.5h", timedelta(hours=1, minutes=30)),
        ("2.5m", timedelta(minutes=2, seconds=30)),
        ("1.25s", timedelta(seconds=1, milliseconds=250)),
        ("1h15m30.918s", timedelta(hours=1, minutes=15, seconds=30, milliseconds=918)),
    ],
)
def test_parse_duration_go_spec(input_str, expected):
    result = parse(input_str)
    assert result == expected, f"parse('{input_str}') = {result}, expected {expected}"


@pytest.mark.parametrize(
    "invalid_input",
    [
        "",
        "1",
        "1x",
        "1m4z",
        "h1",
        "1.2.3m",
    ],
)
def test_parse_duration_invalid(invalid_input):
    with pytest.raises((ValueError, TypeError)):
        parse(invalid_input)
