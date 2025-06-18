import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        feet = float(feet_entry.get())
        inches = float(inch_entry.get())
        age = int(age_entry.get())

        if weight <= 0 or feet < 0 or inches < 0 or age <= 0:
            raise ValueError

        # Convert height to meters
        total_inches = (feet * 12) + inches
        height_m = total_inches * 0.0254

        # Calculate BMI
        bmi = weight / (height_m ** 2)
        bmi = round(bmi, 2)

        # Age-based classification
        if age < 18:
            category = (
                f"Your BMI is {bmi}, but you're under 18.\n"
                "BMI charts for children and teens are different.\n"
                "Please consult a doctor for age-appropriate evaluation."
            )
        else:
            if bmi < 18.5:
                category = f"Your BMI is {bmi}\nCategory: Underweight 😕"
            elif 18.5 <= bmi < 25:
                category = f"Your BMI is {bmi}\nCategory: Normal weight 🙂"
            elif 25 <= bmi < 30:
                category = f"Your BMI is {bmi}\nCategory: Overweight 😐"
            else:
                category = f"Your BMI is {bmi}\nCategory: Obese 😟"

        result_label.config(text=f"Age: {age} years\n{category}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers in all fields.")

# GUI
app = tk.Tk()
app.title("BMI Calculator")
app.geometry("340x370")
app.resizable(False, False)

tk.Label(app, text="Enter your details", font=("Arial", 14)).pack(pady=10)

# Weight
tk.Label(app, text="Weight (kg):").pack()
weight_entry = tk.Entry(app)
weight_entry.pack()

# Age
tk.Label(app, text="Age (years):").pack()
age_entry = tk.Entry(app)
age_entry.pack()

# Height
tk.Label(app, text="Height:").pack()
frame = tk.Frame(app)
frame.pack(pady=5)

tk.Label(frame, text="Feet:").grid(row=0, column=0, padx=5)
feet_entry = tk.Entry(frame, width=5)
feet_entry.grid(row=0, column=1)

tk.Label(frame, text="Inches:").grid(row=0, column=2, padx=5)
inch_entry = tk.Entry(frame, width=5)
inch_entry.grid(row=0, column=3)

# Button
tk.Button(app, text="Calculate BMI", command=calculate_bmi).pack(pady=15)

# Result
result_label = tk.Label(app, text="", font=("Arial", 11), wraplength=300, justify="center")
result_label.pack()

app.mainloop()
