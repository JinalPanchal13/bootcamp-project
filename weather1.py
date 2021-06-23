import requests
#import os
from datetime import datetime





api_key = '8f87f870e61d17e2ac864b0897aedbaf'
location = input("Enter the city name: ")

complete_api_link = "http://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
cloud = api_data['clouds']['all']


print ("-------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print ("-------------------------------------------------------------")



#read
f = open('weather1.txt', 'w')
f.write(format(temp_city))
f.write('\n')
f.write(weather_desc)
f.write('\n')
f.write(str(hmdt))
f.write('\n')
f.write(str(wind_spd))
f.write('\n')
f.write(str(cloud))
f.close()

file1 = open('weather1.txt', 'r')
Lines = file1.readlines()

count = 0
# Strips the newline character
for line in Lines:
    count += 1
    print("1{}: {}".format(count, line.strip()))
            

#print ("Current temperature is: {:.2f} deg C".format(temp_city))
#print ("Current weather desc  :",weather_desc)
#print ("Current Humidity      :",hmdt, '%')
#print ("Current wind speed    :",wind_spd ,'kmph')
#print ("Current cloud         :",cloud,'kph')
