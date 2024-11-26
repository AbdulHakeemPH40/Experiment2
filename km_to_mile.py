def kilometer_to_miles(km):
    kilometer = km * 0.621371
    return kilometer

def miles_to_kilometer(mile):
    miles = mile * 1.60934
    return miles

convertion_type = input("Type 'km to miles' or 'miles to km':" ).strip().lower()
if convertion_type == 'km to miles':
    kilometer = float(input("Enter the number of kilometers:"))
    miles = kilometer_to_miles(kilometer)
    print(f"{kilometer} Kilometer is equal to {miles} Miles")
elif convertion_type == 'miles to km':
    miles = float(input("Enter the number of miles:"))
    kilometer = miles_to_kilometer(miles)
    print(f"{miles} Miles is equal to {kilometer} kilometers")
else:
    print("Invalid convertion type")
    
