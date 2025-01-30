import streamlit as st

st.title('Golden Section Search Method Theory')

st.markdown(r'''
### Key Concepts

The golden ratio (φ) is defined as:
$$\phi = \frac{\sqrt{5} - 1}{2} \approx 0.618$$

Its complement (1 - φ) is:
$$1 - \phi = 0.382$$

### Generic Formula
Two points x₁ and x₂ are chosen within interval [a, b]:
$$x_1 = a + (1 - \phi)(b - a)$$
$$x_2 = a + \phi(b - a)$$

### Steps for Minimization

1. **Initialization**
   - Start with interval [a, b]
   - Compute intermediate points:
   $$x_1 = a + (1 - \phi)(b - a)$$
   $$x_2 = a + \phi(b - a)$$

2. **Iterative Update**
   - If f(x₁) < f(x₂), new interval: [a, x₂]
   - Otherwise, new interval: [x₁, b]

3. **Stopping Criterion**
   $$|b - a| \leq \epsilon$$
   
   Approximate minimum:
   $$x_{min} = \frac{a + b}{2}$$

### Example
For f(x) = (x - 2)², interval [1, 3], ε = 0.42:

Initial points:
$$x_1 = 1 + 0.382(3 - 1) = 1.764$$
$$x_2 = 1 + 0.618(3 - 1) = 2.236$$
''')

# Add visual separation
st.markdown("---")

# Additional section for maximization
st.markdown(r'''
### Maximization
Same process as minimization, but reverse comparison:
- If f(x₁) > f(x₂): [a, x₂]
- Otherwise: [x₁, b]
''')