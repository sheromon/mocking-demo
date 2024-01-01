from unittest.mock import Mock, patch

from easy_outfit.classes import OutfitPicker


# def test_recommend_outfit_function_called():
#     mock = Mock(return_value={"ok": False})
#     with patch('requests.get', mock):
#         result = recommend_outfit()
#         assert requests.get.assert_called_once_with(
#             "https://api-v3.mbta.com/predictions",
#             {"filter[stop]": 70067},
#         )

# def test_recommend_outfit_function():
#     mock = Mock(return_value=35)
#     with patch('mbta.time_check.get_max_temp', mock):
#         result = recommend_outfit()
#         assert result == 300

def test_recommend_outfit():
    """Verify that the expected outfit is selected based on the max temperature."""
    outfitter = OutfitPicker()

    # for temp >= 70, we expect shorts and a T-shirt
    outfitter.get_max_temp = Mock(return_value=85)
    result = outfitter.recommend_outfit()
    expected_result = {
        "top": "T-shirt",
        "bottom": "shorts",
        "other": None,
    }
    assert result == expected_result

    # for 70 > temp >= 45, we expect pants instead of shorts and adding a coat
    outfitter.get_max_temp = Mock(return_value=60)
    result = outfitter.recommend_outfit()
    expected_result = {
        "top": "T-shirt",
        "bottom": "pants",
        "other": None,
    }
    assert result == expected_result

    # for temp < 45, we expect pants instead of shorts and adding a coat
    outfitter.get_max_temp = Mock(return_value=35)
    result = outfitter.recommend_outfit()
    expected_result = {
        "top": "T-shirt",
        "bottom": "pants",
        "other": "coat",
    }
    assert result == expected_result


def test_recommend_outfit_context_manager():
    mock = Mock(return_value=35)
    with patch('easy_outfit.classes.OutfitPicker.get_max_temp', mock):
        outfitter = OutfitPicker()
        result = outfitter.recommend_outfit()
    expected_result = {
        "top": "T-shirt",
        "bottom": "pants",
        "other": "coat",
    }
    assert result == expected_result


@patch('easy_outfit.classes.OutfitPicker.get_max_temp', Mock(return_value=35))
def test_recommend_outfit_decorator():
    outfitter = OutfitPicker()
    result = outfitter.recommend_outfit()
    expected_result = {
        "top": "T-shirt",
        "bottom": "pants",
        "other": "coat",
    }
    assert result == expected_result


@patch.object(OutfitPicker, 'get_max_temp', Mock(return_value=35))
def test_recommend_outfit_decorator_object():
    outfitter = OutfitPicker()
    result = outfitter.recommend_outfit()
    expected_result = {
        "top": "T-shirt",
        "bottom": "pants",
        "other": "coat",
    }
    assert result == expected_result
