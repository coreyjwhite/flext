from datetime import datetime
import requests


def get_hourly_forecast(office, grid_x, grid_y):
    forecast_resp = requests.get(
        f"https://api.weather.gov/gridpoints/{office}/{grid_x},{grid_y}/forecast/hourly",
        headers={"User-Agent": "flext-nws-interface"},
    ).json()
    data = []
    for period in forecast_resp["properties"]["periods"]:
        datum = {
            "office": office,
            "lat": forecast_resp["geometry"]["coordinates"][0][0][0],
            "long": forecast_resp["geometry"]["coordinates"][0][0][1],
            "timestamp": datetime.fromisoformat(
                forecast_resp["properties"]["updated"]
            ),
            "start": datetime.fromisoformat(period["startTime"]),
            "end": datetime.fromisoformat(period["endTime"]),
            "temperature": period["temperature"],
            "forecast": period["shortForecast"],
        }
        data.append(datum)
    return data
