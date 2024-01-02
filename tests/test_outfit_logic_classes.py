from unittest.mock import MagicMock, patch

from outfit_picker.classes import OutfitPicker


def test_recommend_outfit():
    """Verify that the expected outfit is selected based on the max temperature."""
    outfitter = OutfitPicker()

    # for temp >= 70, we expect shorts and a T-shirt
    outfitter.get_max_temp = MagicMock(return_value=85)
    result = outfitter.recommend_outfit()
    expected_result = {
        "top": "T-shirt",
        "bottom": "shorts",
        "other": None,
    }
    assert result == expected_result

    # for 70 > temp >= 45, we expect pants instead of shorts and adding a coat
    outfitter.get_max_temp = MagicMock(return_value=60)
    result = outfitter.recommend_outfit()
    expected_result = {
        "top": "T-shirt",
        "bottom": "pants",
        "other": None,
    }
    assert result == expected_result

    # for temp < 45, we expect pants instead of shorts and adding a coat
    outfitter.get_max_temp = MagicMock(return_value=35)
    result = outfitter.recommend_outfit()
    expected_result = {
        "top": "T-shirt",
        "bottom": "pants",
        "other": "coat",
    }
    assert result == expected_result


def test_recommend_outfit_context_manager():
    mock = MagicMock(return_value=35)
    with patch('outfit_picker.classes.OutfitPicker.get_max_temp', mock):
        outfitter = OutfitPicker()
        result = outfitter.recommend_outfit()
    expected_result = {
        "top": "T-shirt",
        "bottom": "pants",
        "other": "coat",
    }
    assert result == expected_result


@patch('outfit_picker.classes.OutfitPicker.get_max_temp', MagicMock(return_value=35))
def test_recommend_outfit_decorator():
    outfitter = OutfitPicker()
    result = outfitter.recommend_outfit()
    expected_result = {
        "top": "T-shirt",
        "bottom": "pants",
        "other": "coat",
    }
    assert result == expected_result


@patch.object(OutfitPicker, 'get_max_temp', MagicMock(return_value=35))
def test_recommend_outfit_decorator_object():
    outfitter = OutfitPicker()
    result = outfitter.recommend_outfit()
    expected_result = {
        "top": "T-shirt",
        "bottom": "pants",
        "other": "coat",
    }
    assert result == expected_result
