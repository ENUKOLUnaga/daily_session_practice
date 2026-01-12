
"""
Enukolu Nagendra
 Set 7 (Hotel Room Booking)
A hotel manages different room types.
Scenario:
Class Room with attributes room_number, price_per_night


Subclasses: StandardRoom, DeluxeRoom


Requirements:
Deluxe rooms include additional service charges


Override price calculation

"""
#Room class
class Room:
    def __init__(self, room_number, price_per_night):
        self.room_number = room_number
        self.price_per_night = price_per_night
        self.__is_booked = False  
    def is_booked(self):
        return self.__is_booked
    def book_room(self):
        if self.__is_booked:
            print("Room ",self.room_number," is already booked!")
            return False
        else:
            self.__is_booked = True
            print("Room ",self.room_number," booked successfully.")
            return True
    def calculate_price(self, nights):
        return self.price_per_night * nights
    
#Standard Room Class
class StandardRoom(Room):
    def __init__(self, room_number, price_per_night):
        super().__init__(room_number, price_per_night)

#Deluxe Room Class
class DeluxeRoom(Room):
    def __init__(self, room_number, price_per_night, charges):
        super().__init__(room_number, price_per_night)
        self.charges = charges
    def calculate_price(self, nights):
        base_price = super().calculate_price(nights)
        return base_price + self.charges * nights
room1 = StandardRoom(101, 1000)
room2 = DeluxeRoom(201, 2000, 500)
room1.book_room()  
room2.book_room()  
print("Total for 3 nights in Standard Room: ",room1.calculate_price(3))
print("Total for 2 nights in Deluxe Room: ",room2.calculate_price(2))
