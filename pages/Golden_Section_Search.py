import streamlit as st
import sympy as sp

def golden_section_method(func, interval, tol):
    phi = (sp.sqrt(5) - 1) / 2  # Golden ratio
    a, b = interval
    steps = []
    
    while abs(b - a) > tol:
        # Compute intermediate points
        x1 = a + (1 - phi) * (b - a)
        x2 = a + phi * (b - a)
        
        # Evaluate function at x1 and x2
        f_x1 = func.subs(x, x1)
        f_x2 = func.subs(x, x2)
        
        # Store step information
        steps.append((a, b, x1, x2, f_x1, f_x2))
        
        # Update the interval
        if f_x1 < f_x2:
            b = x2
        else:
            a = x1
    
    # Final approximate minimum
    x_min = (a + b) / 2
    return x_min, steps

# Streamlit App
st.title("Golden Section Method for Optimization")
st.markdown("""
This app demonstrates the **Golden Section Method** for finding the minimum of a unimodal function. 
The method uses the golden ratio to iteratively reduce the interval of uncertainty.

### Key Formulas:
1. Points \(x_1\) and \(x_2\) in the interval:
   \[
   x_1 = a + (1 - \phi)(b - a), \quad x_2 = a + \phi(b - a)
   \]
   where \(\phi = \frac{\sqrt{5} - 1}{2}\).
2. Update the interval based on:
   - If \(f(x_1) < f(x_2)\), new interval is \([a, x_2]\).
   - Otherwise, new interval is \([x_1, b]\).
3. Stop when \(|b - a| \leq \text{tolerance}\).
""")

# Input form
with st.form("input_form"):
    function_input = st.text_input("Enter the function (e.g., (x - 2)**2):", value="(x - 2)**2")
    interval = st.text_input("Enter the interval [a, b] (comma-separated):", value="1,3")
    tolerance = st.number_input("Enter the error tolerance:", value=0.42, min_value=0.01)
    submitted = st.form_submit_button("Optimize")

if submitted:
    try:
        # Parse input
        x = sp.Symbol('x')
        func = sp.sympify(function_input)
        a, b = map(float, interval.split(","))
        
        # Perform Golden Section Search
        x_min, steps = golden_section_method(func, (a, b), tolerance)
        
        # Display results
        st.markdown(f"### Results:")
        st.latex(f"\\text{{Approximate minimum point: }} x_{{\\text{{min}}}} = {x_min:.4f}")
        st.latex(f"\\text{{Function value at }} x_{{\\text{{min}}}}: f(x_{{\\text{{min}}}}) = {func.subs(x, x_min):.4f}")
        
        # Display steps
        st.markdown("### Steps:")
        st.write("Each row shows the interval bounds, evaluation points, and function values:")
        table_header = ["Step", "a", "b", "x1", "x2", "f(x1)", "f(x2)"]
        table_data = [
            [i + 1, round(a, 4), round(b, 4), round(x1, 4), round(x2, 4), round(f_x1, 4), round(f_x2, 4)]
            for i, (a, b, x1, x2, f_x1, f_x2) in enumerate(steps)
        ]
        st.table([table_header] + table_data)
    except Exception as e:
        st.error(f"An error occurred: {e}")
