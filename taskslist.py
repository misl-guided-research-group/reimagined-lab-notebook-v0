import ipywidgets as widgets
import datetime
from IPython.display import display

# Creates a tasklist that is managed by the client with adding, removing, and 
# checking off tasks 
class TaskList:
    def __init__(self):
        self.tasks = {}
    
    # Adds a task 
    def add_task(self, _):
        task_text = widgets.Text(description="Task:")
        add_button = widgets.Button(description="Add")
        
        def handle_add_button(button):
            task = task_text.value.strip()
            if task:
                self.tasks.append(task)
                print(f"Task '{task}' added successfully!")
            else:
                print("Task cannot be empty.")
            
            # Clear the input field
            task_text.value = ''
        
        add_button.on_click(handle_add_button)
        display(task_text, add_button)
    
    # Removes a task 
    def remove_task(self, _):
        if not self.tasks:
            print("No tasks found.")
            return
        
        task_dropdown = widgets.Dropdown(options=self.tasks, description="Task:")
        remove_button = widgets.Button(description="Remove")
        
        def handle_remove_button(button):
            task = task_dropdown.value
            self.tasks.remove(task)
            print(f"Task '{task}' removed successfully!")
            
            # Refresh the dropdown options
            task_dropdown.options = self.tasks
            if not self.tasks:
                task_dropdown.close()
                remove_button.close()
            
        remove_button.on_click(handle_remove_button)
        display(task_dropdown, remove_button)
    
    # Marks a task completed 
    def mark_completed(self, task_name):
        if task_name in self.tasks:
            self.tasks[task_name]['completed'] = True
            self.tasks[task_name]['timestamp'] = datetime.datetime.now()
    
    # Displayed the tasklist 
    def get_task_list_widget(self):
        task_list_widgets = []
        for task_name in self.tasks:
            checkbox = widgets.Checkbox(description=task_name)
            checkbox.observe(lambda x: self.mark_completed(task_name) if x['new'] else None, 'value')
            task_list_widgets.append(checkbox)
        return widgets.VBox(task_list_widgets)