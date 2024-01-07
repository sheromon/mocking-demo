from unittest.mock import MagicMock, patch

import requests

from outfit_picker.classes import OutfitPicker


def test_called_with():
    """"Verify that if a lat/lon gets passed in, the request uses it."""
    outfitter = OutfitPicker(lat_lon=(21.3, -157.86))
    ### Insert code to replace outfitter.openmeteo.weather_api with a mock
    # I recommend using the same code from test_exception_handling because
    # it's simpler to go down the error path than it is to set the return value.
    outfitter.recommend_outfit()
    ### Add code to verify that openmeteo.weather_api gets called once with the
    # following paramters.
    #   "https://api.open-meteo.com/v1/forecast"
    #   params={
    #       "latitude": 21.3,
    #       "longitude": -157.86,
    #       "daily": "temperature_2m_max",
    #       "temperature_unit": "fahrenheit",
    #       "timezone": "America/New_York",
    #       "forecast_days": 1
    #   }


def test_called_with_patch_dict():
    """"Verify that the lat/lon in the request_params dict gets used."""
    outfitter = OutfitPicker()
    ### Insert code to replace outfitter.openmeteo.weather_api with a mock
    # I recommend using the same code from test_exception_handling because
    # it's simpler to go down the error path than it is to set the return value.

    ### Add code that uses patch.dict to change the latitude and longitude
    # to 21.3 and -157.86 in the request_params dict
    outfitter.recommend_outfit()

    ### Add code to verify that openmeteo.weather_api gets called once with the
    # following paramters.
    #   "https://api.open-meteo.com/v1/forecast"
    #   params={
    #       "latitude": 21.3,
    #       "longitude": -157.86,
    #       "daily": "temperature_2m_max",
    #       "temperature_unit": "fahrenheit",
    #       "timezone": "America/New_York",
    #       "forecast_days": 1
    #   }
