"""Testing Dictionary Functions"""

__author__ = "730569281"

import pytest
from exercises.ex03.dictionary import invert


def test_invert_basic():
    """Test normal inversion of keys and values."""
    input_dict = {"a": "z", "b": "y", "c": "x"}
    expected = {"z": "a", "y": "b", "x": "c"}
    assert invert(input_dict) == expected


def test_invert_single_element():
    """Test the case with a single key-value pair."""
    input_dict = {"apple": "cat"}
    expected = {"cat": "apple"}
    assert invert(input_dict) == expected


def test_invert_duplicate_value():
    """Test the case where duplicate values cause a KeyError."""
    input_dict = {"kris": "jordan", "michael": "jordan"}
    with pytest.raises(KeyError):
        invert(input_dict)


from exercises.ex03.dictionary import count


def test_count_multiple_occurrences():
    """Test counting multiple occurrences of strings."""
    input_list = ["apple", "banana", "apple", "orange", "banana", "banana"]
    expected = {"apple": 2, "banana": 3, "orange": 1}
    assert count(input_list) == expected


def test_count_no_repetitions():
    """Test counting when no strings are repeated."""
    input_list = ["apple", "banana", "orange"]
    expected = {"apple": 1, "banana": 1, "orange": 1}
    assert count(input_list) == expected


def test_count_empty_list():
    """Test counting with an empty list."""
    input_list = []
    expected = {}
    assert count(input_list) == expected


from exercises.ex03.dictionary import favorite_color


def test_favorite_color_empty():
    """Test case for an empty dictionary."""
    assert favorite_color({}) == ""


def test_favorite_color_single():
    """Test case for a dictionary with a single entry."""
    assert favorite_color({"Alice": "blue"}) == "blue"


def test_favorite_color_multiple():
    """Test case for a dictionary with multiple entries and a single most frequent color."""
    colors = {"Alice": "blue", "Bob": "blue", "Charlie": "green"}
    assert favorite_color(colors) == "blue"


def test_favorite_color_tie():
    """Test case for a dictionary with a tie in frequency of colors."""
    colors = {"Alice": "blue", "Bob": "green", "Charlie": "blue", "David": "green"}
    assert favorite_color(colors) == "blue"


from exercises.ex03.dictionary import bin_len


def test_bin_len_basic():
    """Test basic case where strings are grouped by length."""
    input_list = ["the", "quick", "fox"]
    expected = {3: {"the", "fox"}, 5: {"quick"}}
    assert bin_len(input_list) == expected


def test_bin_len_duplicates():
    """Test case where some strings are duplicates."""
    input_list = ["the", "the", "fox"]
    expected = {3: {"the", "fox"}}
    assert bin_len(input_list) == expected


def test_bin_len_empty():
    """Test case with an empty list."""
    input_list = []
    expected = {}
    assert bin_len(input_list) == expected
