import googlemaps
import os
import populartimes
from os.path import join, dirname
from dotenv import load_dotenv, find_dotenv


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path, override=True)  # 設定 override 才會更新變數哦！

GOOGLE_PLACES_API_KEY = os.environ.get("GOOGLE_PLACES_API_KEY")

# Client
gmaps = googlemaps.Client(key=GOOGLE_PLACES_API_KEY)
geocode_result = gmaps.geocode("臺北市立動物園")
print(geocode_result)
p =populartimes.get_id(GOOGLE_PLACES_API_KEY, 'ChIJj4EySmCqQjQRZte0Cf0G_qo')
print(p)
# # Radar search
# location = (25.017156, 121.506359)
# radius = 25000
# place_type = 'restaurant'
# places_radar_result = gmaps.places_radar(location, radius, type=place_type)

# print(places_radar_result)
# import requests

# url = f"https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=Museum%20of%20Contemporary%20Art%20Australia&inputtype=textquery&fields=formatted_address%2Cname%2Crating%2Copening_hours%2Cgeometry&key={GOOGLE_PLACES_API_KEY}"

# payload={}
# headers = {}

# response = requests.request("GET", url, headers=headers, data=payload)

# print(response.text)