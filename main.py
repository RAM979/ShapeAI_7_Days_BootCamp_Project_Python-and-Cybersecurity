import requests
from datetime import datetime

#Got API from openweathermap.org with mail rofico1208@bbsaili.com
api_key = 'b1925ca5ec0557616e4f903b0e1e03b5'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

#Write the output to Report Weather file
with open("Report Weather.txt","w") as f:
    f.write("-------------------------------------------------------------\n")
    f.write(f"Weather Stats for - {location.upper()}  || { date_time}\n")
    f.write("-------------------------------------------------------------\n")
    #Writing the data
    f.write("\nCurrent temperature is: {:.2f} deg C".format(temp_city))
    f.write(f"\nCurrent weather desc  :{weather_desc}")
    f.write(f"\nCurrent Humidity      :{hmdt}%")
    f.write(f"\nCurrent wind speed    :{wind_spd}kmph\n")
    f.write("\n-------------------------------------------------------------\n")

#Close the file
f.close()