def km_to_miles(km):
    return km * 0.621371

def miles_to_km(miles):
    return miles * 1.60934

convertion_type = input("Type 'km to miles' or 'miles to km':").lower() .strip()
if convertion_type == 'km to miles':
    user_input =  float(input("Enter the number of kilowmeters:"))
    kilometer = km_to_miles(user_input)
    print(f"{user_input} Kilometer is equal to {kilometer} Miles")
elif convertion_type == 'miles to km':
    user_input2 = float(input("Enter the number of miles:"))
    miles = miles_to_km(user_input2)
    print(f"{user_input2} Miles equal to {miles} Kilometer")
else:
    print("Invalid input")
