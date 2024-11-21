import requests #Question 2 Task 1

def fetch_planet_data():#Question 2 Task 2
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()["bodies"]
    #process each planet info
    for planet in planets:
        if planet['isPlanet']:
            name = planet.get('name')
            mass = planet['mass']['massValue']
            orbit_period = planet.get('sideralOrbit')
            print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")

fetch_planet_data()

def fetch_planet_data(): #Question 2 Task 3
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()["bodies"]
    return planets #list of planets

def find_heaviest_planet(planets):
    for planet in planets:
        if planet['isPlanet']:
            name = planet.get('name')
            mass = planet['mass']['massValue']
            return name, mass #heaviest planet

planets = fetch_planet_data()
name, mass = find_heaviest_planet(planets)
print(f"The heaviest planet is {name} with a mass of {mass} kg.")
