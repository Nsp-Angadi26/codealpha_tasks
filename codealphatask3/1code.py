import requests
import folium

def get_geolocation(ip_address=""):
    url = f"http://ip-api.com/json/{ip_address}"
    response = requests.get(url)
    data = response.json()
    
    if data["status"] == "success":
        return data["lat"], data["lon"], data["city"], data["country"]
    else:
        return None

def generate_map(lat, lon, city, country):
    map = folium.Map(location=[lat, lon], zoom_start=10)
    folium.Marker([lat, lon], popup=f"{city}, {country}").add_to(map)
    map.save("geolocation_map.html")

ip_address = ""  # Leave empty for your own IP or provide an IP manually
geo_data = get_geolocation(ip_address)

if geo_data:
    lat, lon, city, country = geo_data
    generate_map(lat, lon, city, country)
    print("Map generated: geolocation_map.html")
else:
    print("Failed to retrieve geolocation data.")