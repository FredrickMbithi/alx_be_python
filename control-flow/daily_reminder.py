task = input("Enter your task:")
priority = input("Priority level (High/medium/low):")
time_bound = input("Is it time bound? (yes/no)")

if priority == "high" and time_bound == "yes":
    print(f"Finish your'{task}' is a{priority} task. Consider completing it when you have free time.")
elif priority == "low" and time_bound == "no":
    print(f"Finish your '{task}' is a {priority} task. Consider completing it when you have free time.")
elif priority == "medium" and time_bound == "no":
    if priority == "medium" and time_bound == "yes":
        print(f"Finish your '{task}' is a {priority} task. Consider completing it when you have free time")
    else:
        print(f"Finish your '{task}' is a {priority} task. Consider completing it when you have free time")
