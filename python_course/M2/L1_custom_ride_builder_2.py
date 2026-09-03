print("Pick your vehicle. 1 - Bike, 2 - Car")

vehicle = int(input("Enter your choice: "))

if vehicle == 1:
    print("You picked Bike\n")
    print("Pick your bike type. 1 - Sports Bike, 2 - Mountain Bike")
    bike_type = int(input("Enter your choice: "))
    
    if bike_type == 1:
        print("You picked Sports Bike")

    elif bike_type == 2:
        print("You picked Mountain Bike")

    else:
        print("Invalid bike type choice. Please enter 1 or 2.")

elif vehicle == 2:
    print("You picked Car\n")
    print("Pick your car type. 1 - Sedan, 2 - SUV")
    car_type = int(input("Enter your choice: "))
    
    if car_type == 1:
        print("You picked Sedan")

    elif car_type == 2:
        print("You picked SUV")

    else:
        print("Invalid car type choice. Please enter 1 or 2.")

else:
    print("Invalid vehicle choice. Please enter 1 or 2.")


print("\nThank you")