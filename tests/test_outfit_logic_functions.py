from unittest.mock import MagicMock, patch

import outfit_picker.functions
from outfit_picker.functions import recommend_outfit


def test_recommend_outfit():
    """Verify that the expected outfit is selected based on the max temperature."""

    # for temp >= 70, we expect shorts and a T-shirt
    outfit_picker.functions.get_max_temp = MagicMock(return_value=85)
    result = recommend_outfit()
    expected_result = {
        "top": "T-shirt",
        "bottom": "shorts",
        "other": None,
    }
    assert result == expected_result

    # for 70 > temp >= 45, we expect pants instead of shorts and adding a coat
    outfit_picker.functions.get_max_temp = MagicMock(return_value=60)
    result = recommend_outfit()
    expected_result = {
        "top": "T-shirt",
        "bottom": "pants",
        "other": None,
    }
    assert result == expected_result

    # for temp < 45, we expect pants instead of shorts and adding a coat
    outfit_picker.functions.get_max_temp = MagicMock(return_value=35)
    result = recommend_outfit()
    expected_result = {
        "top": "T-shirt",
        "bottom": "pants",
        "other": "coat",
    }
    assert result == expected_result


### Insert patch decorator to give the expected result
def test_recommend_outfit_decorator():
    result = recommend_outfit()
    expected_result = {
        "top": "T-shirt",
        "bottom": "pants",
        "other": "coat",
    }
    assert result == expected_result


### Insert patch.object decorator to give the expected result
def test_recommend_outfit_decorator_object():
    result = recommend_outfit()
    expected_result = {
        "top": "T-shirt",
        "bottom": "pants",
        "other": "coat",
    }
    assert result == expected_result


def test_recommend_outfit_context_manager():
    ### Insert code to use a context manager to run the recommend_outfit method
    # and get the expected result
    expected_result = {
        "top": "T-shirt",
        "bottom": "pants",
        "other": "coat",
    }
    assert result == expected_result
