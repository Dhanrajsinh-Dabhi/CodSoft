import tkinter as tk
from tkinter import messagebox

# Create an empty list to store contacts
contacts = []
selected_contact = None  # Variable to store selected contact (name, phone)

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    if name and phone:
        contacts.append({"name": name, "phone": phone})
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        update_contact()
    else:
        messagebox.showerror("Error", "Please fill both Name and Phone fields!")

def update_contact():
    contact_list.delete(0, tk.END)
    for contact in contacts:
        contact_list.insert(tk.END, f"{contact['name']} - {contact['phone']}")

def delete_contact():
    selected_index = contact_list.curselection()
    if selected_index:
        contact_list.delete(selected_index[0])
        contacts.pop(selected_index[0])
    else:
        messagebox.showinfo("Info", "Please select a contact to delete!")


def edit_contact():
    global selected_contact
    selected_index = contact_list.curselection()
    if selected_index:
        selected_contact = contacts[selected_index[0]]
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        name_entry.insert(0, selected_contact["name"])
        phone_entry.insert(0, selected_contact["phone"])
        add_button.config(state=tk.DISABLED)
        save_button.grid(row=3, column=1, padx=5, pady=5, sticky=tk.E)  # Position next to edit button

def save_contact():
    global selected_contact
    selected_index = contact_list.curselection()
    if selected_contact:
        contacts[selected_index[0]]["name"] = name_entry.get()
        contacts[selected_index[0]]["phone"] = phone_entry.get()
        update_contact()
        selected_contact = None
        add_button.config(state=tk.NORMAL)
        save_button.grid_remove() 
    else:
        messagebox.showinfo("Info", "Please select a contact to edit!")


# Creating tkinter window
window = tk.Tk()
window.title("Contact Book")
window.geometry("800x800")

name_label = tk.Label(window, text="Name:")
name_entry = tk.Entry(window)

phone_label = tk.Label(window, text="Phone:")
phone_entry = tk.Entry(window)

contact_list = tk.Listbox(window)

add_button = tk.Button(window, text="Add Contact", command=add_contact)
edit_button = tk.Button(window, text="Edit Contact", command=edit_contact)
save_button = tk.Button(window, text="Save", command=save_contact)
delete_button = tk.Button(window, text="Delete", command=delete_contact)  # Corrected typo


# Arrange the widgets in the window
name_label.grid(row=0, column=0, padx=5, pady=5)

name_entry.grid(row=0, column=1, padx=5, pady=5)

phone_label.grid(row=1, column=0, padx=5, pady=5)
phone_entry.grid(row=1, column=1, padx=5, pady=5)

contact_list.grid(row=2, columnspan=2, padx=5, pady=5)

add_button.grid(row=3, column=0, padx=5, pady=5, sticky=tk.E)
edit_button.grid(row=3, column=1, padx=5, pady=5)
delete_button.grid(row=3, column=2, padx=5, pady=5, sticky=tk.W)


window.mainloop()
