class Vehicle:
    def __init__(self, vehicle_type, capacity):
        self.vehicle_type = vehicle_type
        self.capacity = capacity

class Bus(Vehicle):
    def __init__(self, vehicle_type, capacity, fare_per_passenger):
        super().__init__(vehicle_type, capacity)
        self.fare_per_passenger = fare_per_passenger

    def calculate_total_fare(self, number_of_passengers):
        if number_of_passengers > self.capacity:
            raise ValueError("Exceeds bus capacity.")
        return number_of_passengers * self.fare_per_passenger

if __name__ == "__main__":
    city_bus = Bus("City Bus", 50, 2.5)
    passengers = 30
    total_fare = city_bus.calculate_total_fare(passengers)
    print(f"Total fare for {passengers} passengers: ${total_fare:.2f}")