def celsius_faranheat(celius):
    farenheitt = (celius * 9/5) + 32
    return farenheitt

tem_celcius = 25
tem_celciu2 = 32
tem_celciu3 = 45
tem_farenhiet1 = celsius_faranheat(tem_celcius)
tem_farenhiet2 = celsius_faranheat(tem_celciu2)
tem_farenhiet3 = celsius_faranheat(tem_celciu3)

print(f"{tem_celcius}°C is equal to {tem_farenhiet1}")
print(f"{tem_celciu2}°C is equal to {tem_farenhiet2}")
print(f"{tem_celciu3}°C is equal to {tem_farenhiet3}")