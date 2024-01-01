import logging

import openmeteo_requests
import requests


logging.basicConfig(level=logging.INFO)


class OutfitPicker:

    def __init__(self, lat_lon=None) -> None:
        if lat_lon is None:
            lat_lon = (42.36, -71.06)  # Boston, MA
        # Make sure all required weather variables are listed here
        # The order of variables in hourly or daily is important to assign them correctly below
        self.request_params = {
            "latitude": lat_lon[0],
            "longitude": lat_lon[1],
            "daily": "temperature_2m_max",
            "temperature_unit": "fahrenheit",
            "timezone": "America/New_York",
            "forecast_days": 1
        }

        # Setup the Open-Meteo API client
        self.openmeteo = openmeteo_requests.Client()

    def get_max_temp(self) -> float:
        """Request the max forecasted temperature in degrees Fahrenheit and return it."""
        url = "https://api.open-meteo.com/v1/forecast"
        try:
            responses = self.openmeteo.weather_api(url, params=self.request_params)
        except requests.exceptions.ConnectionError as exc:
            logging.exception(exc)
            return None

        # Process first location. Add a for-loop for multiple locations or weather models
        response = responses[0]
        logging.info(f"Coordinates {response.Latitude()}°E {response.Longitude()}°N")
        logging.info(f"Timezone difference to GMT+0 {response.UtcOffsetSeconds() / 60**2} hrs")

        # Process daily data. The order of variables needs to be the same as requested.
        daily = response.Daily()
        daily_temp_max = daily.Variables(0).ValuesAsNumpy()
        logging.info("Daily max temp: %.2f degrees F", daily_temp_max)
        return daily_temp_max

    def recommend_outfit(self):
        """Return a recommended outfit based on the max temperature."""
        max_temp = self.get_max_temp()
        if max_temp is None:
            print("Weather data is not available. Cannot recommend an outfit.")
            return

        outfit = {
            "top": "T-shirt",
            "bottom": "shorts",
            "other": None,
        }
        if max_temp < 70:
            outfit["bottom"] = "pants"
        if max_temp < 45:
            outfit["other"] = "coat"
        return outfit


def main():
    outfitter = OutfitPicker()
    outfitter.recommend_outfit()


if __name__ == "__main__":
    main()
