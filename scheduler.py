# 🗓️ Exam Scheduler Program using Dictionary

# Dictionary to store exams using exam_id as the key
exams = {
    "MCGE003": {
        "name": "Readings in Philippine History",
        "date": "2025-07-18",
        "time": "8:00 AM",
        "room": "ACB 27"
    },
    "IT143": {
        "name": "Discrete Mathematics",
        "date": "2025-07-19",
        "time": "11:00 AM",
        "room": "GS 22"
    },
    "IT123": {
        "name": "Introduction to Human Computer Interaction",
        "date": "2025-07-20",
        "time": "2:00 PM",
        "room": "IT Building"
    }
}

# Function to add a new exam
def add_exam():
    exam_id = input("Enter unique exam ID: ")
    if exam_id in exams:
        print("❌ Exam ID already exists. Try again.")
        return
    name = input("Enter exam name: ")
    date = input("Enter exam date (YYYY-MM-DD): ")
    time = input("Enter exam time (e.g. 10:00 AM): ")
    room = input("Enter exam room: ")

    exams[exam_id] = {
        "name": name,
        "date": date,
        "time": time,
        "room": room
    }
    print("✅ Exam added successfully!\n")

# Function to view all exams
def view_exams():
    if not exams:
        print("No exams scheduled yet.\n")
        return
    
    print("\n--- 📚 All Scheduled Exams ---")
    for exam_id, details in exams.items():
        print(f"ID: {exam_id}")
        print(f"  Name : {details['name']}")
        print(f"  Date : {details['date']}")
        print(f"  Time : {details['time']}")
        print(f"  Room : {details['room']}\n")

# Function to edit an exam
def edit_exam():
    exam_id = input("Enter the exam ID to edit: ")
    if exam_id not in exams:
        print("❌ Exam ID not found.\n")
        return

    print("Leave a field empty to keep it unchanged.")
    name = input("Enter new exam name: ")
    date = input("Enter new exam date (YYYY-MM-DD): ")
    time = input("Enter new exam time: ")
    room = input("Enter new exam room: ")

    if name:
        exams[exam_id]["name"] = name
    if date:
        exams[exam_id]["date"] = date
    if time:
        exams[exam_id]["time"] = time
    if room:
        exams[exam_id]["room"] = room

    print("✅ Exam updated successfully!\n")

# Function to delete an exam
def delete_exam():
    exam_id = input("Enter the exam ID to delete: ")
    if exam_id in exams:
        del exams[exam_id]
        print("🗑️ Exam deleted successfully.\n")
    else:
        print("❌ Exam ID not found.\n")

# Main menu
def main_menu():
    while True:
        print("===== 🖥️ Exam Scheduler Menu =====")
        print("1. Add a new exam")
        print("2. View all exams")
        print("3. Edit an exam")
        print("4. Delete an exam")
        print("5. Exit")
        choice = input("Select an option (1-5): ")

        if choice == '1':
            add_exam()
        elif choice == '2':
            view_exams()
        elif choice == '3':
            edit_exam()
        elif choice == '4':
            delete_exam()
        elif choice == '5':
            print("Exiting... Goodbye!")
            break
        else:
            print("⚠️ Invalid option. Please try again.\n")

# Run the program
main_menu()
