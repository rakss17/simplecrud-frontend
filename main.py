import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
import tkinter.messagebox as messagebox
import requests

window = tk.Tk()
window.title("CRUD")

style = ttk.Style()

style.configure("Treeview", padding=(10, 5))
style.configure("Treeview.Heading", font=(
    "Helvetica", 12, "bold"), padding=(0, 10))


def load_products():
    try:

        response = requests.get("http://localhost:8000/products/create-fetch/")

        if response.status_code == 200:

            products = response.json()

            for item in table.get_children():
                table.delete(item)

            for product in products:
                table.insert("", "end", values=(
                    product['product_name'], product['quantity'], product['price']))

            messagebox.showinfo('Success', 'Products loaded successfully!')
        else:
            messagebox.showerror(
                'Error', f'Failed to fetch data. Status Code: {response.status_code}')

    except requests.exceptions.RequestException as e:
        messagebox.showerror('Error', f'Failed to fetch data. Error: {str(e)}')


def add_product():
    product_name = product_name_entry.get("1.0", "end-1c")
    quantity = quantity_entry.get("1.0", "end-1c")
    price = price_entry.get("1.0", "end-1c")

    if not product_name or not quantity or not price:
        messagebox.showerror('Error', 'Please fill out all fields')
        return

    product_data = {
        'product_name': product_name,
        'quantity': quantity,
        'price': price
    }

    try:

        response = requests.post(
            "http://localhost:8000/products/create-fetch/", json=product_data)

        if response.status_code == 201:

            table.insert("", "end", values=(product_name, quantity, price))

            messagebox.showinfo('Success', 'Product added successfully!')

            product_name_entry.delete("1.0", "end-1c")
            quantity_entry.delete("1.0", "end-1c")
            price_entry.delete("1.0", "end-1c")
        else:
            messagebox.showerror(
                'Error', f'Failed to add product. Status Code: {response.status_code}')

    except requests.exceptions.RequestException as e:
        messagebox.showerror(
            'Error', f'Failed to add product. Error: {str(e)}')


def modify_product():

    selected_item = table.selection()
    if selected_item:

        values = table.item(selected_item, 'values')

        modify_window = tk.Toplevel(window)
        modify_window.title("Modify Product")

        product_name_label = tk.Label(modify_window, text="Product Name:")
        product_name_label.grid(row=0, column=0)
        product_name_entry = tk.Entry(modify_window)
        product_name_entry.grid(row=0, column=1)
        product_name_entry.insert(0, values[0])

        quantity_label = tk.Label(modify_window, text="Quantity:")
        quantity_label.grid(row=1, column=0)
        quantity_entry = tk.Entry(modify_window)
        quantity_entry.grid(row=1, column=1)
        quantity_entry.insert(0, values[1])

        price_label = tk.Label(modify_window, text="Price:")
        price_label.grid(row=2, column=0)
        price_entry = tk.Entry(modify_window)
        price_entry.grid(row=2, column=1)
        price_entry.insert(0, values[2])

        def update_product():
            new_values = (
                product_name_entry.get(),
                quantity_entry.get(),
                price_entry.get()
            )
            table.item(selected_item, values=new_values)
            messagebox.showinfo('Success', 'Product modified successfully!')
            modify_window.destroy()

        save_button = tk.Button(
            modify_window, text="Save", command=update_product)
        save_button.grid(row=3, columnspan=2)
    else:
        messagebox.showerror('Error', 'Please select a product to modify!')


def delete_product():
    selected_item = table.selection()
    if selected_item:
        table.delete(selected_item)
        messagebox.showinfo('Success', 'Product deleted successfully!')
    else:
        messagebox.showerror('Error', 'Please select a product to remove!')


screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_width = 700
window_height = 700
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
window.geometry(f"{window_width}x{window_height}+{x}+{y}")
window.configure(bg="#D9D9D9")

label_font = Font(family="Helvetica", size=16, weight="bold")
label = tk.Label(window, text="Simple Inventory System (CRUD)",
                 bg="#D9D9D9", font=label_font)
label.pack(padx=50, pady=30)

columns = ("Product Name", "Quantity", "Price")
table = ttk.Treeview(
    window,
    columns=columns,
    show="headings",
    height=10,
    style="Treeview"
)

product_font = Font(family="Helvetica", size=16, weight="bold")

for col in columns:
    table.heading(col, text=col)
    table.column(col, width=150, anchor="center")


load_products()

table.pack(padx=0, pady=0)


main_frame = tk.Frame(window)
main_frame.pack(side="top", pady=20)

child_frame = tk.Frame(main_frame, width=350, height=200, bg="#979C9B")
child_frame.grid(row=0, column=0)

product_name_label = tk.Label(
    child_frame, text="Product Name:", font=("Helvetica", 12), bg="#979C9B")
product_name_label.grid(row=0, column=0, padx=10, pady=10)

product_name_entry = tk.Text(child_frame, font=(
    "Helvetica", 12), height=2, width=20, wrap=tk.WORD)
product_name_entry.grid(row=0, column=1, padx=10, pady=10)

quantity_label = tk.Label(
    child_frame, text="Quantity:", font=("Helvetica", 12), bg="#979C9B")
quantity_label.grid(row=1, column=0, padx=10, pady=10)

quantity_entry = tk.Text(child_frame, font=(
    "Helvetica", 12), height=2, width=20, wrap=tk.WORD)
quantity_entry.grid(row=1, column=1, padx=10, pady=10)

price_label = tk.Label(child_frame, text="Price:",
                       font=("Helvetica", 12), bg="#979C9B")
price_label.grid(row=2, column=0, padx=10, pady=10)

price_entry = tk.Text(child_frame, font=("Helvetica", 12),
                      height=2, width=20, wrap=tk.WORD)
price_entry.grid(row=2, column=1, padx=10, pady=10)

button_add = tk.Button(child_frame, text='Add',
                       font="Helvetica 15 bold", width=10, bg="#79E784", command=add_product)
button_add.grid(row=3, columnspan=2, pady=10)


child_frame2 = tk.Frame(main_frame, width=150, height=200, bg="#D9D9D9")
child_frame2.grid(row=0, column=1)

button_modify = tk.Button(child_frame2, text='Modify',
                          font="Helvetica 15 bold", width=10, command=modify_product)
button_delete = tk.Button(child_frame2, text='Remove',
                          font="Helvetica 15 bold", bg="#EC5858", foreground="white", width=10, command=delete_product)

button_modify.pack(side="top", padx=5)
button_delete.pack(side="bottom", padx=5)


window.mainloop()
