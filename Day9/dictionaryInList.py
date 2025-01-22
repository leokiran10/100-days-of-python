travel_log = [
    {
     "country": "Nepal",
     "visits": 4,
     "cities":["Kathmandu","Pokhara"],
     },
     {
      "country": "India",
      "visits": 4,
      "cities":["Goa","Delhi", "Mumbai"],
      }
]

def add_new_country(country_visited, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)

add_new_country("Russia", 2, ["Moscow", "Moscow1", "Moscow2"])
print(travel_log)