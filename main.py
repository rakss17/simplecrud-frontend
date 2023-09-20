import tkinter as tk



window = tk.Tk()
window.title("CRUD")
window.geometry("500x500")


# def fetch_data():
#     response = requests.get("http://localhost:8000/api/data/")
#     data = response.json()
#     # Update the GUI with the retrieved data


label = tk.Label(window, text="Welcome to Django Tkinter App")
button = tk.Button(window, text="Fetch Data")


label.pack()
button.pack()


window.mainloop()
