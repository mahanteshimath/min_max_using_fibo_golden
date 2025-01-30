import streamlit as st

st.title('Golden Section Search Method Theory')

st.markdown(r'''
The golden ratio (φ) is defined as:
$$\phi = \frac{\sqrt{5} - 1}{2} \approx 0.618$$

Its complement (1 - φ) is:
$$1 - \phi = 0.382$$

Two points x₁ and x₂ are chosen within interval [a, b]:

$$x_1 = a + (1 - \phi)(b - a)$$

$$x_2 = a + \phi(b - a)$$

1. **Initialization**
   - Start with interval [a, b] Compute intermediate points:

    $$x_1 = a + (1 - \phi)(b - a)$$

    $$x_2 = a + \phi(b - a)$$

2. **Iterative Update**
   - If f(x₁) < f(x₂), new interval: [a, x₂] Otherwise, new interval: [x₁, b]

3. **Stopping Criterion**
   $$|b - a| \leq \epsilon$$
   
   Approximate minimum:
   $$x_{min} = \frac{a + b}{2}$$

### Example for Minimization
Let's find the minimum of:
$$f(x) = (x - 2)^2$$
in the interval [1, 3] with ε = 0.42

#### Step 1: Initial Calculations
- Initial interval: [1, 3] Calculate x₁ and x₂:
  $$x_1 = 1 + 0.382(3 - 1) = 1.764$$
  $$x_2 = 1 + 0.618(3 - 1) = 2.236$$

#### Step 2: Function Evaluation
  $$f(x_1) = (1.764 - 2)^2 = 0.055$$
  $$f(x_2) = (2.236 - 2)^2 = 0.055$$

#### Step 3: Comparison
Since f(x₁) = f(x₂) = 0.055:
- Choose interval [1.764, 3]
- New interval length = |3 - 1.764| = 1.236

#### Step 4: Termination Check
Since 1.236 > 0.42, continue iterations...

Final approximate minimum:
$$x_{min} = 2.000$$
$$f(x_{min}) = 0.000$$
''')
# Additional section for maximization
st.markdown(r'''
### Maximization
Same process as minimization, but reverse comparison:
- If f(x₁) > f(x₂): [a, x₂]
- Otherwise: [x₁, b]
''')

st.divider()
st.title('Fibonacci Search Method Theory')

st.markdown(r'''
The Fibonacci Search Method is an efficient algorithm for finding the minimum or maximum of a unimodal function over a specified interval. It uses the Fibonacci sequence to determine evaluation points, minimizing the number of function evaluations.

### Fibonacci Sequence
The Fibonacci sequence is defined as:
$$F_0 = 0, \quad F_1 = 1, \quad F_n = F_{n-1} + F_{n-2} \quad \text{for} \quad n \geq 2$$

### Steps for Finding the Minimum
1. **Define the Interval:**
   - Start with an interval \([a, b]\) where the minimum is known to exist.

2. **Choose the Number of Iterations:**
   - Decide the number of iterations \(n\) or the desired accuracy.

3. **Calculate Fibonacci Numbers:**
   - Generate Fibonacci numbers up to \(F_n\), where \(F_n\) is the smallest Fibonacci number greater than or equal to \((b - a)/\text{tolerance}\).

4. **Initialize Points:**
   - Compute two points \(x_1\) and \(x_2\) within the interval:
     $$x_1 = a + \frac{F_{n-2}}{F_n}(b - a)$$
     $$x_2 = a + \frac{F_{n-1}}{F_n}(b - a)$$

5. **Evaluate the Function:**
   - Evaluate \(f(x_1)\) and \(f(x_2)\).

6. **Narrow the Interval:**
   - If \(f(x_1) < f(x_2)\), the minimum lies in \([a, x_2]\). Update \(b = x_2\).
   - If \(f(x_1) > f(x_2)\), the minimum lies in \([x_1, b]\). Update \(a = x_1\).

7. **Repeat:**
   - Repeat the process with the new interval and the next Fibonacci number.

8. **Termination:**
   - Stop when the interval is smaller than the desired tolerance. The minimum is approximated as the midpoint of the final interval.

### Example for Minimization
Let's find the minimum of:
$$f(x) = (x - 2)^2$$
in the interval \([1, 3]\) with \(\epsilon = 0.42\).

#### Step 1: Initial Calculations
- Initial interval: \([1, 3]\)
- Choose \(n = 5\) (Fibonacci number \(F_5 = 5\))
- Compute \(x_1\) and \(x_2\):
  $$x_1 = 1 + \frac{F_3}{F_5}(3 - 1) = 1 + \frac{2}{5}(2) = 1.8$$
  $$x_2 = 1 + \frac{F_4}{F_5}(3 - 1) = 1 + \frac{3}{5}(2) = 2.2$$

#### Step 2: Function Evaluation
  $$f(x_1) = (1.8 - 2)^2 = 0.04$$
  $$f(x_2) = (2.2 - 2)^2 = 0.04$$

#### Step 3: Comparison
Since \(f(x_1) = f(x_2) = 0.04\):
- Choose interval \([1.8, 3]\)
- New interval length = \(|3 - 1.8| = 1.2\)

#### Step 4: Termination Check
Since \(1.2 > 0.42\), continue iterations...

Final approximate minimum:
$$x_{min} = 2.000$$
$$f(x_{min}) = 0.000$$
''')

# Additional section for maximization
st.markdown(r'''
### Maximization
The process is similar to finding the minimum, but the comparison is reversed:
- If \(f(x_1) > f(x_2)\), the maximum lies in \([a, x_2]\).
- If \(f(x_1) < f(x_2)\), the maximum lies in \([x_1, b]\).
''')