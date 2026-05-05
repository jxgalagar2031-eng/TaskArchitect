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
