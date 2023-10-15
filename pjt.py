#Vehicle valuation programme
vehicle_data = {}


vehicle_data['make'] = input("Enter the make of your vehicle: ")
vehicle_data['model'] = input("Enter the model of your vehicle: ")
vehicle_data['year'] = input("Enter the year of your vehicle: ")
vehicle_data['license_plate'] = input("Enter the license plate number of your vehicle: ")

print("\nVehicle Data:")
for key, value in vehicle_data.items():
    print(f"{key.capitalize()}: {value}")

valuation_data = {
    "Honda Civic": {2022: 25000, 2021: 22000, 2020: 20000},
    "Toyota Camry": {2022: 28000, 2021: 25000, 2020: 22000},
    "Ford F-150": {2022: 35000, 2021: 32000, 2020: 29000},
}

make = input("Enter the make of your vehicle: ")
model = input("Enter the model of your vehicle: ")
year = int(input("Enter the year of your vehicle: "))

if model in valuation_data and year in valuation_data[model]:
    valuation = valuation_data[model][year]
    print(f"The estimated value of your {year} {make} {model} is ${valuation}")
else:
    print("Valuation data not available for this vehicle.")

#Honda Valuation is incorrect please check again
