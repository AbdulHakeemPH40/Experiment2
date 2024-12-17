def celius_to_faranheit(celsius):
    farahiet = (celsius * 9/5) +32
    return farahiet

temp_celsius = 25
temp_faranhiet = celius_to_faranheit(temp_celsius)
print(f"{temp_celsius} celsius is equal to {temp_faranhiet} faranhiet!")
