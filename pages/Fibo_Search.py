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
    k = n
    iterations = []
    
    while k > 1:
        x1 = a + (fib[k - 2] / fib[k]) * (b - a)
        x2 = a + (fib[k - 1] / fib[k]) * (b - a)
        
        phi_x1 = round(phi(x1), 9)
        phi_x2 = round(phi(x2), 9)
        
        iterations.append([round(a, 9), round(b, 9), x1, x2, phi_x1, phi_x2])
        
        if phi_x1 < phi_x2:
            b = x2  # Narrow interval to [a, x2]
        else:
            a = x1  # Narrow interval to [x1, b]
            
        k -= 1
        
        # Check if we've reached desired tolerance
        if abs(b - a) <= tolerance:
            break
    
    # Handle final iteration if needed
    if k == 1 and abs(b - a) > tolerance:
        x1 = a + 0.01 * (b - a)  # Small perturbation
        phi_x1 = round(phi(x1), 9)
        phi_b = round(phi(b), 9)
        iterations.append([round(a, 9), round(b, 9), x1, b, phi_x1, phi_b])
        
        if phi_x1 < phi_b:
            b = x1
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
a = st.sidebar.number_input("Enter the lower bound (a):", value=1.0)
b = st.sidebar.number_input("Enter the upper bound (b):", value=3.0)
tolerance = st.sidebar.number_input("Enter the error tolerance for the minimum point:", value=0.42)

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