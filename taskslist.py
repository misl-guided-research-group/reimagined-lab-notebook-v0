import ipywidgets as widgets
from IPython.display import display, clear_output
import datetime

# Displays a real-time checkbox tasklist with add and remove operations for tasks. A task 
# in this can only be checked off once, outputting the timestamp for when it was 
# checked off. 
class TaskList:
    def __init__(self):
        # Container for tasks 
        self.tasks = []
        
        # Buttons for the operations 
        self.add_button = widgets.Button(description="Add Task")
        self.remove_button = widgets.Button(description="Remove Task")
        self.buttons_layout = widgets.HBox([self.add_button, self.remove_button])
        
        self.add_button.on_click(self.add_task)
        self.remove_button.on_click(self.remove_task)
        
        display(self.buttons_layout)
    
    # Adds a new non-duplicate task to the tasklist
    def add_task(self, _):
        task_text = widgets.Text(description="Task:")
        add_button = widgets.Button(description="Add")
        
        def handle_add_button(_):
            new_task = task_text.value.strip()
            if new_task:
                for task in self.tasks:
                    if task['name'] == new_task:
                        break
                else:
                    self.tasks.append({'name': new_task, 'completed': False, 'timestamp': None})
                    self.update_task_list()
        
        add_button.on_click(handle_add_button)
        display(task_text, add_button)
    
    # Removes a task from the tasklist
    def remove_task(self, _):
        if not self.tasks:
            print("No tasks found.")
            return
        
        task_dropdown = widgets.Dropdown(options=[task['name'] for task in self.tasks], description="Task:")
        remove_button = widgets.Button(description="Remove")
        
        def handle_remove_button(_):
            task_name = task_dropdown.value
            self.tasks = [task for task in self.tasks if task['name'] != task_name]
            self.update_task_list()
        
        remove_button.on_click(handle_remove_button)
        display(task_dropdown, remove_button)
    
    # Updates the tasklist display
    def update_task_list(self):
        task_list = widgets.VBox()

        for task in self.tasks:
            checkbox = widgets.Checkbox(value=task['completed'], description=task['name'])
            timestamp_label = widgets.Label()

            if task['completed']:
                timestamp_label.value = f"Completed at: {task['timestamp']}"
                checkbox.disabled = True

            def handle_checkbox_change(change, task_name=task['name']):
                self.mark_completed(task_name, change.new)
                if change.new:
                    timestamp_label.value = f"Completed at: {task['timestamp']}"
                    checkbox.disabled = True

            checkbox.observe(handle_checkbox_change, 'value')

            task_row = widgets.HBox([checkbox, timestamp_label])

            task_list.children += (task_row,)

        clear_output()
        display(self.buttons_layout, task_list)
    
    # Marks a task as completed with the given value and updates the timestamp
    def mark_completed(self, task_name, value):
        for task in self.tasks:
            if task['name'] == task_name:
                task['completed'] = value
                if value:
                    task['timestamp'] = datetime.datetime.now()
                break

        self.update_task_list()


    
