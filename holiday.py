"""
This code calculates the total cost of a holiday trip, 
including flight, hotel, and car rental expenses.

**Inputs:**

- `city_flight`: The desired city of destination (Rome, London, or Paris).
- `num_nights`: The number of nights to stay at the hotel.
- `rental_days`: The number of days to rent a car.

**Functions:**

- `hotel_cost(num_nights)`: Calculates the hotel cost based on the number of nights and a fixed price per night.
- `plane_cost(city_flight)`: Determines the flight cost based on the destination city.
- `car_rental(rental_days)`: Calculates the car rental cost based on the number of rental days and a fixed price per day.
- `holiday_cost(num_nights, city_flight, rental_days)`: 
    Calculates the total holiday cost by summing the costs from 
    `hotel_cost`, `plane_cost`, and `car_rental`.

**Output:**

Prints a summary of the holiday details, including:
- City of destination
- Flight cost
- Hotel nights and cost
- Car rental days and cost
- Total holiday cost
"""

city_flight = input("We have flights to Rome, London and Paris. Could you please confirm your desirable city of destination: ")
num_nights = int(input("Number of nights you are stay at the hotel: "))
rental_days = int(input("Number of days you will hire a car: "))


def hotel_cost(num_nights):
    """
    Calculates the total hotel cost.

    Args:
        num_nights: The number of nights to stay at the hotel.

    Returns:
        The total hotel cost.
    """
    price_per_night = 100 
    return num_nights * price_per_night


def plane_cost(city_flight):
    """
    Calculates the flight cost based on the destination city.

    Args:
        city_flight: The desired city of destination.

    Returns:
        The flight cost.
    """
    if city_flight == "Rome":
        return 800
    elif city_flight == "London":
        return 900
    elif city_flight == "Paris":
        return 1200
    else: 
        return 0


def car_rental(rental_days):
    """
    Calculates the total car rental cost.

    Args:
        rental_days: The number of days to rent a car.

    Returns:
        The total car rental cost.
    """
    price_per_day = 50 
    return rental_days * price_per_day


def holiday_cost(num_nights, city_flight, rental_days):
    """
    Calculates the total holiday cost.

    Args:
        num_nights: The number of nights to stay at the hotel.
        city_flight: The desired city of destination.
        rental_days: The number of days to rent a car.

    Returns:
        The total holiday cost.
    """
    hotel = hotel_cost(num_nights)
    plane = plane_cost(city_flight)
    car = car_rental(rental_days)
    total_cost = hotel + plane + car
    return total_cost

total_holiday = holiday_cost(num_nights, city_flight, rental_days)

print(f"\nHoliday details:")
print(f"  City: {city_flight}")
print(f"  Flight cost: ${plane_cost(city_flight)}") 
print(f"  Hotel nights: {num_nights}")
print(f"  Hotel cost: ${hotel_cost(num_nights)}")
print(f"  Car rental days: {rental_days}")
print(f"  Car rental cost: ${car_rental(rental_days)}")
print(f"  \nHoliday total cost: ${total_holiday}")