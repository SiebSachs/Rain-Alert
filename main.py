import requests                 # for API requests
from twilio.rest import Client  # to send SMS
import smtplib
import os

# Environmental variables has to be saved in PyCharm under: klick left to the play button on the dropdown and
# select Edit Configuration -> Select the python script configuration or create a new one -> search on the right
# side the field for Environment variables -> insert the variables -> save them with klick on ok"

MY_EMAIL = os.environ.get('MY_GM_EMAIL')
MY_PASSWORD = os.environ.get('MY_GM_PASSWORD')

#account_sid = "SKd38fd54e23017faa8668ed5795e339d2"
#auth_token = os.environ.get('AUTH_TOKEN_TWILIO')
#print(auth_token)

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get('OWM_API_KEY')
parameters = {
    "lat": 48.710814,
    "lon": 9.459378,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params= parameters)
response.raise_for_status()
weather_data = response.json()
print(weather_data)

# Get the weather condition id from the data and evaluate it
# https://openweathermap.org/api/weather-conditions#Weather-Condition-Codes-2   # Weather condition codes -> everything < 700 means rain

for item in weather_data["list"]:
    if item["weather"][0]["id"] < 700:
        print("Bring an umprella")
        #client = Client(account_sid, auth_token)
        # Send an SMS
        #message = client.messages.create(
        #    body="It's going to rain today. Remember to bring an umbrella.",
        #    to="+4917643847xxx",
        #    from_="+4915888620339",
        #)
        #print(message.status)

        # Send a WhatsApp
        #message = client.messages.create(
        #    from_="+4915888620339",
        #    body="It's going to rain today. Remember to bring an umbrella",
        #    to="+4917643847xxx"
        #)
        #print(message.status)

        # Send an email
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject: Rain is coming.\n\nIt's going to rain today. Remember to bring an umbrella."
        )
        break

#weather_id_list = [item["weather"][0]["id"] for item in weather_data["list"]]  # Extracts the weather id from the data
#print(weather_id_list)
