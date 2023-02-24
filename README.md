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