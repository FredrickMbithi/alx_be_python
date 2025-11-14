task = input("Enter your task:")
priority = input("Priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes/no):")

# Modify reminder based on time sensitivity using an if statement
if time_bound == "yes":
    urgency = "Immediate action required."
else:
    urgency = "No immediate action required."

# Provide a customized reminder using match-case on priority
match priority:
    case "high":
        print(f"Reminder: '{task}' is a high priority task. {urgency}")
    case "medium":
        print(f"Reminder: '{task}' is a medium priority task. {urgency}")
    case "low":
        print(f"Reminder: '{task}' is a low priority task. {urgency}")
    case _:
        print(f"Reminder: '{task}' has priority '{priority}'. {urgency}")
