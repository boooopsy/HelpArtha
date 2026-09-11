# Module 05: Calculus of Rates, Gradients & Computational DAGs

**Tier:** `tier0_foundations`  
**Status:** Verified Master Specification  

## 1. Concrete Mental Model
>A derivative is an optical zoom into a curve until it becomes a straight line. Multi-dimensional gradients point in the direction of steepest ascent.

## 2. Core Primitives
Difference quotients, limits, instantaneous rates of change, power rule, product rule, quotient rule, scalar chain rule; partial derivatives, gradient vector, directional derivatives, contour plots, saddle points; forward evaluation passes and reverse-mode chain rule accumulation over DAGs.

## 3. Physical & Virtual Workbenches (BOM)
Graphing calculator, 3D surface clay models.

## 4. Primary Literature & Canonical Links
- **[Textbook]** [Michael Spivak - Calculus (4th Edition, Publish or Perish)](https://www.amazon.com/Calculus-4th-Michael-Spivak/dp/0914098918)
- **[Course]** [Grant Sanderson - 3Blue1Brown: Essence of Calculus Visual Series](https://www.3blue1brown.com/topics/calculus)
- **[Workbench]** [Andrej Karpathy - Building Micrograd: A Tiny Scalar Reverse-Mode Autograd Engine](https://github.com/karpathy/micrograd)
- **[Seminal Paper]** [Seppo Linnainmaa - Representation of Cumulative Rounding Errors (Invention of Backprop, 1970)](https://link.springer.com/article/10.1007/BF01931367)

## 5. Standardized Milestone Projects
- **P05_1 (Alpha (Tactile))**: Difference Quotient Visualizer — Interactive slider showing the secant line converging to a tangent line as delta_x -> 0.
- **P05_2 (Beta (Milestone))**: Scalar Reverse-Mode Autograd Engine — Implement a Python Value class supporting arithmetic operations, DAG building, and .backward().
- **P05_3 (Gamma (Capstone))**: 2D Gradient Descent Visualizer — Plot optimization trajectories over non-convex functions across varying learning rates.
