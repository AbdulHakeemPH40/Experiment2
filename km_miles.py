def km_to_miles(km):
    return km * 0.621371

def miles_to_km(miles):
    return miles * 1.60394

input_types = input("Type 'km to miles' or 'miles to km':").strip().lower()
if input_types == 'km to miles':
    user_input = float(input("Ennter the distance of kilometer:"))
    kilometer = km_to_miles(user_input)
    print(f"{user_input} kilometer is equal to {kilometer} Miles")
elif input_types == 'miles to km':
    user_input2 = float(input("Enter the distance of Miles:"))
    miles = miles_to_km(user_input2)
    print(f"{user_input2} Miles is equal to {miles} Kilometer")
else:
    print("Invalid Input")

