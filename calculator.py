from alhambra_mixes import *
import pandas as pd

class Calculator:
    # Parses the csv file containing all recipes 
    # Takes in the current inventory 
        ## Figure out a different way to keep track of inventory, 
        ## This way is too hard-coded :(
    def __init__(self, inventory):
        self.recipes = pd.read_csv("recipes.csv", delimiter="|"); 
        self.inventory = inventory

    # Method to find the index of the row containing the recipe wanted
    def find_recipe_index(self, name: str) -> int:
        for i in range(0, len(self.recipes)):
            if (self.recipes.loc[i].Name == name):
                return i
                
    # Method to create mixes using the Inventory and Component classes (Hawa created)
    def create_mix(self, name: str, volume: str): 
        # Parses the row into name, buffer, and components  
        index = self.find_recipe_index(name)   
        row = self.recipes.loc[index]
        temp = row.Components.split(";")
        mixing_components = []

        for components in temp: 
            temp = components.split(",")
            component_id = temp[0]
            print(component_id)
            # Checks if component is contained in inventory 
            if self.inventory.find_component(component_id): 
                c = self.inventory.get_component(component_id)
                mixing_components.append((Component(c.component_name, c.concentration), temp[1]))

        # Returns a Mix from alhambra
        return Mix(
        [
            FixedConcentration(c[0], c[1]) for c in mixing_components 
        ],
        name=name,
        buffer_name=row.Buffer,
        fixed_total_volume=volume
        )      

    # Problems: 
    #   1) No way to gain data from the components in the inventory, consider storing Components 
    #      rather than just the component_id
    #   2) code-readibility
    #
    # Considerations:
    #   1) General inputs for components in inventory, no need for exact concentrations 
    #   2) Error Handling 
    #   3) Efficiently combine features together, reduce coupling 