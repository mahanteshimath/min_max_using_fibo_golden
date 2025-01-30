import streamlit as st
import pandas as pd
import numpy as np

# Corrected Golden Section Search Function
def golden_section_search(phi, a, b, tolerance):
    rho = (np.sqrt(5) - 1) / 2  # Golden ratio (~0.618)
    iterations = []
    
    while abs(b - a) > tolerance:
        x1 = round(a + (1 - rho) * (b - a), 5)
        x2 = round(a + rho * (b - a), 5)
        
        phi_x1 = round(phi(x1), 5)
        phi_x2 = round(phi(x2), 5)
        
        iterations.append([round(a, 5), round(b, 5), x1, x2, phi_x1, phi_x2])
        
        if phi_x1 <= phi_x2:  # Changed to <= to handle equality case
            b = x2  # Choose left interval when equal
        else:
            a = x1  # Choose right interval
    
    return iterations

# Streamlit App
st.title("Golden Section Search Method")
st.write("This app finds the minimum of a unimodal function using the Golden Section Search method.")

# User Inputs
st.sidebar.header("Input Parameters")
function_input = st.sidebar.text_input("Enter the function (use 'x' as the variable):", "(x - 2)**2")
a = st.sidebar.number_input("Enter the lower bound (a):", value=1.0)
b = st.sidebar.number_input("Enter the upper bound (b):", value=3.0)
tolerance = st.sidebar.number_input("Enter the error tolerance for the minimum point:", value=0.42)

# Define the function from user input
try:
    phi = lambda x: eval(function_input)
except Exception as e:
    st.error(f"Error in function definition: {e}")
    st.stop()

# Run Golden Section Search
if st.sidebar.button("Run Golden Section Search"):
    iterations = golden_section_search(phi, a, b, tolerance)
    
    st.write("Iterations:")
    df = pd.DataFrame(iterations, columns=["a", "b", "x1", "x2", "ϕ(x1)", "ϕ(x2)"])
    pd.set_option('display.float_format', lambda x: '%.5f' % x)
    st.dataframe(df)
    
    if len(iterations) > 0:
        final_a, final_b = iterations[-1][0], iterations[-1][1]
        x_min = round((final_a + final_b)/2, 5)
        f_min = round(phi(x_min), 5)
        
        st.write(f"Total number of iterations: {len(iterations)}")
        st.write(f"Loop break condition: |b - a| ≤ tolerance")
        st.write(f"Final interval width: {abs(final_b - final_a):.5f}")
        st.write(f"Tolerance value: {tolerance}")
        st.write(f"Final interval: [{final_a:.5f}, {final_b:.5f}]")
        st.write(f"Function value at minimum: f({x_min:.5f}) = {f_min:.5f}")
    else:
        st.write("Initial interval already meets the error tolerance.")