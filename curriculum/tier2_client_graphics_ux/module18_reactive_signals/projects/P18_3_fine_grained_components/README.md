# Fine-Grained UI Component Engine (P18_3)

**Module:** Reactive Client Runtimes, State DAGs & Fine-Grained Signals (`module18_reactive_signals`)  
**Classification:** Gamma (Capstone)  

## 1. Project Objective
Build a component library that compiles template literals directly into surgical DOM update instructions.

## 2. Mental Model & Physical Analogy
User interfaces are derived from state: UI = f(State). Fine-grained signals operate like spreadsheet cells: when a base value changes, only dependent downstream cells recompute.

## 3. Bill of Materials / Tools
Modern browser DevTools with performance profiler & DOM timeline.
