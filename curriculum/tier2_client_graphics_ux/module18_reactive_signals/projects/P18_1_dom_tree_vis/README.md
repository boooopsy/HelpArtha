# DOM Tree Visualizer (P18_1)

**Module:** Reactive Client Runtimes, State DAGs & Fine-Grained Signals (`module18_reactive_signals`)  
**Classification:** Alpha (Tactile)  

## 1. Project Objective
Interactive tool illustrating layout reflows and paint boundaries when modifying DOM elements.

## 2. Mental Model & Physical Analogy
User interfaces are derived from state: UI = f(State). Fine-grained signals operate like spreadsheet cells: when a base value changes, only dependent downstream cells recompute.

## 3. Bill of Materials / Tools
Modern browser DevTools with performance profiler & DOM timeline.
