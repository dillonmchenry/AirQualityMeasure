from date import Date

d1 = Date("2019-01-01")
d2 = Date("2019-05-01")

def test_in_span():
    first = d1
    second = d2
    third = Date("2019-10-01")

    assert second.in_span(first, third)
    assert not first.in_span(second, third)
    assert not third.in_span(second, first)

def test_equal():
    assert d1.equal(d1)
    assert not d2.equal(d1)