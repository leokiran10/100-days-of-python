capitals = {
    "Nepal": "Kathmandu",
    "India": "Delhi"
}

# Nesting a List in a Dictorary
travel_log = {
    "Nepal": ["Kathmandu", "Porkara", "Mustang"],
    "India": ["Goa", "Delhi","Mumbai"]
}
# print(travel_log)

# Nesting Dictionary in Dictionary
travel_log = {
    "Nepal": {"cities_visited": ["Kathmandu","Pokhara","Mustang"], "Total_visits":6},
}
# print(travel_log)

# Nesting Dictionary in list
travel_log = [
    {
     "country": "Nepal",
     "cities_visited":["Kathmandu","Pokhara"],
     "total_visits": 4
     },
     {
      "country": "India",
      "cities_visited":["Goa","Delhi"],
      "total_visits": 4
      }
]
print(travel_log)