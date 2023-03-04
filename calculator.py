from alhambra_mixes import *
import pandas as pd
from IPython.display import display
import pandas as pd
import ipywidgets as widgets
from ipysheet.easy import cell
from ipywidgets import Layout

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
                component = component_id.split("_")
                mixing_components.append((Component(component[0], component[1]), temp[1]))

        # Returns a Mix from alhambra
        return Mix(
        [
            FixedConcentration(c[0], c[1]) for c in mixing_components 
        ],
        name=name,
        buffer_name=row.Buffer,
        fixed_total_volume=volume
        )      
    
    def search_for_recipes(self):
        recipes = self.recipes.iloc[:, 0]
        for i in range(0, len(recipes)): 
            
        
            print(recipes) 
            recipe_Menu = widgets.Dropdown(
            options=[recipe for recipe in recipes],
            value='Search for recipe:',
            disabled=False,
            )

        return recipe_Menu

    # Problems: 
    #   1) No way to gain data from the components in the inventory, consider storing Components 
    #      rather than just the component_id
    #   2) code-readibility
    #
    # Considerations:
    #   1) General inputs for components in inventory, no need for exact concentrations 
    #   2) Error Handling 
    #   3) Efficiently combine features together, reduce coupling 