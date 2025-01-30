import streamlit as st

st.title('Fibonacci and Golden Ratio Theory')

# Introduction
st.markdown(r'''
### Mathematical Foundation

The Fibonacci sequence and Golden Ratio are closely related mathematical concepts.

#### Fibonacci Sequence
The sequence where each number is the sum of the two preceding ones:
$$F_n = F_{n-1} + F_{n-2}$$

#### Golden Ratio (φ)
The golden ratio is defined as:
$$\phi = \frac{1 + \sqrt{5}}{2} \approx 1.618033989$$

#### Relationship
The ratio of consecutive Fibonacci numbers approaches φ:
$$\lim_{n \to \infty} \frac{F_{n+1}}{F_n} = \phi$$

#### Golden Ratio Properties
The golden ratio satisfies:
$$\phi^2 = \phi + 1$$
''')

# Additional mathematical properties
st.latex(r'\phi = 1 + \frac{1}{\phi}')

# Applications section
st.markdown(r'''
### Applications in Optimization
The golden ratio appears in optimization problems where:
$$x_{min} = \frac{a + b\phi}{\phi + 1}$$
''')