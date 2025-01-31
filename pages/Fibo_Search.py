import streamlit as st
import pandas as pd
import numpy as np
import random

# Validate if the function is unimodal
def validate_unimodal(f, a, b, samples=100):
    """Check if function appears to be unimodal in interval [a,b]"""
    x = np.linspace(a, b, samples)
    y = [f(xi) for xi in x]
    peaks = len([i for i in range(1, len(y)-1) if y[i-1] > y[i] < y[i+1]])
    valleys = len([i for i in range(1, len(y)-1) if y[i-1] < y[i] > y[i+1]])
    return peaks + valleys <= 1

# Correct Fibonacci Search Function with proper loop break logic and precision to 9 decimals
def fibonacci_search(f, a, b, tol=1e-5):
    # Validate input function
    if not validate_unimodal(f, a, b):
        raise ValueError("Function does not appear to be unimodal in the given interval")

    # Convert input parameters to float with 9 decimal precision
    a = float(format(float(a), '.9f'))
    b = float(format(float(b), '.9f'))
    tol = float(format(float(tol), '.9f'))

    # Generate Fibonacci numbers until the ratio meets the required precision
    fib = [1.00000000, 1.000000000]
    while fib[-1] < float(format((b - a) / tol, '.9f')):
        fib.append(float(format(fib[-1] + fib[-2], '.9f')))

    n = len(fib) - 1  # Number of iterations required

    # Initial points with explicit float conversion and 9 decimal precision
    x1 = float(format(a + (fib[n - 2] / fib[n]) * (b - a), '.9f'))
    x2 = float(format(a + (fib[n - 1] / fib[n]) * (b - a), '.9f'))

    f1 = float(format(f(x1), '.9f'))
    f2 = float(format(f(x2), '.9f'))

    iterations = []

    # Corrected while loop condition
    while fib[n] < (b - a) / tol:
        iterations.append([f"{a:.9f}", f"{b:.9f}", f"{x1:.9f}", f"{x2:.9f}", f"{f1:.9f}", f"{f2:.9f}"])
        
        if abs(f1 - f2) < 1e-9:  # Handle equal function values more precisely
            # Move both points inward by golden ratio
            golden = 0.618034
            a = x1 * (1 - golden) + x2 * golden
            b = x1 * golden + x2 * (1 - golden)
            x1 = a + (fib[n - 2] / fib[n]) * (b - a)
            x2 = a + (fib[n - 1] / fib[n]) * (b - a)
        elif f1 > f2:
            a = x1
            x1, f1 = x2, f2
            x2 = round(a + (fib[n - 1] / fib[n]) * (b - a), 9)
            f2 = round(f(x2), 9)
        else:  # f1 < f2
            b = x2
            x2, f2 = x1, f1
            x1 = round(a + (fib[n - 2] / fib[n]) * (b - a), 9)
            f1 = round(f(x1), 9)
        n -= 1

    # Final comparison to minimize interval.
    if f1 < f2:
        b = x2
    else:
        a = x1

    return iterations

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
    iterations = fibonacci_search(phi, a, b, tolerance)
    
    st.write("Iterations:")
    df = pd.DataFrame(iterations, columns=["a", "b", "x1", "x2", "ϕ(x1)", "ϕ(x2)"])
    pd.set_option('display.precision', 9)
    st.dataframe(df)
    
    if len(iterations) > 0:
        final_a, final_b = float(iterations[-1][0]), float(iterations[-1][1])
        final_x2 = float(iterations[-1][3])
        x_min = round((final_a + final_x2)/2, 9)
        f_min = round(phi(x_min), 9)
        
        st.write(f"Total number of iterations: {len(iterations)}")
        st.write(f"Loop break condition: |b - a| ≤ tolerance value : {abs(final_b - final_a):.9f} tolerance :{tolerance:.9f}  is  {abs(final_b - final_a) <= tolerance} ")
        st.write(f"Final interval width: {abs(final_b - final_a):.9f}")
        st.write(f"Tolerance value: {tolerance:.9f}")
        st.write(f"Final interval: [{final_a:.9f}, {final_x2:.9f}]")
        st.write(f"Function value at minimum: f({x_min:.9f}) = {f_min:.9f}")
    else:
        st.write("Initial interval already meets the error tolerance.")

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