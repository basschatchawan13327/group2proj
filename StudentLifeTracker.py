import json

DATA_FILE = "student_life.json"

student_sessions = []
assignments = []
expenses = []
habits = []

def load_data():
    global student_sessions,assignments,expenses,habits
    with open(DATA_FILE, "r") as f:
        data = json.load(f)

        student_sessions = data.get("student_sessions",[])
        assignments = data.get("assignments",[])
        expenses = data.get("expenses",[])
        habits = data.get("habits",[])

while True :
    print("===Student Life Tracker===")
    print("1. Study")
    print("2. Assignments")
    print("3. Expenses")
    print("4. Habits")
    print("5. Weekly Summary")
    print("0. Exit")
    choice = input("Select ")
    
    if choice == "0":
        print("Good bye")
        break