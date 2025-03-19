import streamlit as st
import math

# Custom CSS for styling
st.markdown(
    """
    <style>
    body {
        background-color: #000000;  /* Black background for the entire page */
        color: #FFFFFF;  /* White text color for readability */
        font-family: Arial, sans-serif;
    }
    .stApp {
        background-color: #222222;  /* Dark gray background for the container */
        padding: 20px;
        border-radius: 8px;  /* Rounded corners for the container */
    }
    h1, h2, h3, h4, h5, h6, p {
        background: linear-gradient(to right, 
            #FF0000, #FF7F00, #FFFF00, #00FF00, 
            #00FFFF, #0000FF, #8A2BE2);  /* Gradient with 7 colors */
        -webkit-background-clip: text;
        color: transparent;
    }
    .stButton {
        background-color: #1E90FF;  /* Button color */
        color: white;  /* Button text color */
    }
    .stButton:hover {
        background-color: #00BFFF;  /* Button hover color */
    }
    .stSelectbox, .stNumberInput {
        background-color: #333333;  /* Input field background */
        color: #FFFFFF;  /* Input field text color */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Simple Calculator Code
def simple_calculator():
    # Apply gradient effect to the title
    st.markdown(
        """
        <h1 style="background: linear-gradient(to right, 
            #FF0000, #FF7F00, #FFFF00, #00FF00, 
            #00FFFF, #0000FF, #8A2BE2);
        -webkit-background-clip: text;
        color: transparent;">Simple Calculator</h1>
        """,
        unsafe_allow_html=True
    )
    st.write("This is a simple calculator that performs basic arithmetic operations.")  # Description

    # Input fields for numbers in columns
    col1, col2 = st.columns(2)
    with col1:
        num1 = st.number_input("Enter first number", value=0.0, step=0.1)
    with col2:
        num2 = st.number_input("Enter second number", value=0.0, step=0.1)

    # Operation selection
    operation = st.selectbox(
        "Choose operation",
        ["Addition (+)", "Subtraction (-)", "Multiplication (×)", "Division (÷)"],
    )

    # Calculate result for simple operations
    if st.button("Calculate"):
        try:
            if operation == "Addition (+)":
                result = num1 + num2
                symbol = "+"
            elif operation == "Subtraction (-)":
                result = num1 - num2
                symbol = "-"
            elif operation == "Multiplication (×)":
                result = num1 * num2
                symbol = "×"
            elif operation == "Division (÷)":
                if num2 == 0:
                    st.error("Error: Division by zero!")
                    return
                result = num1 / num2
                symbol = "÷"
            st.success(f"**Result:** {num1} {symbol} {num2} = {result}")  # Highlight result
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

# Main function to run both calculators side by side
def main():
    col1, col2 = st.columns([1, 0.05])  # Adjust width of columns for space between
    with col1:
        simple_calculator()  # Run simple calculator
    with col2:
        st.markdown('<div style="border-left: 3px solid blue; height: 100%;"></div>', unsafe_allow_html=True)  # Divider line

if __name__ == "__main__":
    main()
