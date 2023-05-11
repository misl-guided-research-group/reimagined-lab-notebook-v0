from datetime import datetime
from IPython.display import display
import ipywidgets as widgets
from ipywidgets import Layout
import pandas as pd

class Member:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        
class Component:
    def __init__(self, creator, component_name, concentration, is_buffer):
        self.creator = creator 
        self.component_name = component_name
        self.concentration = concentration
        self.component_id = f"{component_name}_{concentration}"
        self.is_buffer = is_buffer # not sure how to use this yet.
        self.curr_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")

#ideally the entire inventory should be a real time interaction, rather than typing. 
# need to abstract away the methods/

class Inventory:
    def __init__(self):
        self.components = []
        
        # create an empty dataframe with the desired columns
        self.df = pd.DataFrame(columns=['Creator', 'Component Name', 'Concentration', 'Component ID', 'Is Buffer', 'Timestamp'])

        # display the widgets
        self.display_options()

    def display_options(self):
        add_button = widgets.Button(description="Add Component",  layout=Layout(display='flex'))
        remove_button = widgets.Button(description="Remove Component",  layout=Layout(display='flex'))
        display_button = widgets.Button(description="Display All Components",  layout=Layout(display='flex'))
        search_button = widgets.Button(description="Search for Component",  layout=Layout(display='flex'))

        add_button.on_click(lambda event: self.add_component)
        remove_button.on_click(lambda event: self.remove_component)
        search_button.on_click(lambda event: self.find_component)
        display_button.on_click(lambda event: self.display_inventory)

        display(add_button)
        display(remove_button)
        display(display_button)
        display(search_button)

    # Updates all the displays 
    def display_inventory(self): 
        self.df = pd.DataFrame([vars(c) for c in self.components])
        print(self.df)
        
    # Adds a new component to the inventory 
    def add_component(self):
            # take input from the user for the new row
            creator = input("Enter the name of the creator: ")
            component_name = input("Enter the name of the component: ")
            concentration = input("Enter the concentration of the component: ")
            is_buffer = input("Enter of the component is a buffer: ")
            
            # Make the new component 
            new_component = Component(creator, component_name, concentration, is_buffer)

            # Checks if component is already contained 
            if new_component.component_id in self.components:
                self.contains_component(new_component)
                return

            # Add new component 
            self.components.append(new_component)

            # Display a message to indicate the component was radded
            print(f"Component with ID {new_component.component_id} was successfully added to the inventory.")

    # Removes an existing component in the inventory 
    def remove_component(self):
        # Prompt the user to enter the component ID
        component_id = input("Enter the component ID of the component you wish to remove: ")
        
        # Check if the component exists in the inventory
        component = None
        for c in self.components:
            if c.component_id == component_id:
                component = c
                break
                
        if component is None:
            print(f"Component with ID {component_id} is not in the inventory!")
            return
        
        # Remove the component from the list
        self.components.remove(component)
        
        # Update the dataframe
        self.df = self.df[self.df['Component ID'] != component_id]
    
        # Display a message to indicate the component was removed
        print(f"Component with ID {component_id} was successfully removed from the inventory.")


    # pass in component object as a whole. this function differse 
    # to find_component in that it will do the highlighting logic. 
    def contains_component(self, component):
        # if the unique component already exists, then display table, highlight cell green
        # and indicate it is already in there.
        if component.component_id in self.components:
             # can use this mechanism since order of elements is persistent in python
                # meaning the number corresponding to the position in our components list should be equivalent to row + 1 or row + 2 in the table (accounting for header)
            print(f"Component with {component.component_id} is already in the inventory")

            return True
            

    # pass in unique component Id
    def find_component(self, componentId):
        if componentId not in self.components:
            print(f"Component with ID {componentId} is not in the inventory!")
            return False
        
        print(f"Component with ID {componentId} is in the inventory!")
        return True

        # inventory shouldnt be able to add things within the actual jupyter notebook.
        # not even sure if we should be able to remove things from the inventory because it seems
        # to somewhat ruin the purpose. I am not sure if we should just keep some external csv file to populate and remobve
        # or when they add something, I would need to figure out a way to write that to a csv file. 
        # hwo would we track if they manual entered something in the ipysheet table, i guess when they 
        # type something in and add a row and click something such as "submit" -> we can
        # validate the data in that cell they added,and then save it to a csv data file store

