import ipywidgets as widgets
import datetime

# Creates a tasklist that is managed by the client with adding, removing, and 
# checking off tasks 
class TaskList:
    def __init__(self):
        self.tasks = {}
    
    # Adds a task
    def add_task(self, task_name):
        self.tasks[task_name] = {'completed': False, 'timestamp': None}
    
    # Removes a task 
    def remove_task(self, task_name):
        del self.tasks[task_name]
    
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