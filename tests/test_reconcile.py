import pytest
from reference import reconcile

@pytest.mark.parametrize("events,expected",[
    ([],{}),
    ([{"tenant":"a","key":"x","version":1,"value":5}],{"a/x":5}),
    ([{"tenant":"a","key":"x","version":2,"value":9},{"tenant":"a","key":"x","version":1,"value":1}],{"a/x":9}),
    ([{"tenant":"a","key":"x","version":1,"value":1},{"tenant":"b","key":"x","version":1,"value":2}],{"a/x":1,"b/x":2}),
    ([{"tenant":"a","key":"x","version":1,"value":1}]*2,{"a/x":1}),
])
def test_valid(events,expected):
    assert reconcile(events)==expected

@pytest.mark.parametrize("events",[
    [{"tenant":"a","key":"x","version":1,"value":1},{"tenant":"a","key":"x","version":1,"value":2}],
    [{"tenant":"a","key":"x","version":-1,"value":2}],
    [{"tenant":"a","key":"x","version":True,"value":2}],
    [{"tenant":"","key":"x","version":1,"value":2}],
    [{"tenant":"a","key":"x","version":1}],
])
def test_invalid(events):
    with pytest.raises(ValueError):
        reconcile(events)
