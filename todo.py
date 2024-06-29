import json
import os
import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk

class ToDoList:
    def __init__(self, file_name='todo_list.json'):
        self.file_name = file_name
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, 'r') as file:
                return json.load(file)
        return []

    def save_tasks(self):
        with open(self.file_name, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        self.save_tasks()

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
            self.save_tasks()

    def update_task(self, index, new_task):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["task"] = new_task
            self.save_tasks()

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            self.save_tasks()

class AutoScrollbar(tk.Scrollbar):
    def set(self, lo, hi):
        if float(lo) <= 0.0 and float(hi) >= 1.0:
            self.pack_forget()
        else:
            if self.cget("orient") == tk.HORIZONTAL:
                self.pack(side=tk.BOTTOM, fill=tk.X)
            else:
                self.pack(side=tk.RIGHT, fill=tk.Y)
        tk.Scrollbar.set(self, lo, hi)

class ToDoListApp:
    def __init__(self, root):
        self.todo_list = ToDoList()
        self.root = root
        self.root.title("To-Do List Application")

        self.frame = tk.Frame(root)
        self.frame.pack(padx=10, pady=10)

        self.heading = tk.Label(self.frame, text="TO-DO LIST", font=('Calibri', 32, 'bold'))
        self.heading.pack(pady=10)

        self.listbox_frame = tk.Frame(self.frame)
        self.listbox_frame.pack()

        self.listbox = tk.Listbox(self.listbox_frame, selectmode=tk.SINGLE, width=60, height=15, font=('Calibri', 14), bd=2, relief="groove")
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.v_scrollbar = AutoScrollbar(self.listbox_frame, orient=tk.VERTICAL)
        self.v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.h_scrollbar = AutoScrollbar(self.frame, orient=tk.HORIZONTAL)
        self.h_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

        self.listbox.config(yscrollcommand=self.v_scrollbar.set, xscrollcommand=self.h_scrollbar.set)
        self.v_scrollbar.config(command=self.listbox.yview)
        self.h_scrollbar.config(command=self.listbox.xview)

        self.entry = tk.Entry(root, width=60, font=('Calibri', 14))
        self.entry.pack(padx=10, pady=10)

        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)

        style = ttk.Style()
        style.configure("TButton", font=('Calibri', 16), padding=10)

        self.add_button = ttk.Button(self.button_frame, text="Add Task", command=self.add_task, style="TButton")
        self.add_button.grid(row=0, column=0, padx=10, pady=5)

        self.complete_button = ttk.Button(self.button_frame, text="Complete Task", command=self.complete_task, style="TButton")
        self.complete_button.grid(row=0, column=1, padx=10, pady=5)

        self.update_button = ttk.Button(self.button_frame, text="Update Task", command=self.update_task, style="TButton")
        self.update_button.grid(row=1, column=0, padx=10, pady=5)

        self.delete_button = ttk.Button(self.button_frame, text="Delete Task", command=self.delete_task, style="TButton")
        self.delete_button.grid(row=1, column=1, padx=10, pady=5)

        self.load_tasks()

    def load_tasks(self):
        self.listbox.delete(0, tk.END)
        for idx, task in enumerate(self.todo_list.tasks):
            status = "Done" if task["completed"] else "Not Done"
            self.listbox.insert(tk.END, f"{idx + 1}. {task['task']} - {status}")

    def add_task(self):
        task = self.entry.get().strip().capitalize()
        if task:
            self.todo_list.add_task(task)
            self.entry.delete(0, tk.END)
            self.load_tasks()
        else:
            messagebox.showwarning("Input Error", "Task cannot be empty")

    def complete_task(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            self.todo_list.complete_task(selected_index[0])
            self.load_tasks()
        else:
            messagebox.showwarning("Selection Error", "No task selected")

    def update_task(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            current_task = self.todo_list.tasks[selected_index[0]]["task"]
            new_task = simpledialog.askstring("Update Task", "Edit your task:", initialvalue=current_task)
            if new_task:
                self.todo_list.update_task(selected_index[0], new_task.strip().capitalize())
                self.load_tasks()
        else:
            messagebox.showwarning("Selection Error", "No task selected")

    def delete_task(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            confirm = messagebox.askyesno("Delete Task", "Are you sure you want to delete the selected task?")
            if confirm:
                self.todo_list.delete_task(selected_index[0])
                self.load_tasks()
        else:
            messagebox.showwarning("Selection Error", "No task selected")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
