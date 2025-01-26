import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("500x500")
root.title("BMI Calculator")

# Title
tk.Label(root, text="Health & BMI Calculator", font=("Arial", 16)).pack()

# BMI Calculator Frame
frame = tk.Frame(root) 
frame.pack(pady=5)

# Weight Entry
tk.Label(frame, text="Enter your weight (kg):", font=("Arial", 12)).grid(row=0, column=0, padx=5)
weight_entry = tk.Entry(frame, font=("Arial", 12))
weight_entry.grid(row=0, column=1, padx=5)

# Height Entry
tk.Label(frame, text="Enter your Height (m):", font=("Arial", 12)).grid(row=1, column=0, padx=5)
height_entry = tk.Entry(frame, font=("Arial", 12))
height_entry.grid(row=1, column=1, padx=5)

# Shows Result
result_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
result_label.pack(pady=10)

# BMI Calculating Function
def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight <= 0 or height <= 0:
            messagebox.showinfo(title="error", message="Enter a valid number")
            return

        bmi = round(weight / height ** 2)

        if bmi < 18.5:
            result_label.config(text=f"Your BMI is {bmi}, you are underweight.")
        elif 18.5 <= bmi <= 24.9:
            result_label.config(text=f"Your BMI is {bmi}, you have a normal weight.")
        elif 25 <= bmi <= 29.9:
            result_label.config(text=f"Your BMI is {bmi}, you are overweight.")
        elif 30 <= bmi <= 34.9:
            result_label.config(text=f"Your BMI is {bmi}, you are obese (Class 1).")
        else:
            result_label.config(text=f"Your BMI is {bmi}, you are clinically obese (Class 2 or higher).")
    except ValueError:
        messagebox.showinfo(title="error", message="Enter valid information")

# BMI Calculate Button
bmi_calc_button = tk.Button(root, text="Calculate", font=("Arial", 14), command=calculate_bmi).pack(pady=10, padx=10)

# Height Conversion Section
tk.Label(root, text="Convert height from feet/inches to meters", font=("Arial", 16)).pack(pady=20)

# Height Conversion Frame
frame2 = tk.Frame(root)
frame2.pack(pady=5)

# Feet and Inches Input
tk.Label(frame2, text="Feet", font=("Arial", 12)).grid(row=0, column=0, padx=5)
feet_entry = tk.Entry(frame2, width=5, font=("Arial", 12))
feet_entry.grid(row=0, column=1, padx=5)

tk.Label(frame2, text="Inches", font=("Arial", 12)).grid(row=0, column=2, padx=5)
inch_entry = tk.Entry(frame2, width=5, font=("Arial", 12))
inch_entry.grid(row=0, column=3, padx=5)

# Height Conversion Result
meter_result = tk.Label(root, text="", font=("Arial", 12), fg="green")
meter_result.pack(pady=10)

# Height Conversion Function
def convert_to_meter():
    try:

        feet = float(feet_entry.get())
        inch = float(inch_entry.get())

        if feet <= 0 or inch < 0:
            messagebox.showinfo(title="error", message="Enter a valid number")
            return

        total_inches = (feet * 12) + inch
        meters = round(total_inches * 0.0254, 3)

        meter_result.config(text=f"Your height in meters is {meters}")

    except ValueError:

        messagebox.showinfo(title="error", message="Enter valid information")

# Convert Button
meter_calc_button = tk.Button(frame2, text="Calculate", font=("Arial", 14), command=convert_to_meter).grid(row=0, column=6)

root.mainloop()