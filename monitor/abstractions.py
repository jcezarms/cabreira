"""Module for generic object manipulation utilitary functions.
"""


def are_keys_in(obj: dict, keys: list):
    """Safe check for the presence of a list of keys in an object.

    Args:
        obj: The dictionary into which validations will occur.
        keys: List of keys for validation. Must be ordered sequentially,
            so to validate `obj['a']['b']`, `keys=['a', 'b']`.

    Returns:
        Boolean indicating whether or not all keys are present in `obj`.
    """
    o = obj

    for k in keys:
        is_int = isinstance(k, int)
        key_present = (isinstance(o, list) and len(o) > k) if is_int else o.get(k)

        if not key_present:
            return False

        o = o[k]

    return True
