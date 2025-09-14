import pytest
from datetime import timedelta
from goduration import parse


@pytest.mark.parametrize(
    "input_str,expected",
    [
        ("0", timedelta(0)),
        ("0s", timedelta(0)),
        ("0m", timedelta(0)),
        ("0h", timedelta(0)),
        ("+1h", timedelta(hours=1)),
        ("+30m", timedelta(minutes=30)),
        ("1h0m", timedelta(hours=1)),
        ("1h0m0s", timedelta(hours=1)),
        ("0h30m", timedelta(minutes=30)),
        ("0h0m30s", timedelta(seconds=30)),
    ],
)
def test_parse_edge_cases(input_str, expected):
    result = parse(input_str)
    assert result == expected
