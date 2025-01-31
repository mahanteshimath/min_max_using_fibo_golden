import streamlit as st
import pandas as pd
import numpy as np
import random
from sympy import symbols, sympify
import plotly.graph_objects as go

# Correct Fibonacci Search Function with proper loop break logic and precision to 9 decimals
def fibonacci_search(func, a, b, tol=1e-6, max_iter=100):
    """Fibonacci search method implementation"""
    # Generate Fibonacci numbers
    fib = [1, 1]
    while fib[-1] < (b - a) / tol:
        fib.append(fib[-1] + fib[-2])
    n = len(fib) - 1
    iterations = []
    
    # Initial points
    x1 = a + (fib[n-2] / fib[n]) * (b - a)
    x2 = a + (fib[n-1] / fib[n]) * (b - a)
    
    for k in range(n):
        f1 = func(x1)
        f2 = func(x2)
        
        iterations.append({
            'iteration': k + 1,
            'interval': [a, b],
            'x1': x1,
            'x2': x2,
            'f1': f1,
            'f2': f2
        })
        
        if f1 < f2:
            b = x2
            x2 = x1
            x1 = a + (fib[n-k-3] / fib[n-k-1]) * (b - a)
        else:
            a = x1
            x1 = x2
            x2 = a + (fib[n-k-2] / fib[n-k-1]) * (b - a)
            
        if abs(b - a) < tol:
            break
    
    return (a + b) / 2, iterations

def sanitize_function(func_str):
    # Replace unicode minus with regular minus
    func_str = func_str.replace('−', '-')
    # Replace other common mathematical symbols
    func_str = func_str.replace('^', '**')
    # Remove any whitespace
    func_str = func_str.replace(' ', '')
    return func_str

# Streamlit App
st.title("Fibonacci Search Method")
st.write("This app finds the minimum of a unimodal function using the Fibonacci Search method.")

# User Inputs
st.sidebar.header("Input Parameters")
st.sidebar.markdown("""
**Function Input Guide:**
- Use simple Python syntax: (x-2)**2
- Spaces will be automatically removed
- Both regular minus (-) and mathematical minus (−) are supported
- ^ will be converted to **
- Examples:
  * (x-2)**2
  * x**2 + 2*x + 1
  * 3*x**2 - np.exp(x)
""")
function_input = st.sidebar.text_input("Enter the function (use 'x' as the variable):", "(x-2)**2")
a = st.sidebar.number_input("Enter the lower bound (a):", value=1.0, format="%.9f")
b = st.sidebar.number_input("Enter the upper bound (b):", value=3.0, format="%.9f")
tolerance = st.sidebar.number_input("Enter the error tolerance for the minimum point:", value=0.42, format="%.9f")

# Define the function from user input with sanitization
try:
    sanitized_input = sanitize_function(function_input)
    x = symbols('x')
    func_expr = sympify(sanitized_input)
    phi = lambda x_val: float(func_expr.subs(x, x_val))
except Exception as e:
    st.error(f"Error in function definition: {str(e)}\nSanitized input: {sanitized_input}")
    st.stop()

# Run Fibonacci Search
if st.sidebar.button("Run Fibonacci Search"):
    x_min, iterations = fibonacci_search(phi, a, b, tolerance)
    
    st.write(f"Minimum found at x = {x_min:.4f}")
    st.write(f"Minimum value = {phi(x_min):.4f}")
    ##
    x_vals = np.linspace(a, b, 200)
    y_vals = [phi(x_val) for x_val in x_vals]
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x_vals, y=y_vals, name='f(x)'))
    
    # Show iterations
    st.write("### Iteration Details")
    for iter_data in iterations:
        st.write(f"Iteration {iter_data['iteration']}")
        st.write(f"Interval: [{iter_data['interval'][0]:.4f}, {iter_data['interval'][1]:.4f}]")
    
    st.plotly_chart(fig)

st.markdown(
    '''
    <style>
    .streamlit-expanderHeader {
        background-color: blue;
        color: white; # Adjust this for expander header color
    }
    .streamlit-expanderContent {
        background-color: blue;
        color: white; # Expander content color
    }
    </style>
    ''',
    unsafe_allow_html=True
)

footer="""<style>
.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: #2C1E5B;
color: white;
text-align: center;
}
</style>
<div class="footer">
<p>Developed with ❤️ by <a style='display: inline; text-align: center;' href="https://www.linkedin.com/in/mahantesh-hiremath/" target="_blank">MAHANTESH HIREMATH</a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)
