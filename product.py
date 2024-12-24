from tkinter import *

# Create the main window
window = Tk()
window.geometry("700x700")

# Function to calculate the product
def calculate():
    try:
        num1 = float(en1.get())  # Get the first number
        num2 = float(en2.get())  # Get the second number
        result = num1 * num2
        print(result)  # Print the result
        result_label.config(text=f"Product: {result}")  # Display the result
    except ValueError:
        result_label.config(text="Invalid input! Please enter numbers.")

# Labels and Entry widgets
l1 = Label(window, text="Enter 1st number:", bg="black", fg="white", height=1, width=25)
l2 = Label(window, text="Enter 2nd number:", bg="black", fg="white", height=1, width=25)
en1 = Entry(window, width=25)
en2 = Entry(window, width=25)

# Button to calculate
b = Button(window, text="Calculate", bg="green", command=calculate)

# Label to display the result
result_label = Label(window, text="", fg="blue", font=("Arial", 12))

# Pack widgets into the window
l1.pack(pady=10)
en1.pack(pady=10)
l2.pack(pady=10)
en2.pack(pady=10)
b.pack(pady=20)
result_label.pack(pady=10)

# Run the application
window.mainloop()
