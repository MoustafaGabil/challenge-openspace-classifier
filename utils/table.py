
class seat:
    ''' This is the seat class to check if is free or not, if it is free so, it assigns a name to the free seat, It can also 
        remove a person from a set and assign it as a free place '''
    
    def __init__(self):                # this constructor intiate the instance object (seat) with a free spot.
        self.free = True
        self.occupant = ""

    def set_occupant(self,name):      # this (function/method) assign a name to a certain seat.
        self.free = False
        self.occupant = name
    
    def remove_occupant(self):        # this (function/method) remove the an occupant (person) from the seat  
        self.free = True
        self.occupant = ""
        
    def __str__(self):                # This function return the name of the occupant if it is assigned or "free seat" if it is free.
        if self.free:
            return f"free seat"
        else:
            return f"{self.occupant}" 


##################################              Class Table                 ##################################
class Table:
""" This class is mainly to assing 4 different persons to one table which is the maximum capacity for each table. 
        It returns also the capacity of each table"""
        
    def __init__(self, capacity=4):
        self.capacity = capacity
        self.seats = []  # this has to be the seats objects created from the seat class
        for j in range(self.capacity):
            self.seats.append(
                seat()
            )  # here we are creating new seat and add to the list (object)

    def showing_seats(self):  # looping over the
        for i in self.seats:
            print(i)

    def has_free_spot(self):
        for seat in self.seats:
            if seat.free:
                return True
            else:
                return False

    def assign_seat(self, name):
        for seat in self.seats:
            if seat.free:
                seat.set_occupant(name)
                return True

    def left_capacity(self):
        left_free = 0
        for i in self.seats:
            if i.free:
                left_free += 1
        return left_free
