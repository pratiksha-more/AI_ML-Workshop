# Description: This file contains the code for the lab activity of Day 1
#string

city_name="City A"
print(f"City Name is: {city_name}")

#Integer
temprature=25
print(f"Temprature is: {temprature} °C")


#Float
carbon_footprint=500.75
print(f"Carbon Footprint is: {carbon_footprint} Kg CO2")

#boolean
is_sustainable=carbon_footprint<400
print(f"Is The city Sustainable ? {is_sustainable}")

#Create and Assign List variable 
weekly_temprature=[25,27,28,26,24,30,29]
print(f"Weekly Temprature: {weekly_temprature}")

#create a dictionory variable

city_data={
    "name":"City A",
    "temperature":25,
    "carbon_footprint":500.75,
    "is_sustainable":False,
}

print(f"City Data: {city_data}")


#Assign Multiple Variable in Single Line
city_name,temprature,carbon_footprint="City B",30,350.50
print(f"City Name: {city_name},Temprature: {temprature} °C, Carbon Footprint: {carbon_footprint} Kg CO2")

#Use 1:  Filter Data to find cities with high temprature
climate_data=[
    {"city":"City A","temprature":25,"carbon_footprint":500},
    {"city":"City B","temprature":30,"carbon_footprint":350},
    {"city":"City C","temprature":22,"carbon_footprint":600},
    {"city":"City D","temprature":15,"carbon_footprint":200},
    {"city":"City E","temprature":28,"carbon_footprint":450},
]

high_temp_threshhold=26
high_temp_cities=[city for city in climate_data if city["temprature"]>high_temp_threshhold]


print("Cities with High temparature (>26°C):")
for city in high_temp_cities:
    print(f"{city['city']} : {city['temprature']} °C")

#Use 2:  Calculate Average Carbon Footprint of all cities
print("****Use 2: ******")
total_carbon=0
for city in climate_data:
    total_carbon+=city["carbon_footprint"]

average_carbon_footprint=total_carbon/len(climate_data)
print(f"Average Carbon Footprint: {average_carbon_footprint:.2f} Kg CO2")

#use  3: Filter and Manipulate Data to find Sustainable cities

sustainability_threshold=400
sustainable_cities=list(filter(lambda city:city["carbon_footprint"]<sustainability_threshold,climate_data))
print("\nSustainable Cities(carbon_footprint<400 kg CO2)")

for city in sustainable_cities:
    print(f"{city['city']} : {city['carbon_footprint']} Kg CO2")


#use 4: Analyze Dara to Find city with the Highest Footprint City

highest_footprint_city=max(climate_data,key=lambda city:city["carbon_footprint"])

print(f"\nCity with Highest Carbon Footprint: {highest_footprint_city['city']} : {highest_footprint_city['carbon_footprint']} Kg CO2")
print(f"{highest_footprint_city['city']}-{highest_footprint_city['carbon_footprint']} Kg CO2")