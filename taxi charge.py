# Taxi Service Program
#Blessing Gijima R247779H 2.1
# Constant (base fare)
BASE_FARE = 5.00


def calculate_fare(distance, rate_per_km):
    """Calculate total taxi fare"""
    return BASE_FARE + (distance * rate_per_km)


def main():
    print("Welcome to vhamvhamvhum taxi Service ")

    customer_name = input("Enter your name: ")
    distance = float(input("Enter distance to travel (in km): "))
    rate_per_km = float(input("Enter rate per km (e.g. 2.5): "))


    total_fare = calculate_fare(distance, rate_per_km)


    print("..... TAXI RECEIPT ......")
    print("Customer Name:", customer_name)
    print("Distance Travelled:", distance, "km")
    print("Rate per km: $", rate_per_km)
    print("Base Fare: $", BASE_FARE)
    print("Total Fare: $", total_fare)
    print("---------------------")
    print("Thank you for riding with vhamvhamvhum ")


# Run the program
if __name__ == "__main__":
    main()

input()
