import tkinter as tk
from tkinter import ttk
from tkinter.font import Font

window = tk.Tk()
window.title("CRUD")

style = ttk.Style()

style.configure("Treeview", padding=(10, 5))
style.configure("Treeview.Heading", font=(
    "Helvetica", 12, "bold"), padding=(0, 10))


def load_products():
    products = [
        ("Product 1", "Category A", "$19.99"),
        ("Product 2", "Category B", "$29.99"),
        ("Product 3", "Category A", "$24.99"),
    ]

    for product in products:
        table.insert("", "end", values=product, tags=('cell_text',))

    table.tag_configure('cell_text', font=(
        "Helvetica", 10))


def add_product():
    # Retrieve data from the Entry or Text widgets
    # Retrieve text from the Text widget
    product_name = product_name_entry.get("1.0", "end-1c")
    quantity = quantity_entry.get("1.0", "end-1c")
    price = price_entry.get("1.0", "end-1c")

    # Print the retrieved data (you can replace this with your desired action)
    print("Product Name:", product_name)
    print("Quantity:", quantity)
    print("Price:", price)


def modify_product():
    selected_item = table.selection()
    if selected_item:
        # Get the values of the selected product
        values = table.item(selected_item, 'values')

        # Create a new window for modification
        modify_window = tk.Toplevel(window)
        modify_window.title("Modify Product")

        # Populate the new window with the selected product details
        product_name_label = tk.Label(modify_window, text="Product Name:")
        product_name_label.grid(row=0, column=0)
        product_name_entry = tk.Entry(modify_window)
        product_name_entry.grid(row=0, column=1)
        product_name_entry.insert(0, values[0])  # Set the initial value

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

        # Function to update the Treeview with the modified details
        def update_product():
            new_values = (
                product_name_entry.get(),
                quantity_entry.get(),
                price_entry.get()
            )
            table.item(selected_item, values=new_values)
            modify_window.destroy()

        # Add a "Save" button to confirm the changes
        save_button = tk.Button(
            modify_window, text="Save", command=update_product)
        save_button.grid(row=3, columnspan=2)


def delete_product():
    selected_item = table.selection()
    if selected_item:
        table.delete(selected_item)


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
