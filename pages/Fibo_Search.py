import streamlit as st
import pandas as pd
import numpy as np

# Fibonacci Search Function
def fibonacci_search(phi, a, b, tolerance):
    # Generate Fibonacci sequence up to F_n >= (b - a) / tolerance
    fib = [0, 1]
    while fib[-1] < (b - a) / tolerance:
        fib.append(fib[-1] + fib[-2])
    
    n = len(fib) - 1  # Number of iterations
    iterations = []
    
    for k in range(n - 1, 1, -1):
        x1 = a + (fib[k - 2] / fib[k]) * (b - a)
        x2 = a + (fib[k - 1] / fib[k]) * (b - a)
        
        phi_x1 = round(phi(x1), 9)
        phi_x2 = round(phi(x2), 9)
        
        iterations.append([round(a, 9), round(b, 9), x1, x2, phi_x1, phi_x2])
        
        if phi_x1 < phi_x2:
            b = x2  # Narrow interval to [a, x2]
        else:
            a = x1  # Narrow interval to [x1, b]
    
    return iterations

# Streamlit App
st.title("Fibonacci Search Method")
st.write("This app finds the minimum of a unimodal function using the Fibonacci Search method.")

# User Inputs
st.sidebar.header("Input Parameters")
st.sidebar.markdown("""
**Function Input Guide:**
- Use Python math syntax
- Use `**` for powers
- Use `-` (hyphen) for minus
- Use `np.exp()` for exponential
- Example: `3*x**2 - np.exp(x)` for 3x² - eˣ
""")
function_input = st.sidebar.text_input("Enter the function (use 'x' as the variable):", "3*x**2 - np.exp(x)")
a = st.sidebar.number_input("Enter the lower bound (a):", value=1.0)
b = st.sidebar.number_input("Enter the upper bound (b):", value=3.0)
tolerance = st.sidebar.number_input("Enter the error tolerance for the minimum point:", value=0.42)

# Define the function from user input
try:
    phi = lambda x: eval(function_input, {"np": np, "x": x})
except Exception as e:
    st.error(f"Error in function definition: {e}")
    st.stop()

# Run Fibonacci Search
if st.sidebar.button("Run Fibonacci Search"):
    iterations = fibonacci_search(phi, a, b, tolerance)
    
    st.write("Iterations:")
    df = pd.DataFrame(iterations, columns=["a", "b", "x1", "x2", "ϕ(x1)", "ϕ(x2)"])
    pd.set_option('display.float_format', lambda x: '%.9f' % x)
    st.dataframe(df)
    
    if len(iterations) > 0:
        final_a, final_b = iterations[-1][0], iterations[-1][1]
        final_x2 = iterations[-1][3]
        x_min = round((final_a + final_x2) / 2, 9)
        f_min = round(phi(x_min), 9)
        
        st.write(f"Total number of iterations: {len(iterations)}")
        st.write(f"Loop break condition: |b - a| ≤ tolerance value : {abs(final_b - final_a):.9f} tolerance :{tolerance}  is  {abs(final_b - final_a) <= tolerance} ")
        st.write(f"Final interval width: {abs(final_b - final_a):.9f}")
        st.write(f"Tolerance value: {tolerance}")
        st.write(f"Final interval: [{final_a:.9f}, {final_x2:.9f}]")
        st.write(f"Function value at minimum: f({x_min:.9f}) = {f_min:.9f}")
    else:
        st.write("Initial interval already meets the error tolerance.")