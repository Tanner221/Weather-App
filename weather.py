import requests, json, password

def askName():
  name = input("City Name: ")
  return name

def processName(cityName):
  processedName = ''
  for x in cityName:
    if x == ' ':
      processedName += '+'
    else:
      processedName += x
  return processedName

def fillURL(url, id, cityName):
  url += cityName
  url += id
  return url

def convertTemp(tempKelvin):
  tempFahrenheit = (tempKelvin - 273.15) * 9/5 + 32
  temp = float("{:.1f}".format(tempFahrenheit))
  return temp

def printResponse(response):
  response = response.json()
  code = response["cod"]
  if code == 200:
    main = response["main"]
    #convert from Kelvin to Fahrenheit
    kelvin = main["temp"]
    feelLikeKelvin = main["feels_like"]
    temp = convertTemp(kelvin)
    feelTemp = convertTemp(feelLikeKelvin)
    humidity = main["humidity"]
    visibility = response["visibility"]

    print(f"\nTemperature: {temp} Degrees Fahrenheit")
    print(f"Feels LIke: {feelTemp} Degrees Fahrenheit")
    print(f"Humidity: {humidity}%")
    print(f"Visibility: {visibility} feet")
  else:
    print("ERROR: City Name does not exist")

from password import *

print("\nWelcome to the Weather App! Please Enter the City name to find its current outdoor temperature\n")
cityName = askName()
cityName = processName(cityName)
setUrl = fillURL(url, id, cityName)
response = requests.get(setUrl)
printResponse(response)
