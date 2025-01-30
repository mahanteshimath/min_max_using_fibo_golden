### **Generic Formula for Golden Section Search Method**
The **Golden Section Search Method** is an optimization technique used to find the **maxima** or **minima** of a unimodal function \( f(x) \) within a specified interval \([a, b]\). It uses the properties of the **golden ratio** to iteratively narrow the search interval. Here's the detailed explanation of the generic formulas for both **maximization** and **minimization**.

---

### **Key Concepts**
- The golden ratio (\(\phi\)) is defined as:
  \[
  \phi = \frac{\sqrt{5} - 1}{2} \approx 0.618.
  \]
  Its complement (\(1 - \phi\)) is:
  \[
  1 - \phi = 0.382.
  \]
  
- In each iteration, two points \(x_1\) and \(x_2\) are chosen within the interval \([a, b]\):
  \[
  x_1 = a + (1 - \phi)(b - a), \quad x_2 = a + \phi(b - a).
  \]

- Depending on whether you're maximizing or minimizing, the interval is reduced by eliminating the less promising region.

---

### **Steps for Minimization**

#### Step 1: **Initialization**
1. Start with an initial interval \([a, b]\).
2. Compute the two intermediate points:
   \[
   x_1 = a + (1 - \phi)(b - a),
   \]
   \[
   x_2 = a + \phi(b - a).
   \]
3. Evaluate the function at these points: \( f(x_1) \) and \( f(x_2) \).

---

#### Step 2: **Iterative Update**
1. Compare \( f(x_1) \) and \( f(x_2) \):
   - If \( f(x_1) < f(x_2) \), the minimum lies in \([a, x_2]\), and the new interval becomes:
     \[
     [a, b] \rightarrow [a, x_2].
     \]
   - Otherwise, the minimum lies in \([x_1, b]\), and the new interval becomes:
     \[
     [a, b] \rightarrow [x_1, b].
     \]

2. Recompute \(x_1\) and \(x_2\) for the updated interval:
   - If the interval is \([a, x_2]\):
     \[
     x_1 = a + (1 - \phi)(x_2 - a), \quad x_2 = x_1 + \phi(x_2 - x_1).
     \]
   - If the interval is \([x_1, b]\):
     \[
     x_2 = x_1 + \phi(b - x_1), \quad x_1 = x_2 - (1 - \phi)(x_2 - x_1).
     \]

---

#### Step 3: **Stopping Criterion**
Stop when the interval length satisfies the error tolerance:
\[
|b - a| \leq \epsilon.
\]

The approximate minimum point is:
\[
x_{\text{min}} = \frac{a + b}{2}.
\]

---

### **Steps for Maximization**
For **maximization**, the process is nearly identical to minimization. The difference is in the comparison step:

1. Compare \( f(x_1) \) and \( f(x_2) \):
   - If \( f(x_1) > f(x_2) \), the maximum lies in \([a, x_2]\).
   - Otherwise, the maximum lies in \([x_1, b]\).

All other steps remain the same.

---

### **Generic Formulas**
#### **For Minimization:**
- Points:
  \[
  x_1 = a + (1 - \phi)(b - a), \quad x_2 = a + \phi(b - a).
  \]
- New intervals:
  - If \( f(x_1) < f(x_2) \): \([a, b] \rightarrow [a, x_2]\),
  - Otherwise: \([a, b] \rightarrow [x_1, b]\).

---

#### **For Maximization:**
- Points:
  \[
  x_1 = a + (1 - \phi)(b - a), \quad x_2 = a + \phi(b - a).
  \]
- New intervals:
  - If \( f(x_1) > f(x_2) \): \([a, b] \rightarrow [a, x_2]\),
  - Otherwise: \([a, b] \rightarrow [x_1, b]\).

---

### **Example for Minimization**

Let \( f(x) = (x - 2)^2 \), interval \([1, 3]\), error tolerance \(\epsilon = 0.42\).

1. **Initialization:**
   \[
   x_1 = 1 + 0.382(3 - 1) = 1.764, \quad x_2 = 1 + 0.618(3 - 1) = 2.236.
   \]

2. Evaluate \( f(x_1) \) and \( f(x_2) \):
   \[
   f(x_1) = (1.764 - 2)^2 = 0.055, \quad f(x_2) = (2.236 - 2)^2 = 0.055.
   \]

3. Compare and update interval:
   - Since \( f(x_1) = f(x_2) \), choose \([1.764, 3]\).

4. Repeat until \(|b - a| \leq 0.42\).

---

### Summary
The **Golden Section Method** efficiently reduces the interval using the golden ratio to approximate the minimum or maximum of a unimodal function. The iterative process stops when the desired error tolerance is achieved.