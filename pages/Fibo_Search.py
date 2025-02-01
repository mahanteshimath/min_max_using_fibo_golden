import streamlit as st
import pandas as pd
import numpy as np
import random
import math

# Fibonacci Search Function
def fibonacci_search(f, a, b, tol=1e-5):
    # Calculate the golden ratio φ
    phi = 1.618

    # Calculate the number of iterations
    n = math.ceil(math.log(5 * (b - a) / tol) / math.log(phi))

    # Generate Fibonacci numbers until the ratio meets the required precision
    fib = [1, 1]
    while len(fib) <= n:
        fib.append(fib[-1] + fib[-2])

    # Initial points
    x1 = a + (fib[n - 2] / fib[n]) * (b - a)
    x2 = a + (fib[n - 1] / fib[n]) * (b - a)
    f1, f2 = f(x1), f(x2)

    iterations = []
    while abs(b - a) > tol:
        iterations.append([a, b, x1, x2, f1, f2])
        if f1 > f2:
            a = x1
            x1, f1 = x2, f2
            x2 = a + (fib[n - 1] / fib[n]) * (b - a)
            f2 = f(x2)
        elif f1 < f2:
            b = x2
            x2, f2 = x1, f1
            x1 = a + (fib[n - 2] / fib[n]) * (b - a)
            f1 = f(x1)
        else:
            a = x1 if random.choice([True, False]) else x2
            n -= 1

    # Final interval adjustment
    if f1 < f2:
        b = x2
    else:
        a = x1

    return iterations

# Function Sanitizer
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
    phi = lambda x: eval(sanitized_input, {"np": np, "x": x})
except Exception as e:
    st.error(f"Error in function definition: {str(e)}\nSanitized input: {sanitized_input}")
    st.stop()

# Run Fibonacci Search
if st.sidebar.button("Run Fibonacci Search"):
    # Check if initial interval already meets the tolerance
    if abs(b - a) <= tolerance:
        st.write("Initial interval already meets the error tolerance.")
    else:
        iterations = fibonacci_search(phi, a, b, tolerance)
        
        st.write("Iterations:")
        df = pd.DataFrame(iterations, columns=["a", "b", "x1", "x2", "ϕ(x1)", "ϕ(x2)"])
        pd.set_option('display.precision', 9)
        st.dataframe(df)
        
        if len(iterations) > 0:
            final_a, final_b = float(iterations[-1][0]), float(iterations[-1][1])
            x_min = (final_a + final_b) / 2
            f_min = phi(x_min)
            
            st.write(f"Total number of iterations: {len(iterations)}")
            st.write(f"Loop break condition: |b - a| ≤ tolerance value : {abs(final_b - final_a):.9f} tolerance :{tolerance:.9f}  is  {abs(final_b - final_a) <= tolerance}")
            st.write(f"Final interval width: {abs(final_b - final_a):.9f}")
            st.write(f"Tolerance value: {tolerance:.9f}")
            st.write(f"Final interval: [{final_a:.9f}, {final_b:.9f}]")
            st.write(f"Function value at minimum: f({x_min:.9f}) = {f_min:.9f}")
        else:
            st.write("No iterations were needed as the initial interval already met the tolerance.")

st.markdown(
    '''
    <style>
    .streamlit-expanderHeader {
        background-color: blue;
        color: white;
    }
    .streamlit-expanderContent {
        background-color: blue;
        color: white;
    }
    </style>
    ''',
    unsafe_allow_html=True
)

footer = """<style>
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
st.markdown(footer, unsafe_allow_html=True)
