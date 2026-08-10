def weather_condition(temperature):
    if temperature >= 35:
        return "Very Hot"
    elif temperature >= 25:
        return "Warm"
    elif temperature >= 15:
        return "Cool"
    else:
        return "Cold"


def display_weather(city, temperature):
    condition = weather_condition(temperature)
    print("City:", city)
    print("Temperature:", temperature, "°C")
    print("Weather Condition:", condition)


# Main program
city = input("Enter city name: ")
temperature = float(input("Enter temperature in °C: "))

display_weather(city, temperature)