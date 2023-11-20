import tkinter as tk

class AgeCalculator(tk.Frame):
    def __init__(self, master):
        super().__init__(master) 

        # Create labels
        label_title = tk.Label(self, text="Age Calculator") 
        label_given_day = tk.Label(self, text="Given Day:") 
        label_given_month = tk.Label(self, text="Given Month:") 
        label_given_year = tk.Label(self, text="Given Year:") 
        label_result_age = tk.Label(self, text="Result Age:") 
        label_years = tk.Label(self, text="Years:") 
        label_months = tk.Label(self, text="Months:") 
        label_days = tk.Label(self, text="Days:") 

        # Create entry fields
        entry_given_day = tk.Entry(self)
        entry_given_month = tk.Entry(self)
        entry_given_year = tk.Entry(self)
        entry_result_age_years = tk.Entry(self, state="readonly")
        entry_result_age_months = tk.Entry(self, state="readonly")
        entry_result_age_days = tk.Entry(self, state="readonly")

        # Create buttons
        button_calculate = tk.Button(self, text="Calculate", command=self.calculate_age)
        button_clear = tk.Button(self, text="Clear", command=self.clear_fields)

        # Grid layout
        label_title.grid(row=0, column=0, columnspan=2)
        label_given_day.grid(row=1, column=0)
        entry_given_day.grid(row=1, column=1)
        label_given_month.grid(row=2, column=0)
        entry_given_month.grid(row=2, column=1)
        label_given_year.grid(row=3, column=0)
        entry_given_year.grid(row=3, column=1)
        label_result_age.grid(row=4, column=0)
        entry_result_age_years.grid(row=4, column=1)
        label_years.grid(row=5, column=0)
        entry_result_age_months.grid(row=5, column=1)
        label_months.grid(row=6, column=0)
        entry_result_age_days.grid(row=6, column=1)
        button_calculate.grid(row=7, column=0)
        button_clear.grid(row=7, column=1)

    def calculate_age(self):
        # Get the given day, month, and year
        given_day = int(self.entry_given_day.get())
        given_month = int(self.entry_given_month.get())
        given_year = int(self.entry_given_year.get())

        # Calculate the current date
        current_date = datetime.date.today()

        # Calculate the age in years, months, and days
        age_in_years = current_date.year - given_year
        age_in_months = current_date.month - given_month
        age_in_days = current_date.day - given_day

        # Set the result age fields
        self.entry_result_age_years.config(state="normal")
        self.entry_result_age_months.config(state="normal")
        self.entry_result_age_days.config(state="normal")
        self.entry_result_age_years.delete(0, "end")
        self.entry_result_age_months.delete(0, "end")
        self.entry_result_age_days.delete(0, "end")
        self.entry_result_age_years.insert(0, str(age_in_years))
        self.entry_result_age_months.insert(0, str(age_in_months))
        self.entry_result_age_days.insert(0, str(age_in_days))