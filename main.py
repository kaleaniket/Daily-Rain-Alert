import requests
from twilio.rest import Client


MY_LAT = "INSERT YOUR LATITUDE AS AN INTEGER"
MY_LON = "INSERT YOUR LATITUDE AS AN INTEGER"
api_key = "GET YOUR OPEN WEATHERMAP APIKEY BY SIGNING IN TO https://api.openweathermap.org"

account_sid = "ENTER YOUR TWILIO ACCOUNT ID" #YOU CAN GET YOUR ACCOUNT ID AND TOKEN BY SIGNING IN TO twilio.com
auth_token = "ENTER YOUR TWILIO AUTH TOKEN"

parameters = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "appid": api_key,
    "exclude": "current,minutely,daily",
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()
print(data)

hour = 0
will_rain = False
for weather in range(0, 11):
    weather_id = data["hourly"][hour]["weather"][0]["id"]
    hour += 1
    if weather_id < 700:
        will_rain = True

if will_rain:
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
                body="It's gonna rain today bring an umberlla☂️.",
                from_="NUMBER WHICH YOU GET FROM TWILIO",
                to="YOUR TWILIO REGISTERED MOBILE NUMBER"
                    )
        print(message.status)
