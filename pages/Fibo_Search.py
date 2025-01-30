import streamlit as st
import pandas as pd
import numpy as np

def fibonacci_search(phi, a, b, tolerance):
    def fib(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fib(n-1) + fib(n-2)
    
    # Find required Fibonacci number
    n = 0
    while fib(n) < (b - a)/tolerance:
        n += 1
    
    iterations = []
    k = n
    
    while k > 1:
        ratio = round(fib(k-2)/fib(k-1), 9)
        x1 = round(a + ratio * (b - a), 9)
        x2 = round(a + (1 - ratio) * (b - a), 9)
        
        phi_x1 = round(phi(x1), 9)
        phi_x2 = round(phi(x2), 9)
        
        iterations.append([round(a, 9), round(b, 9), x1, x2, phi_x1, phi_x2, k])
        
        if phi_x1 <= phi_x2:
            b = x2
        else:
            a = x1
            
        k -= 1
    
    return iterations

st.title("Fibonacci Search Method")
st.write("This app finds the minimum of a unimodal function using the Fibonacci Search method.")

# User Inputs with Guide
st.sidebar.header("Input Parameters")
st.sidebar.markdown("""
**Function Input Guide:**
- Use Python math syntax
- Use `**` for powers
- Use `-` (hyphen) for minus
- Use `np.exp()` for exponential
- Example: `3*x**2 - np.exp(x)` for 3x² - eˣ
""")
function_input = st.sidebar.text_input("Enter the function (use 'x' as the variable):", "(x - 2)**2")
a = st.sidebar.number_input("Enter the lower bound (a):", value=1.0)
b = st.sidebar.number_input("Enter the upper bound (b):", value=3.0)
tolerance = st.sidebar.number_input("Enter the error tolerance:", value=0.42)

# Function definition with numpy support
try:
    phi = lambda x: eval(function_input, {"np": np, "x": x})
except Exception as e:
    st.error(f"Error in function definition: {e}")
    st.stop()

if st.sidebar.button("Run Fibonacci Search"):
    iterations = fibonacci_search(phi, a, b, tolerance)
    
    st.write("Iterations:")
    df = pd.DataFrame(iterations, columns=["a", "b", "x1", "x2", "ϕ(x1)", "ϕ(x2)", "k"])
    pd.set_option('display.float_format', lambda x: '%.9f' % x)
    st.dataframe(df)
    
    if len(iterations) > 0:
        final_a, final_b = iterations[-1][0], iterations[-1][1]
        final_x2 = iterations[-1][3]
        x_min = round((final_a + final_x2)/2, 9)
        f_min = round(phi(x_min), 9)
        
        st.write(f"Total number of iterations: {len(iterations)}")
        st.write(f"Final Fibonacci number k: {iterations[-1][6]}")
        st.write(f"Loop break condition: |b - a| ≤ tolerance value : {abs(final_b - final_a):.9f}")
        st.write(f"Final interval width: {abs(final_b - final_a):.9f}")
        st.write(f"Tolerance value: {tolerance}")
        st.write(f"Final interval: [{final_a:.9f}, {final_x2:.9f}]")
        st.write(f"Function value at minimum: f({x_min:.9f}) = {f_min:.9f}")
    else:
        st.write("Initial interval already meets the error tolerance.")
