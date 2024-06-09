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

