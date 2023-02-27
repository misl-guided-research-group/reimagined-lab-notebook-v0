from datetime import datetime
import ipysheet
from IPython.display import display
import pandas as pd
import ipywidgets as widgets
from ipysheet.easy import cell
from ipywidgets import Layout
import re

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
        
        # create an empty sheet to display the inventory
        self.sheet = ipysheet.sheet(rows=2, columns=5)
        self.header = ['Component ID', 'Name','Concentration','Added By', "Date Added"]
        for i, col_name in enumerate(self.header):
            ipysheet.cell(row=0, column=i, value=col_name)

        ipysheet.renderer(code=self.renderer_contains_component, name="component_exists")

        self.display_options()

    def add_row(self,btn):
        self.sheet.rows += 1

    def create_add_button(self):
        add_button = widgets.Button(description="Add Component to Inventory")
        out = widgets.Output()

        add_button.on_click(self.add_row)
        widgets.VBox([add_button,self.sheet])


        display(add_button)
        return add_button

    def renderer_contains_component(self):
        return {
            'backgroundColor': 'green'
        }
    
    def display_options(self):
        add_button = widgets.Button(description="Add Component",  layout=Layout(display='flex', flex_flow='row'))
        remove_button = widgets.Button(description="Remove Component",  layout=Layout(display='flex', flex_flow='row'))
        display_button = widgets.Button(description="Display All Components",  layout=Layout(display='flex', flex_flow='row'))
        search_button = widgets.Button(description="Search for Component",  layout=Layout(display='flex', flex_flow='row'))

        def hand(self):
            print("Clicked")

        add_button.on_click(hand)
        remove_button.on_click(hand)
        display_button.on_click(self.display_inventory)
        search_button.on_click(hand)

        out = widgets.Output()
        widgets.VBox([add_button, remove_button, display_button, search_button, self.sheet])

        display(add_button)
        display(remove_button)
        display(display_button)
        display(search_button)

        return [add_button, remove_button, display_button, search_button]

    # pass in component object as a whole
    def contains_component(self, component):
                # if the unique component already exists, then display table, highlight cell green
        # and indicate it is already in there.
        if component.component_id in self.components:
             # can use this mechanism since order of elements is persistent in python
                # meaning the number corresponding to the position in our components list should be equivalent to row + 1 or row + 2 in the table (accounting for header)
            index = self.components.index(component.component_id)
            #the above is 0th index. so in my table should be +1

            pos = index + 1

            row = ipysheet.row(pos,[component.component_id, component.component_name, component.concentration, component.creator.first_name, component.curr_time], background_color="green")
            row.send_state()

            print(f"Component with {component.component_id} is already in the inventory")

            return True
            

    def add_component(self, component):

        #is it possible for me to grab the data when they enter it in the table in real time
        # or maybe i can give them option to add compoennt, dispaly some form, and have the
        # table dynamically update.

        if component.component_id in self.components:
            self.contains_component(component)
            return

        self.components.append(component.component_id)
        # get the index of the last row in the sheet
        last_row = len(self.components)
        self.sheet.rows += 1

# need some error handling done here

        # set the values for the new row
        ipysheet.cell(last_row,0,component.component_id)
        ipysheet.cell(last_row, 1,component.component_name)
        ipysheet.cell(last_row, 2,component.concentration)
        ipysheet.cell(last_row, 3,component.creator.first_name + ' ' + component.creator.last_name)
        ipysheet.cell(last_row, 4,component.curr_time)

    # pass in unique component Id
    def find_component(self, componentId):
        if componentId not in self.components:
            print(f"Component with ID {componentId} is not in the inventory!")
            self.generate_similar_keys(componentId)
            return False
        
        print(f"Component with ID {componentId} is in the inventory!")
        return True
        
    # generate similar keys as their failed search utilizing regex, delimitted by _
    def generate_similar_keys(self, componentId):
        # delimit the component ID as they are in the for Ab_10, in this case
        # we dont want the concentration for our regex match, bc we want to implement 
        # a basic recommendation algorithm 

        # need to transform to lower case in case they want to search!
        #can specify format of name _ concentration
        if not componentId:
            return

        generalId = (componentId.split("_")[0]).lower()

        for id in self.components:
            if generalId in id.lower():
                print(f"Consider checking out {id} instead!")


    def search_for_components(self):
        mixtureMenu = widgets.Dropdown(
        options=['MgCI_10X', 'h20', 'NacI_1X'],
        value='MgCI_10X',
        description='Search for mixture:',
        disabled=False,
        )

        return mixtureMenu

    def display_inventory(self, callback):
        display(self.sheet)


        # inventory shouldnt be able to add things within the actual jupyter notebook.
        # not even sure if we should be able to remove things from the inventory because it seems
        # to somewhat ruin the purpose. I am not sure if we should just keep some external csv file to populate and remobve
        # or when they add something, I would need to figure out a way to write that to a csv file. 
        # hwo would we track if they manual entered something in the ipysheet table, i guess when they 
        # type something in and add a row and click something such as "submit" -> we can
        # validate the data in that cell they added,and then save it to a csv data file store
