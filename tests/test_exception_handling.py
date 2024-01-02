import io
from unittest.mock import patch

from easy_outfit.classes import OutfitPicker


@patch("sys.stdout", new_callable=io.StringIO)
def test_exception_handling(mock_stdout):
    """"Verify that if there is a connection error while calling the weather api,
    the expected message gets printed.
    """
    outfitter = OutfitPicker()
    ### Insert code to trigger an exception that will result in the expected
    # message being printed out
    outfitter.recommend_outfit()
    expected_output = "Weather data is not available. Cannot recommend an outfit."
    assert mock_stdout.getvalue().strip() == expected_output
