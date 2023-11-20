import tkinter as tk

class StudentMarksheet(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # Create labels
        label_title = tk.Label(self, text="Student Marksheet")
        label_name = tk.Label(self, text="Name:")
        label_roll_no = tk.Label(self, text="Roll No.:")
        label_subject = tk.Label(self, text="Subject")
        label_marks = tk.Label(self, text="Marks")

        # Create entry fields
        entry_name = tk.Entry(self)
        entry_roll_no = tk.Entry(self)

        # Create a listbox to display the subjects and marks
        listbox_subjects = tk.Listbox(self)

        # Add buttons to add and remove subjects
        button_add_subject = tk.Button(self, text="Add Subject", command=self.add_subject)
        button_remove_subject = tk.Button(self, text="Remove Subject", command=self.remove_subject)

        # Add buttons to calculate and save the marksheet
        button_calculate = tk.Button(self, text="Calculate", command=self.calculate_marksheet)
        button_save = tk.Button(self, text="Save", command=self.save_marksheet)

        # Grid layout
        label_title.grid(row=0, column=0, columnspan=2)
        label_name.grid(row=1, column=0)
        entry_name.grid(row=1, column=1)
        label_roll_no.grid(row=2, column=0)
        entry_roll_no.grid(row=2, column=1)
        label_subject.grid(row=3, column=0)
        label_marks.grid(row=3, column=1)
        listbox_subjects.grid(row=4, column=0, columnspan=2)
        button_add_subject.grid(row=5, column=0)
        button_remove_subject.grid(row=5, column=1)
        button_calculate.grid(row=6, column=0)
        button_save.grid(row=6, column=1)

    def add_subject(self):
        # Get the subject name and marks from the user
        subject_name = tk.simpledialog.askstring("Add Subject", "Enter the subject name:")
        marks = tk.simpledialog.askinteger("Add Subject", "Enter the marks:")

        # Add the subject and marks to the listbox
        self.listbox_subjects.insert(tk.END, (subject_name, marks))

    def remove_subject(self):
        # Get the selected item from the listbox
        selected_item = self.listbox_subjects.get(tk.ANCHOR)

        # Remove the selected item from the listbox
        self.listbox_subjects.delete(tk.ANCHOR)

    def calculate_marksheet(self):
        # Get the total marks and percentage
        total_marks = 0
        for subject in self.listbox_subjects.get(0, tk.END):
            total_marks += subject[1]

        percentage = total_marks / (len(self.listbox_subjects.get(0, tk.END)) * 100) * 100

        # Display the total marks and percentage
        tk.messagebox.showinfo("Marksheet", "Total Marks: " + str(total_marks) + "\nPercentage: " + str(percentage))

    def save_marksheet(self):
        # Get the student name, roll no, subject names, and marks
        student_name = self.entry_name.get()
        roll_no = self.entry_roll_no.get()
        subject_names = []
        marks = []
        for subject in self.listbox_subjects.get(0, tk.END):
            subject_names.append(subject[0])
            marks.append(subject[1])

        # Create a file to save the marksheet
        with open("marksheet.csv", "w") as f