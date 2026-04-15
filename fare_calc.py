# CityCab Fare Calculator

def calculate_fare(km, vehicle, hour):
    rates = {
        "Economy": 10,
        "Premium": 18,
        "SUV": 25
    }

    # check vehicle
    if vehicle not in rates:
        return -1, False

    base = km * rates[vehicle]

    surge = False
    if 17 <= hour <= 20:
        surge = True

    final = base * (1.5 if surge else 1)

    booking_fee = 20
    final = final + booking_fee

    return final, surge


print("CityCab Fare Estimator\n")

try:
    km = float(input("Distance (km): "))

    vehicle = input("Vehicle type: ").strip().title()

    hour = int(input("Hour (0-23): "))

    if not (0 <= hour <= 23):
        print("Invalid hour entered")
    elif km <= 0:
        print("Distance should be greater than 0")
    else:
        fare, surge_flag = calculate_fare(km, vehicle, hour)

        if fare == -1:
            print("Service Not Available")
        else:
            print("\n----- Receipt -----")
            print("Distance:", km, "km")
            print("Vehicle:", vehicle)
            print("Time:", hour)

            if surge_flag:
                print("Note: Peak hour pricing applied")
            else:
                print("Note: Normal pricing")

            print("Booking Fee: ₹20")

            print("Total Fare: ₹", int(fare) if fare.is_integer() else round(fare, 1))

except ValueError:
    print("Please enter valid numbers only")