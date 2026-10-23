import tkinter as tk
from tkinter import ttk, messagebox

def add_task():
    task = task_entry.get().strip()
    if task:
        task_list.insert(tk.END, "○ " + task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showinfo("BeeBuddy", "Enter a task first.")

def complete_task():
    selected = task_list.curselection()
    if selected:
        index = selected[0]
        task = task_list.get(index)
        if task.startswith("○ "):
            task_list.delete(index)
            task_list.insert(index, "✓ " + task[2:])
    else:
        messagebox.showinfo("BeeBuddy", "Select a task first.")

def summarize():
    text = source_text.get("1.0", tk.END).strip()
    if not text:
        messagebox.showinfo("BeeBuddy", "Enter some text first.")
        return

    sentences = [
        sentence.strip()
        for sentence in text.replace("\n", " ").split(".")
        if sentence.strip()
    ]

    result = ". ".join(sentences[:3])
    if result and not result.endswith((".", "!", "?")):
        result += "."

    output_text.config(state="normal")
    output_text.delete("1.0", tk.END)
    output_text.insert("1.0", result)
    output_text.config(state="disabled")

root = tk.Tk()
root.title("BeeBuddy AI - Student Assistant")
root.geometry("650x520")

ttk.Label(
    root, text="BeeBuddy AI",
    font=("Arial", 22, "bold")
).pack(pady=12)

tabs = ttk.Notebook(root)
tabs.pack(fill="both", expand=True, padx=12, pady=8)

# Task manager
task_tab = ttk.Frame(tabs, padding=12)
tabs.add(task_tab, text="Tasks")

task_entry = ttk.Entry(task_tab)
task_entry.pack(fill="x", pady=8)

ttk.Button(
    task_tab, text="Add Task", command=add_task
).pack(pady=4)

task_list = tk.Listbox(task_tab, height=12)
task_list.pack(fill="both", expand=True, pady=8)

ttk.Button(
    task_tab, text="Mark Complete", command=complete_task
).pack()

# Notes
notes_tab = ttk.Frame(tabs, padding=12)
tabs.add(notes_tab, text="Notes")

notes = tk.Text(notes_tab, wrap="word")
notes.pack(fill="both", expand=True)

def save_note():
    content = notes.get("1.0", tk.END).strip()
    if content:
        messagebox.showinfo(
            "BeeBuddy", "Your note is ready:\n\n" + content[:300]
        )
    else:
        messagebox.showinfo("BeeBuddy", "Write a note first.")

ttk.Button(
    notes_tab, text="Preview Note", command=save_note
).pack(pady=8)

# Simple text summarizer
summary_tab = ttk.Frame(tabs, padding=12)
tabs.add(summary_tab, text="Summarizer")

ttk.Label(
    summary_tab, text="Enter text to summarize:"
).pack(anchor="w")

source_text = tk.Text(summary_tab, height=10, wrap="word")
source_text.pack(fill="both", expand=True, pady=8)

ttk.Button(
    summary_tab, text="Summarize", command=summarize
).pack(pady=5)

ttk.Label(summary_tab, text="Summary:").pack(anchor="w")

output_text = tk.Text(
    summary_tab, height=5, wrap="word", state="disabled"
)
output_text.pack(fill="x", pady=5)

ttk.Label(
    root, text="Python desktop prototype • No live Bee integration",
    foreground="gray"
).pack(pady=6)

root.mainloop()
