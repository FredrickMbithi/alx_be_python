def perform_operation(num1, num2, operation):

    if operation == "add":
        return num1 + num2

    elif operation == "subtract":
        return num1 - num2

    elif operation == "multiply":
        return num1 * num2

    elif operation == "divide":
        # Handle division by zero
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2

    else:
        # Unknown operation
        return "Error: Invalid operation"
result = perform_operation(5, 6, "subtract")
print(result)
