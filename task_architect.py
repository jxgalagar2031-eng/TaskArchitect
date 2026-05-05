# Project Title: Task Architect
# Group Members: Eli Dellosa, Xia Galagar, Laurence Cupin
# Description: A Python program to help students manage ADHD and executive dysfunction by prioritizing tasks.


tasks = []  # List to store all task data
total_time = 0  # Counter for total workload in minutes

# Function to convert deadline strings (e.g., '2h') into minutes for sorting
def ConvertToMinutes(value):
    if value.endswith("m"):
        return int(value[:-1])
    elif value.endswith("h"):
        return int(value[:-1]) * 60
    elif value.endswith("d"):
        return int(value[:-1]) * 1440
    else:
        return int(value)


num_tasks = int(input("How many tasks? "))

# Loop to collect task details from the user
for i in range(num_tasks):
    print("\nTask", i + 1)
    name = input("Task name: ")
    deadline_input = input("Deadline (e.g. 30m, 2h, 1d): ")
    difficulty = input("Difficulty (Easy/Medium/Hard): ")
    time = int(input("Estimated time (minutes): "))

    # Use the Pascal Case function to process the deadline
    deadline_mins = ConvertToMinutes(deadline_input)
    tasks.append([name, deadline_mins, difficulty, time])
    total_time += time

# Sort tasks so the nearest deadline is at the top
tasks.sort(key=lambda x: x[1])

# Logic to detect overload and suggest a task to postpone
if total_time > 300:
    print("\nYou are too overloaded!")  # Simple print warning for CR003
    longest_task = max(tasks, key=lambda x: x[3])
    print("Suggestion: Consider postponing ->", longest_task[0])
else:
    print("\nYou are within a manageable workload.")
