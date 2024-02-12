import streamlit as st

def calculator():
    st.title("Simple Calculator")

    # Get user input for two numbers
    num1 = st.number_input("Enter the first number:", value=0.0)
    num2 = st.number_input("Enter the second number:", value=0.0)

    # Select operation
    operation = st.radio("Select operation:", ('Addition', 'Subtraction', 'Multiplication', 'Division'))

    # Perform calculation based on the selected operation
    if operation == 'Addition':
        result = num1 + num2
    elif operation == 'Subtraction':
        result = num1 - num2
    elif operation == 'Multiplication':
        result = num1 * num2
    elif operation == 'Division':
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Cannot divide by zero"

    # Display the result
    st.write(f"Result: {result}")

if __name__ == "__main__":
    calculator()
