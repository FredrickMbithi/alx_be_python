from datetime import datetime, timedelta

def display_current_datetime():
    currentdate = datetime.now()
    print(f"Current DateTime: {currentdate}")
    return currentdate
# display_current_datetime()

def calculate_future_date():
    days_to_add = int(input("Input a number of days (as an integer): "))
    current_date = datetime.now()
    future = current_date + timedelta(days=days_to_add)
    print(f"The future date is {future}")
    
display_current_datetime()
calculate_future_date()