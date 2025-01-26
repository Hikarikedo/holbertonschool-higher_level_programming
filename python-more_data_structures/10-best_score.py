#!/usr/bin/python3
def best_score(a_dictionary):
    """
    Returns the key with the highest integer value in the dictionary.
    Args:
        a_dictionary (dict): The dictionary to evaluate.
    Returns:
        str or None: The key with the highest value,
        or None if dictionary is empty or None.
    """
    if not a_dictionary:
        return None
    return max(a_dictionary, key=a_dictionary.get)
