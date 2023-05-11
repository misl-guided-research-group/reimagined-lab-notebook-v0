from datetime import datetime
from IPython.display import display
import ipywidgets as widgets
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

class Inventory:
    def __init__(self):
        self.components = []
        
        # create an empty dataframe with the desired columns
        self.df = pd.DataFrame(columns=['Creator', 'Component Name', 'Concentration', 'Component ID', 'Is Buffer', 'Timestamp'])

        # display the widgets
        self.display_options()

    def display_options(self):
        add_button = widgets.Button(description="Add Component")
        remove_button = widgets.Button(description="Remove Component")
        display_button = widgets.Button(description="Display All Components")
        search_button = widgets.Button(description="Search for Component")

        add_button.on_click(self.add_component)
        remove_button.on_click(self.remove_component)
        search_button.on_click(self.contains_component)
        display_button.on_click(self.display_inventory)

        button_layout = widgets.HBox([add_button, remove_button, display_button, search_button])
        display(button_layout)

    # Updates all the displays 
    def display_inventory(self, _): 
        self.df = pd.DataFrame([vars(c) for c in self.components])
        print(self.df)
        
    # Adds a new component to the inventory.
    #   - Note: use of enter inputs all values 
    def add_component(self, _):
        # Create text input widgets
        creator_text = widgets.Text(description="Creator:")
        component_name_text = widgets.Text(description="Component Name:")
        concentration_text = widgets.Text(description="Concentration:")
        is_buffer_text = widgets.Text(description="Is Buffer:")

        # Display the input widgets
        display(creator_text)
        display(component_name_text)
        display(concentration_text)
        display(is_buffer_text)

        # Define a function to handle input submission
        def handle_submit(sender):
            # Retrieve the input values
            creator = creator_text.value
            component_name = component_name_text.value
            concentration = concentration_text.value
            is_buffer = is_buffer_text.value

            # Create the new component
            new_component = Component(creator, component_name, concentration, is_buffer)

            # Check if the component is already contained
            if self.contains_component(new_component):
                return

            # Add the new component
            self.components.append(new_component)

            # Display a message to indicate the component was added
            print(f"Component with ID {new_component.component_id} was successfully added to the inventory.")

            # Close the input widgets
            creator_text.close()
            component_name_text.close()
            concentration_text.close()
            is_buffer_text.close()

        # Register the submit handler
        creator_text.on_submit(handle_submit)
        component_name_text.on_submit(handle_submit)
        concentration_text.on_submit(handle_submit)
        is_buffer_text.on_submit(handle_submit)

    # Removes an existing component in the inventory 
    def remove_component(self, _):
        # Widget to get Component ID
        component_id_text = widgets.Text(description="Component ID:")

        # Display the input widgets
        display(component_id_text)

        # Define a function to handle input submission
        def handle_submit(sender):
            # Retrieve the input values
            component_id = component_id_text.value

            # Check if the component exists in the inventory
            for component in self.components:
                if component.component_id == component_id:
                    # Removes the component from the inventory
                    self.components.remove(component)

                    # Display a message to indicate the component was removed
                    print(f"Component with ID {component_id} was successfully removed from the inventory.")

                    # Update the dataframe
                    self.df = self.df[self.df['Component ID'] != component_id]

                    return 

            # Display a message to indicate the component was not found
            print(f"Component with ID {component_id} is not within the inventory.")

            # Close the input widgets
            component_id_text.close()
        
        # Register the submit handler
        component_id_text.on_submit(handle_submit)

    # pass in component object as a whole. this function differse 
    # to find_component in that it will do the highlighting logic. 
    def contains_component(self, _):
        # Widget to get Component ID
        component_id_text = widgets.Text(description="Component ID:")

        # Display the input widgets
        display(component_id_text)

        # Define a function to handle input submission
        def handle_submit(sender):
            # Retrieve the input values
            component_id = component_id_text.value

            # Check if the component exists in the inventory
            for component in self.components:
                if component.component_id == component_id:

                    # Display a message to indicate the component is in the inventory 
                    print(f"Component with ID {component_id} is contained within inventory.")
                    return 

            # Close the input widgets
            component_id_text.close()
        
        # Register the submit handler
        component_id_text.on_submit(handle_submit)

# inventory shouldnt be able to add things within the actual jupyter notebook.
# not even sure if we should be able to remove things from the inventory because it seems
# to somewhat ruin the purpose. I am not sure if we should just keep some external csv file to populate and remobve
# or when they add something, I would need to figure out a way to write that to a csv file. 
# hwo would we track if they manual entered something in the ipysheet table, i guess when they 
# type something in and add a row and click something such as "submit" -> we can
# validate the data in that cell they added,and then save it to a csv data file store

