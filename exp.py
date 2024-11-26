def celsius_faranheat(celius):
    faranheat = (celius * 9/5) + 32
    return faranheat

temp_celsius = 25

temp_fahrenheit = celsius_faranheat(temp_celsius)
print(f"{temp_celsius} is equal to {temp_fahrenheit} degrees Fahrenheit.")