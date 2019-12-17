from ..date import Date

def test_in_span():
    first = Date("2019-01-01")
    second = Date("2019-05-01")
    third = Date("2019-10-01")

    assert second.in_span(first, third)
    assert not first.in_span(second, third)
    assert not third.in_span(second, first)