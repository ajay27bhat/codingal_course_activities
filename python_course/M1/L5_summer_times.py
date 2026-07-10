# Program to check if the temperature is suitable
# for wearing light clothes

# Get temperature from the user
temperature = float(input("Enter the temperature (°C): "))

# Check the temperature
if temperature >= 25:
    print("The weather is warm.")
    print("You can wear light and soft clothes.")
else:
    print("The weather is cold.")
    print("Wear a jacket or a pullover.")