import io
from unittest.mock import Mock, patch

import requests

import requests

from outfit_picker.classes import OutfitPicker


@patch("sys.stdout", new_callable=io.StringIO)
def assert_stdout(outfitter, expected_output, mock_stdout):
    """Verify that the expected message gets printed when recommend_outfit is run."""
    outfitter.recommend_outfit()
    assert mock_stdout.getvalue().strip() == expected_output


def test_exception_handling():
    """"Verify that if there is a connection error while calling the weather api,
    the expected message gets printed.
    """
    outfitter = OutfitPicker()
    outfitter.openmeteo.weather_api = Mock(side_effect=requests.exceptions.ConnectionError())
    expected_output = "Weather data is not available. Cannot recommend an outfit."
    assert_stdout(outfitter, expected_output)
