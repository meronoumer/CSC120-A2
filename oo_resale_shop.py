from computer import *

"""
ResaleShop : ResaleShop

Description:
This class represents a Resale Shop with the inventory attribute as well as methods to access those attributes like buy,sell and print_inventory
"""
class ResaleShop:


    def __init__(self):
        """
        Initializes a new Resale Shop Object. 
        """
        self.inventory = []
    def buy(self,computer:Computer):
        """
        Adds a computer to the inventory and returns its index.
        Args:
            computer: The computer object to be added to the inventory.
        return:The index of the added computer in the inventory.
        """
        self.inventory.append(computer)
        return self.inventory.index(computer)


    def sell(self,computer:Computer):
        """
        Sells a computer from the inventory.
        Args:
            computer: The computer object to be sold.
        """
        if computer in self.inventory:
            self.inventory.remove(computer)
            print("Item", computer, "sold!")
        else:
            print("Computer", computer,"not. Please select another item to sell.")

        """
        Prints the current inventory of computers.
        """
    def print_inventory(self,computer:Computer):

        
        if self.inventory:
            for computer in self.inventory:
                print(f'Computer:{self.inventory.index(computer)} Description: {computer.description} Processor Type :{computer.processor_type} Hard Drive Capacity:{computer.hard_drive_capacity} Memory :{computer.memory}Operating System:{computer.operating_system} Year Made:{computer.year_made} Price:{computer.price}')


                
                    #   Computer:self.inventory.index(computer),
                    #   description: {computer.description},
                    #   processor_type :{computer.processor_type},
                    #   hard_drive_capacity:{computer.hard_drive_capacity},
                    #   memory:{computer.memory},
                    #   operating_system:{computer.operating_system},
                    #   year_made:{computer.year_made},
                    #   price:{computer.price}
        else:
            print("No inventory to display.")
    def refurbish(self, index, new_operating_system=None):
     """
    Refurbishes a computer in the inventory based on its manufacturing year 
    and optionally installs a new operating system.

    Args:
        index (int): The index (or item ID) of the computer in the inventory.
        new_operating_system (str): The new operating system to install..
    """
     if len(self.inventory)>index and self.inventory[index] is not None :
            computer = self.inventory[index]

            year_made = int(computer.year_made)
            if year_made < 2000:
                computer.update_price(0)  
            elif year_made < 2012:
                computer.update_price(250)
            elif year_made < 2018:
                computer.update_price(550) 
            else:
                computer.update_price(1000) 

            if new_operating_system:
                computer.update_os(new_operating_system)
     else:
        print(f"Item {index} not found. Please select another item to refurbish.")
     
     
        




 

        

def main():

    my_laptop:Computer = Computer("Microsoft Surface Pro","Intel Core i5","128GB","8GB","Windows 10 ","2020","500")
    store = ResaleShop()
    store.buy(my_laptop)
    store.sell(my_laptop)
    store.print_inventory(my_laptop)
    my_laptop.update_price(499)
    store.print_inventory(my_laptop)
    store.refurbish(0, "Windows 11 ")
    store.print_inventory(my_laptop)


main()
