import io
from unittest.mock import Mock, patch

import requests

import requests

from outfit_picker.classes import OutfitPicker


@patch("sys.stdout", new_callable=io.StringIO)
def test_exception_handling(mock_stdout):
    """"Verify that if there is a connection error while calling the weather api,
    the expected message gets printed.
    """
    outfitter = OutfitPicker()
    outfitter.openmeteo.weather_api = Mock(side_effect=requests.exceptions.ConnectionError())
    outfitter.recommend_outfit()
    expected_output = "Weather data is not available. Cannot recommend an outfit."
    assert mock_stdout.getvalue().strip() == expected_output
