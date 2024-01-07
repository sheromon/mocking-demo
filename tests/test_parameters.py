from unittest.mock import MagicMock, patch

import requests

from outfit_picker.classes import OutfitPicker


def test_called_with():
    """"Verify that if a lat/lon gets passed in, the request uses it."""
    outfitter = OutfitPicker(lat_lon=(21.3, -157.86))
    outfitter.openmeteo.weather_api = MagicMock(side_effect=requests.exceptions.ConnectionError)
    outfitter.recommend_outfit()
    outfitter.openmeteo.weather_api.assert_called_once_with(
        "https://api.open-meteo.com/v1/forecast",
        params={
            "latitude": 21.3,
            "longitude": -157.86,
                "daily": "temperature_2m_max",
                "temperature_unit": "fahrenheit",
                "timezone": "America/New_York",
                "forecast_days": 1
        })


def test_called_with_patch_dict():
    """"Verify that the lat/lon in the parameters dict gets used."""
    outfitter = OutfitPicker()
    outfitter.openmeteo.weather_api = MagicMock(side_effect=requests.exceptions.ConnectionError)
    with patch.dict(outfitter.request_params, {"latitude": 21.3, "longitude": -157.86}):
        outfitter.recommend_outfit()
        outfitter.openmeteo.weather_api.assert_called_once_with(
            "https://api.open-meteo.com/v1/forecast",
            params={
                "latitude": 21.3,
                "longitude": -157.86,
                    "daily": "temperature_2m_max",
                    "temperature_unit": "fahrenheit",
                    "timezone": "America/New_York",
                    "forecast_days": 1
            })
