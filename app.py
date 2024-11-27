# Streamlit Simple Calculator App

import streamlit as st

def main():
    st.title("Simple Calculator")
    st.write("Select the operation and input numbers to perform calculations.")

    # Define operations
    operations = ["Addition", "Subtraction", "Multiplication", "Division"]
    operation = st.selectbox("Choose an operation:", operations)

    # Get user inputs
    num1 = st.number_input("Enter the first number:", value=0.0)
    num2 = st.number_input("Enter the second number:", value=0.0)

    # Perform calculation when the button is clicked
    if st.button("Calculate"):
        try:
            if operation == "Addition":
                result = num1 + num2
            elif operation == "Subtraction":
                result = num1 - num2
            elif operation == "Multiplication":
                result = num1 * num2
            elif operation == "Division":
                if num2 != 0:
                    result = num1 / num2
                else:
                    st.error("Error! Division by zero is not allowed.")
                    return
            # Display the result
            st.success(f"The result of {operation} is: {result}")
        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
