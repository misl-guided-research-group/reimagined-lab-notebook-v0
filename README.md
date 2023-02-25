# reimagined-lab-notebook-prototype-v0

Developers / Researchers : Please create a seperate branch for the individual core features. 

 This repository contains the initial key features that were scoped out utilizing jupyter notebooks + extensions + reactive programming. Version 0 of the reimagined lab notebook ideally should support the following features:

- [ ]  **Calculations: Mixing Calculation Automation (i.e finding concentrations, amounts etc)**

- **FrontEnd Components**
    - widgets, dropbox ( select a chemical), slider volume(take care of edge cases such as negative values), submit
    - print out mixing table (like table donavan had displayed in the alhambra)
- **Backend Components**
    - mixing calculation alhambra
    - `mixCalc(t,b,c)`
    - figuring out iteration of FixedComponents

- [ ]  **Basic Inventory Support → Reactive Updates (i.e Do we have the concentration or not?)**

- **FrontEnd Components**

    - display inventory button → inventory displays like a table
    - close inventory button
    - text input to put desired component search
    - delete button (pause)
    - displays name + concentration
- **Backend Components**
    - unique ID  (name + concentration)  (readable keys)
    - `containsItem()`
    - `addItem(), deleteItem()`
    - buffers? (salt concentrations → magnesium, sodium potassium )
    - specifying salt concentrations in a format that allows simple calculations
    - inventory volume sanity checks for the norm
    - (date + person) who created inventory

- [ ]  **Generating tips / errors based on if values look suspicious or incorrect**
- **FrontEnd Components**
    - manually print error or warning  (meaningful usage message)
    - potential color change of a cell or row
    - or warning pop up maybe ?
- **Backend Components**
    - `isAmountSus( )`  → too little or too high, can't make something more concentrated than what you actually have
    - `isInInventory( )`
    - Alhambra Errors (taken care of)


    component_concentration = input("Please enter the concentration of the mixture")
            print(component_concentration)

            member_name = input("Please enter your first and last name seperated by a space")
            print(member_name) # might need to dynamically get the name

            # self, creator, component_name, concentration, is_buffer)
            # maybe just create a global member to be persisted throughout the entire cycle 
            first_name = member_name.split(" ")[0]
            last_name = member_name.split(" ")[1]

            member = Member(first_name, last_name)

            new_component = Component(member,component_name, component_concentration,False)
            

            #is it possible for me to grab the data when they enter it in the table in real time
            # or maybe i can give them option to add compoennt, dispaly some form, and have the
            # table dynamically update.

            if new_component.component_id in self.components:
                self.contains_component(new_component)
                return

            self.components.append(new_component.component_id)
            # get the index of the last row in the sheet
            last_row = len(self.components)
            self.sheet.rows += 1
    
# need some error handling done here

            # set the values for the new row
            ipysheet.cell(last_row,0,new_component.component_id)
            ipysheet.cell(last_row, 1,new_component.component_name)
            ipysheet.cell(last_row, 2,new_component.concentration)
            ipysheet.cell(last_row, 3,new_component.creator.first_name + ' ' + new_component.creator.last_name)
            ipysheet.cell(last_row, 4,new_component.curr_time)