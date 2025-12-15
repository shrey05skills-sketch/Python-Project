from tkinter import *
from tkinter import messagebox
from datetime import datetime

# --- FUNCTIONS ---

def day_of_week_calculator():
    def calculate():
        try:
            d, m, y = map(int, entry.get().split('-'))
            date_obj = datetime(y, m, d)
            days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
            result = "That date is a " + days[date_obj.weekday()]
            messagebox.showinfo("Result", result)
        except:
            messagebox.showerror("Error", "Enter date in DD-MM-YYYY format")

    win = Toplevel(root)
    win.title("Day of the Week Calculator")
    Label(win, text="Enter a date (DD-MM-YYYY):").pack(pady=5)
    entry = Entry(win)
    entry.pack(pady=5)
    Button(win, text="Calculate", command=calculate).pack(pady=10)


def age_calculator():
    def calculate():
        try:
            d, m, y = map(int, entry.get().split('-'))
            birth_date = datetime(y, m, d)
            today = datetime.now()

            years = today.year - birth_date.year
            months = today.month - birth_date.month
            days = today.day - birth_date.day

            if days < 0:
                months -= 1
                prev_month = today.month - 1 or 12
                days_in_prev_month = [31, 29 if today.year % 4 == 0 else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
                days += days_in_prev_month[prev_month - 1]

            if months < 0:
                years -= 1
                months += 12

            result = f"You are {years} years, {months} months, and {days} days old."
            messagebox.showinfo("Result", result)
        except:
            messagebox.showerror("Error", "Enter date in DD-MM-YYYY format")

    win = Toplevel(root)
    win.title("Age Calculator")
    Label(win, text="Enter your date of birth (DD-MM-YYYY):").pack(pady=5)
    entry = Entry(win)
    entry.pack(pady=5)
    Button(win, text="Calculate", command=calculate).pack(pady=10)


def countdown_to_event():
    def calculate():
        try:
            d, m, y = map(int, entry.get().split('-'))
            event_date = datetime(y, m, d)
            now = datetime.now()

            if event_date <= now:
                messagebox.showinfo("Result", "That date has already passed!")
                return

            diff = event_date - now
            days_left = diff.days

            sec = diff.seconds
            h_left = sec // 3600
            m_left = (sec % 3600) // 60
            s_left = sec % 60

            result = f"Event is in {days_left} days, {h_left} hours, {m_left} minutes, {s_left} seconds."
            messagebox.showinfo("Result", result)
        except:
            messagebox.showerror("Error", "Enter date in DD-MM-YYYY format")

    win = Toplevel(root)
    win.title("Countdown to Event")
    Label(win, text="Enter future event date (DD-MM-YYYY):").pack(pady=5)
    entry = Entry(win)
    entry.pack(pady=5)
    Button(win, text="Calculate", command=calculate).pack(pady=10)


# --- MAIN GUI WINDOW ---

root = Tk()
root.title("Date & Time Applications")
root.geometry("350x300")

Label(root, text="DATE & TIME APPLICATIONS", font=("Arial", 14)).pack(pady=15)

Button(root, text="Day of the Week Calculator", width=25, command=day_of_week_calculator).pack(pady=5)
Button(root, text="Age Calculator", width=25, command=age_calculator).pack(pady=5)
Button(root, text="Countdown to Future Event", width=25, command=countdown_to_event).pack(pady=5)
Button(root, text="Exit", width=25, command=root.destroy).pack(pady=20)

root.mainloop()