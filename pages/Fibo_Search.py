import streamlit as st
import pandas as pd
import numpy as np

# Fibonacci Search Function
def fibonacci_search(f, a, b, tol):
    # Generate Fibonacci numbers
    fib = [1, 1]
    while fib[-1] < (b - a) / tol:
        fib.append(fib[-1] + fib[-2])
    
    n = len(fib) - 1  # Number of iterations
    x1 = a + (fib[n-2] / fib[n]) * (b - a)
    x2 = a + (fib[n-1] / fib[n]) * (b - a)
    f1, f2 = f(x1), f(x2)

    # Collect data for the table
    iterations = []
    for i in range(n):
        iterations.append([a, b, x1, x2, f1, f2])
        if abs(b - a) <= tol:
            break
        if f1 > f2:
            a = x1
            x1, f1 = x2, f2
            x2 = a + (fib[n-i-1] / fib[n-i]) * (b - a)
            f2 = f(x2)
        else:
            b = x2
            x2, f2 = x1, f1
            x1 = a + (fib[n-i-2] / fib[n-i]) * (b - a)
            f1 = f(x1)
    return iterations

# Streamlit UI
st.title("Fibonacci Search Method")
st.write("This app finds the minimum of a unimodal function using the Fibonacci Search method.")

# Sidebar Inputs
st.sidebar.header("Input Parameters")
function_input = st.sidebar.text_input("Enter the function (use 'x' as the variable):", "(x-2)**2")
a = st.sidebar.number_input("Enter the lower bound (a):", value=1.0, step=0.01)
b = st.sidebar.number_input("Enter the upper bound (b):", value=3.0, step=0.01)
tolerance = st.sidebar.number_input("Enter the tolerance for the minimum point:", value=0.42, step=0.01)

# Define the function
try:
    f = lambda x: eval(function_input, {"x": x, "np": np})
except Exception as e:
    st.error(f"Error in function definition: {e}")
    st.stop()

# Run Fibonacci Search
if st.sidebar.button("Run Fibonacci Search"):
    iterations = fibonacci_search(f, a, b, tolerance)
    if len(iterations) > 0:
        # Prepare DataFrame for display
        df = pd.DataFrame(iterations, columns=["a", "b", "x1", "x2", "ϕ(x1)", "ϕ(x2)"])
        df = df.applymap(lambda x: round(x, 9))  # Round to 9 decimals
        st.write("### Iterations:")
        st.dataframe(df)
        
        final_a, final_b = iterations[-1][0], iterations[-1][1]
        final_x1 = iterations[-1][2]
        st.write(f"Total number of iterations: {len(iterations)}")
        st.write(f"Final Interval: [{final_a:.9f}, {final_b:.9f}]")
        st.write(f"Estimated Minimum Point: {final_x1:.9f}")
        st.write(f"Function Value at Minimum: {f(final_x1):.9f}")
    else:
        st.write("Initial interval already satisfies the tolerance.")
