import json
import tkinter as tk
from tkinter import messagebox, filedialog

class Task:
    def __init__(self, title, description, status):
        self.title = title
        self.description = description
        self.status = status

class ToDoListApp:
    def __init__(self):
        self.tasks = []

        self.root = tk.Tk()
        self.root.title("To-Do List App")
        self.root.geometry("600x600")

        self.title_label = tk.Label(self.root, text="Title", font=(15))
        self.title_label.pack(pady=2)

        self.title_entry = tk.Entry(self.root,width=50, font=(15))
        self.title_entry.pack(pady=2)

        self.desc_label = tk.Label(self.root, text="Description", font=(15))
        self.desc_label.pack(pady=2)

        self.desc_entry = tk.Entry(self.root,width=50, font=(15))
        self.desc_entry.pack(pady=2)

        self.add_button = tk.Button(self.root, text="Add Task",  font=(15),command=self.add_task)
        self.add_button.pack(pady=2)

        self.task_listbox = tk.Listbox(self.root, height=10,width=50, font=(15))
        self.task_listbox.pack(pady=2)

        self.delete_button = tk.Button(self.root, text="Delete Task", font=(15), command=self.delete_task)
        self.delete_button.pack(pady=2)

        self.save_button = tk.Button(self.root, text="Save Tasks", font=(15), command=self.save_tasks)
        self.save_button.pack(pady=2)

        self.load_button = tk.Button(self.root, text="Load Tasks", font=(15), command=self.load_tasks)
        self.load_button.pack(pady=2)

        self.root.mainloop()

    def add_task(self):
        title = self.title_entry.get()
        description = self.desc_entry.get()

        if title and description:
            task = Task(title, description, "Not Completed")
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, f"{task.title} - {task.description}")
            self.title_entry.delete(0, tk.END)
            self.desc_entry.delete(0, tk.END)
            messagebox.showinfo("Success", "Task added successfully.")
        else:
            messagebox.showerror("Error", "Please enter both title and description.")

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.task_listbox.delete(index)
            del self.tasks[index]
            messagebox.showinfo("Success", "Task deleted successfully.")
        else:
            messagebox.showerror("Error", "Please select a task to delete.")

    def save_tasks(self):
        filename = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON Files", "*.json")])
        if filename:
            tasks_data = []
            for task in self.tasks:
                tasks_data.append({
                    'title': task.title,
                    'description': task.description,
                    'status': task.status
                })

            with open(filename, 'w') as file:
                json.dump(tasks_data, file)
            messagebox.showinfo("Success", "Tasks saved successfully.")

    def load_tasks(self):
        filename = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
        if filename:
            try:
                with open(filename, 'r') as file:
                    tasks_data = json.load(file)
                self.tasks = []
                self.task_listbox.delete(0, tk.END)
                for task_data in tasks_data:
                    task = Task(task_data['title'], task_data['description'], task_data['status'])
                    self.tasks.append(task)
                    self.task_listbox.insert(tk.END, f"{task.title} - {task.description}")
                messagebox.showinfo("Success", "Tasks loaded successfully.")
            except FileNotFoundError:
                messagebox.showerror("Error", "File not found.")

def main():
    todo_list_app = ToDoListApp()

if __name__ == "__main__":
    main()
