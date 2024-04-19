country = input()
visits = int(input())
cities = eval(input())
travel_log = [
    {
        "country": "france",
        "visits": 12,
        "cities": ["paris", "lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "hamburg", "stuttgart"]
    }
]
def add_new_country(name, times, list_cities):
    new_country = {}
    new_country["country"] = name
    new_country["visits"] = times
    new_country["cities"] = list_cities
    travel_log.append(new_country)
add_new_country(country, visits, cities)
print(f"I have been to {travel_log[2]['country']} {travel_log[2]['visits']} times")
print(f"My favourite city  is {travel_log[2]['cities'][0]}")
