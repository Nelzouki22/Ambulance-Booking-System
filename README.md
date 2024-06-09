# Ambulance Booking System
Creating an Ambulance Booking System in Python involves several steps. We'll design a basic console-based system to start with. The core functionalities will include:

Booking an Ambulance
Viewing Bookings
Cancelling a Booking
Exiting the System

Creating an Ambulance Booking System in Python involves several steps. We'll design a basic console-based system to start with. The core functionalities will include:

Booking an Ambulance
Viewing Bookings
Cancelling a Booking
Exiting the System
To implement this, we'll use Python's built-in data structures and basic control flow. Here's a simple implementation outline:

Step 1: Define the Ambulance Booking System
We'll create a class AmbulanceBookingSystem to encapsulate the functionalities.

python
Copy code
class AmbulanceBookingSystem:
    def __init__(self):
        self.bookings = []

    def book_ambulance(self, patient_name, contact_number, location):
        booking_id = len(self.bookings) + 1
        booking = {
            'id': booking_id,
            'patient_name': patient_name,
            'contact_number': contact_number,
            'location': location,
            'status': 'Booked'
        }
        self.bookings.append(booking)
        print(f"Ambulance booked successfully! Your booking ID is {booking_id}.")

    def view_bookings(self):
        if not self.bookings:
            print("No bookings found.")
            return
        for booking in self.bookings:
            print(f"ID: {booking['id']}, Patient: {booking['patient_name']}, Contact: {booking['contact_number']}, Location: {booking['location']}, Status: {booking['status']}")

    def cancel_booking(self, booking_id):
        for booking in self.bookings:
            if booking['id'] == booking_id:
                booking['status'] = 'Cancelled'
                print(f"Booking ID {booking_id} has been cancelled.")
                return
        print(f"No booking found with ID {booking_id}.")

    def run(self):
        while True:
            print("\nAmbulance Booking System")
            print("1. Book an Ambulance")
            print("2. View Bookings")
            print("3. Cancel a Booking")
            print("4. Exit")

            choice = input("Enter your choice: ")
            if choice == '1':
                patient_name = input("Enter patient name: ")
                contact_number = input("Enter contact number: ")
                location = input("Enter location: ")
                self.book_ambulance(patient_name, contact_number, location)
            elif choice == '2':
                self.view_bookings()
            elif choice == '3':
                booking_id = int(input("Enter booking ID to cancel: "))
                self.cancel_booking(booking_id)
            elif choice == '4':
                print("Exiting the system.")
                break
            else:
                print("Invalid choice. Please try again.")

# Run the system
if __name__ == "__main__":
    system = AmbulanceBookingSystem()
    system.run()
Step 2: Explanation
Class Initialization: The __init__ method initializes an empty list for bookings.
Book an Ambulance: The book_ambulance method takes patient details, creates a booking, and appends it to the bookings list.
View Bookings: The view_bookings method prints all the current bookings.
Cancel a Booking: The cancel_booking method updates the status of the specified booking to "Cancelled".
Main Loop: The run method provides a simple text-based menu for the user to interact with the system.
Step 3: Running the System
To run the system, save the code to a Python file (e.g., ambulance_booking_system.py) and execute it. The user will interact with the system through the console.

This is a basic version. In a real-world application, you would likely use a database to store bookings, add validation, handle exceptions, and possibly create a user interface (UI).





