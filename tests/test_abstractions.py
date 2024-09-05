from monitor.abstractions import are_keys_in


def test_are_keys_in_doesnt_fail_empty_objects():
    expected = False
    actual = are_keys_in(obj={}, keys=["a", "b", "c"])
    assert expected == actual


def test_are_keys_in_finds_multiple_nesting_levels():
    expected = True
    actual = are_keys_in(obj={"a": {"b": {"c": 1}}}, keys=["a", "b", "c"])
    assert expected == actual
