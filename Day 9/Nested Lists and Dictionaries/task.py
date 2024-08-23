# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Stuttgart", "Berlin"],
# }

# for key in travel_log:
#     for cities in travel_log[key]:
#         print(cities)


# nested_list = ["A", "B", ["C", "D"]]
#
# print(nested_list[2][1])

travel_log = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
   },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
   },
}

for key in travel_log:
    for details in travel_log[key]:
        if details == "cities_visited":
            for cities in travel_log[key][details]:
                print(cities)
