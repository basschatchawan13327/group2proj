import json
import os

DATA_FILE = "student_life.json"

student_sessions = []
assignments = []
expenses = []
habits = []

main_choice = ""
s_choice = ""

date = ""
subject = ""
duration = ""

def load_data():
    global student_sessions, assignments, expenses, habits
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
    
        student_sessions = data.get("student_sessions",[])
        assignments = data.get("assignments",[])
        expenses = data.get("expenses",[])
        habits = data.get("habits",[])
    else:
        student_sessions = []
        assignments = []
        expenses = []
        habits = []
    return student_sessions, assignments, expenses, habits

def save_data(student_sessions, assignments, expenses, habits):
    data = {
        "student_sessions": student_sessions,
        "assignments": assignments,
        "expenses": expenses,
        "habits": habits
    }
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, ensure_ascii=False, indent = 4)

def get_input(field):
    return input(f"Enter: {field}")

while True :
    print("===Student Life Tracker===\n1. Study\n2. Assignments\3. Expenses\n4. Habits\n5. Weekly Summary\n0. Exit\n")
    main_choice = get_input(main_choice)
    
    if main_choice == "0":
        print("Good bye")
        break
    elif main_choice == "1":
        print("1.Add\n2.List\n3.Delete\n")
        s_choice = get_input(s_choice)
        if s_choice == "1":
            date = get_input(date)
            subject = get_input(subject)
            duration = get_input(duration)
            student_sessions.append({ "date": date,"subject": subject,"duration": duration})
            with open(DATA_FILE, "w", encoding="utf-8") as f:
                json.dump(student_sessions, f, ensure_ascii=False, indent=4)
        elif s_choice == "2":
            load_data()
            print("Date: ", student_sessions[date])
            print("Subject: ", student_sessions[subject])
            print("Duration: ", student_sessions[duration])
