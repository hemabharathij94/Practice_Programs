MAX_SEAT = 20

class Booking:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.source = ""
        self.destination = ""
        self.seat_number = 0
        self.is_booked = False

train = [Booking() for _ in range(MAX_SEAT)]

def initialize():
    for i in range(MAX_SEAT):
        train[i].is_booked = False
        
def display_available_seats():
    print("Available Seats:")
    for i in range(MAX_SEAT):
        if not train[i].is_booked:
            print(f"Seat {i + 1} is available.")

def book_seat():
    seat_number = int(input("Enter the seat number to book: "))
    if 1 <= seat_number <= MAX_SEAT:
       if not train[seat_number - 1].is_booked:
           train[seat_number - 1].name = input("Enter the Name: ")
           train[seat_number - 1].seat_number = seat_number
           train[seat_number - 1].source = input("Enter the Source: ")
           train[seat_number - 1].destination = input("Enter the Destination: ")
           train[seat_number - 1].age = int(input("Enter the Age: "))
           train[seat_number - 1].is_booked = True
           print(f"Seat {seat_number} has been booked.")
       else:
           print("Seat is already booked.")
    else:
        print("Invalid seat number.")

def cancel_seat():
    seat_number = int(input("Enter the seat number to cancel: "))
    if 1 <= seat_number <= MAX_SEAT:
       if train[seat_number - 1].is_booked:
          train[seat_number - 1].is_booked = False
          train[seat_number - 1].name = ""
          train[seat_number - 1].age = 0
          train[seat_number - 1].source = ""
          train[seat_number - 1].destination = ""
          print(f"Seat {seat_number} has been canceled.")
       else:
          print("Seat is not booked.")
    else:
        print("Invalid seat number.")

def print_ticket():
    seat_number = int(input("Enter the seat number to print ticket for: "))
    if 1 <= seat_number <= MAX_SEAT:
       if train[seat_number - 1].is_booked:
          print("Name of Passenger:", train[seat_number - 1].name)
          print("Age of Passenger:", train[seat_number - 1].age)
          print("Source:", train[seat_number - 1].source)
          print("Destination:", train[seat_number - 1].destination)
       else:
          print("Seat is not booked.")
    else:
        print("Invalid seat number.")

def main():
    initialize()
    choice = 0
    while choice != 5:
        print("\nTrain Booking System")
        print("1. Display available seats")
        print("2. Book a seat")
        print("3. Cancel a seat")
        print("4. Print ticket")
        print("5. Exit")

        choice = int(input("Choose the number: "))

        if choice == 1:
            display_available_seats()
        elif choice == 2:
            book_seat()
        elif choice == 3:
            cancel_seat()
        elif choice == 4:
            print_ticket()
        elif choice == 5:
            print("Exiting the system.")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()