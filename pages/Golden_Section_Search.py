import streamlit as st
import pandas as pd
import numpy as np

# Golden Section Search Function (Updated for phi(x1) = phi(x2))
def golden_section_search(phi, a, b, tolerance):
    rho = (3 - np.sqrt(5)) / 2  # Golden ratio
    iterations = []
    
    while (b - a) > 2 * tolerance:
        x1 = a + (1 - rho) * (b - a)
        x2 = a + rho * (b - a)
        
        phi_x1 = phi(x1)
        phi_x2 = phi(x2)
        
        iterations.append([a, b, x1, x2, phi_x1, phi_x2])
        
        if phi_x1 < phi_x2:
            b = x2  # Minimum is in [a, x2]
        elif phi_x1 > phi_x2:
            a = x1  # Minimum is in [x1, b]
        else:
            # If phi(x1) == phi(x2), evaluate a third point x3
            x3 = (x1 + x2) / 2  # Midpoint of [x1, x2]
            phi_x3 = phi(x3)
            
            if phi_x3 < phi_x1:
                # Minimum is in [x1, x2]
                a, b = x1, x2
            else:
                # Minimum could be in either subinterval; retain [a, x2] or [x1, b]
                if phi(a) < phi(b):
                    b = x2
                else:
                    a = x1
    
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
    
    # Display iterations in a DataFrame
    st.write("Iterations:")
    df = pd.DataFrame(iterations, columns=["a", "b", "x1", "x2", "ϕ(x1)", "ϕ(x2)"])
    st.dataframe(df)
    
    # Display final result
    if len(iterations) > 0:
        final_a, final_b = iterations[-1][0], iterations[-1][1]
        st.write(f"Final interval: [{final_a}, {final_b}]")
        st.write(f"Minimum lies within the interval with an error tolerance of {tolerance}.")
    else:
        st.write("Initial interval already meets the error tolerance.")