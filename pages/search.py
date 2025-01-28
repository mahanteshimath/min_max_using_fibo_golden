import streamlit as st
import numpy as np

# Define the Fibonacci Search function
def fibonacci_search(func, a, b, error_tolerance):
    # Generate the Fibonacci sequence until it satisfies the error condition
    fib = [1, 1]
    while (b - a) / fib[-1] > error_tolerance:
        fib.append(fib[-1] + fib[-2])
    
    n = len(fib) - 1  # Number of iterations
    fib_n, fib_n1 = fib[n], fib[n-1]
    
    # Initial two test points
    x1 = a + (fib[n-2] / fib[n]) * (b - a)
    x2 = a + (fib[n-1] / fib[n]) * (b - a)
    f1, f2 = func(x1), func(x2)
    
    # Table to store steps
    steps = []
    steps.append([1, a, b, x1, x2, f1, f2])
    
    # Perform the Fibonacci search iterations
    for step in range(2, n - 1):
        if f1 > f2:
            a = x1
            x1, f1 = x2, f2
            x2 = a + (fib_n1 / fib_n) * (b - a)
            f2 = func(x2)
        else:
            b = x2
            x2, f2 = x1, f1
            x1 = a + (fib[n-2] / fib[n]) * (b - a)
            f1 = func(x1)
        
        # Update Fibonacci numbers
        fib_n, fib_n1 = fib_n1, fib_n - fib_n1
        
        # Append the current step
        steps.append([step, a, b, x1, x2, f1, f2])
    
    # The final interval and minimum approximation
    x_min = (a + b) / 2
    f_min = func(x_min)
    
    return x_min, f_min, steps

# Streamlit App
st.title("Fibonacci Search Method")

# User Input
st.sidebar.header("Input Parameters")
func_input = st.sidebar.text_input("Function (use 'x' as the variable):", "(x - 2)**2")
a = st.sidebar.number_input("Start of Interval (a):", value=1.0)
b = st.sidebar.number_input("End of Interval (b):", value=3.0)
error_tolerance = st.sidebar.number_input("Error Tolerance:", value=0.42)

if st.sidebar.button("Find Minimum"):
    try:
        # Parse the function
        func = lambda x: eval(func_input)
        
        # Perform Fibonacci Search
        x_min, f_min, steps = fibonacci_search(func, a, b, error_tolerance)
        
        # Display Results
        st.subheader("Results")
        st.write(f"Minimum approximately at: **x = {x_min:.4f}**")
        st.write(f"Function value at minimum: **f(x) = {f_min:.4f}**")
        
        # Display Steps in a Table
        st.subheader("Steps")
        st.table(
            {
                "Step": [step[0] for step in steps],
                "a": [step[1] for step in steps],
                "b": [step[2] for step in steps],
                "x1": [step[3] for step in steps],
                "x2": [step[4] for step in steps],
                "ϕ(x1)": [step[5] for step in steps],
                "ϕ(x2)": [step[6] for step in steps],
            }
        )
    except Exception as e:
        st.error(f"Error in processing the function: {e}")
