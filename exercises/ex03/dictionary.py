"""Practice with Dictionary Functions!"""

__author__ = "730569281"


def invert(d: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values of a dictionary. If duplicates exist, raises KeyError"""
    inverted = {}
    for key, value in d.items():
        if value in inverted:
            raise KeyError(f"Duplicate value found: {value})")
        inverted[value] = key
    return inverted


def count(lst: list[str]) -> dict[str, int]:
    """Counts how many times each string appears and returns a dictionary"""
    counts = {}
    for item in lst:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts


def favorite_color(colors: dict[str, str]) -> str:
    """Return most frequent color given a dictionary of names and favorite colors"""
    if not colors:
        return ""
    color_count = count(list(colors.values()))
    return max(color_count, key=color_count.get)


def bin_len(lst: list[str]) -> dict[int, set[str]]:
    """Groups strings by their length into a dictionary of sets"""
    length_bins = {}
    for word in lst:
        length = len(word)
        if length not in length_bins:
            length_bins[length] = {word}
        else:
            length_bins[length].add(word)
    return length_bins
