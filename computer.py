
"""
Computer : Computer

Description:
    This class represents a computer with attributes like a description of the computer,the type of processor it uses, the capacity of its hard drive,memory,its operating system, the year it was made,and its price.
    It also provides methods on how we can access those attributes.
"""
class Computer:

    # What attributes will it need?
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int
    

    def __init__(self,description:str,processor_type:str,hard_drive_capacity:int,memory:int,operating_system:str,year_made:int,price:int):
        "Initializes a new Computer Object"
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price
    

    def update_price(self,price:float):
        """
        Updates the price of a computer.
        Args:
            price(float): The new price of the computer
        """
        self.price = price
    def update_os(self,operating_system:str):
       """
        Updates the operating system of a computer.
        Args:
            operating_system(float): The new operating system of the computer
        """        
       self.operating_system = operating_system

        




