"""
Activity: Weather Outfit Picker

Instructions:
1. Ask the user to enter today's temperature.
2. If the temperature is below 20°C, suggest wearing a jacket.
3. Otherwise, suggest wearing a t-shirt.
4. Ask if it is raining.
5. If it is raining, remind the user to carry an umbrella.
8. Ask if there are puddles on the ground.
9. If there are puddles, suggest wearing boots.
10. Otherwise, suggest wearing sneakers.
11. Display a summary of the outfit choices.
"""

# Ask for today's temperature
temperature = int(input("Enter today's temperature (°C): "))

# Check if it is cold and decide the outfit 
if temperature < 20:
    outfit = "Jacket"
else:
    outfit = "T-Shirt"

print("Suggested Outfit:", outfit)


# Check if it is raining and decide on the umbrella
raining = input("Is it raining? (yes/no): ")

if raining == "yes":
    print("Don't forget to carry an umbrella!")

else:
    print("No umbrella needed.")


# Check for puddles and decide the shoes
puddles = input("Are there puddles? (yes/no): ")

if puddles == "yes":
    shoes = "Boots"
else:
    shoes = "Sneakers"

print("Suggested Shoes:", shoes)

# Display the final summary
print("\n===== WEATHER OUTFIT SUMMARY =====")
print("Temperature :", temperature, "°C")
print("Outfit      :", outfit)
print("Raining     :", raining)
print("Shoes       :", shoes)
print("=================================")