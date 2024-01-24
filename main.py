import json
import turtle 
import urllib.request 
import time 
import webbrowser 
import geocoder 

url = 'http://api.open-notify.org/astros.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())
people = result['people']
print("People on board the ISS:")
for each in people:
  astronaut_name = each.get('name', 'Unknown')
  print(astronaut_name)
  
#setup world map and iss in turtle module 

screen = turtle.Screen()
screen.setup(1280, 720)
screen.setworldcoordinates(-180, -90, 180, 90)

screen.bgpic('map.gif')
screen.register_shape('satellite.gif')
iss = turtle.Turtle()
iss.shape('satellite.gif')
iss.setheading(40)
iss.penup()

# load current location of iss in real time
while True: 
  url = 'http://api.open-notify.org/iss-now.json'
  responce = urllib.request.urlopen(url)
  result = json.loads(responce.read())

  location = result['iss_position']
  lat = location['latitude']
  lon = location['longitude']

  lat = float(lat)
  lon = float(lon)
  print("\nLatitude: " + str(lat))
  print("\nLongitude: "+ str(lon))

  # update iss location 
  iss.goto(lon, lat)

  #refresh every 7 sec 
  
  time.sleep(2)

  