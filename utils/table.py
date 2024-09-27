List_names = ["Majed","Minah" ,"Amr", "JAck", "Leon"]
import random

class seat:
    ''' This is the seat class to check if is free or not, where we can creat instance object'''
    def __init__(self):
        self.free = True
        self.occupant = ""
        

    def set_occupant(self,name):
        self.free = False
        self.occupant = name
    
    def remove_occupant(self):
        self.free = True
        self.occupant = ""
         
    def __str__(self):
        if self.free:
            return f"free seat"
        else:
            return f"{self.occupant}"
        

##################################              Class Table                 ##################################
class Table:
    """ This is the class to check the tables"""
    def __init__(self, capacity = 4):   
        self.capacity = capacity
        self.seats = []              # this has to be the seats objects created from the seat class
        for j in range (self.capacity):
            self.seats.append(seat())    # here we are creating new seat and add to the list (object) 
           
    def showing_seats (self):             # looping over the 
        for i in self.seats:
            print (i)
          
    def has_free_spot(self):
        for seat in self.seats:
            if seat.free:
                return True
            else:
                return False
    
    def assign_seat(self,name):
        for seat in self.seats:
            if seat.free:
                seat.set_occupant(name)
                return True 
            

    def left_capacity(self):
        left_free = 0
        for i in self.seats:
            if i.free:
                left_free +=1
        return  left_free