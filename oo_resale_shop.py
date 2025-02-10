from computer import *

class ResaleShop:
    """
    ResaleShop : ResaleShop

    Description:
        This class represents a Resale Shop with the inventory attribute as well as methods to access those attributes like buy,sell and print_inventory
    """

    def __init__(self):
        """
        Initializes a new Resale Shop Object. 
        """
        self.inventory : list = []
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
    
    def print_inventory(self,computer:Computer):
        """
        Prints the current inventory of computers.
        """
        if self.inventory:
            for computer in self.inventory:
                print(f'Computer:self.inventory.index(computer) : {computer}')
        else:
            print("No inventory to display.")
    def refurbish(self, index, new_operating_system):
        """
    
        Refurbishes a computer in the inventory based on when it was manufactured.

        Updates the computer's price based on its age and also installs a new operating system.

        Args:
            index (int): The index (or them item ID) of the computer in the inventory.
            new_operating_system (str, optional): The new operating system to install. 
                Default is set to  None, which would mean no operating system update.

        """
        if index in self.inventory:
            computer = self.inventory[index]  # Retrieve the Computer object

            year_made = computer.year_made  # Access year_made directly

            if year_made < 2000:
                computer.price = 0  
            elif year_made < 2012:
                computer.price = 250  
            elif year_made < 2018:
                computer.price = 550  
            else:
                computer.price = 1000  

            if new_operating_system:
                computer.operating_system = new_operating_system  

        else:
            print(f"Item {index} not found. Please select another item to refurbish.")




 

        

def main():

    my_laptop:Computer = Computer("Microsoft Surface Pro","Intel Core i5","128GB","8GB","Windows 10 ","2020","500")
    store = ResaleShop()
    store.buy(my_laptop)
    store.sell(my_laptop)
    store.print_inventory()
    my_laptop.update_price(499)


main()
