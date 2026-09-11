# Zero-Dependency Reactive Signal Engine (P18_2)

**Module:** Reactive Client Runtimes, State DAGs & Fine-Grained Signals (`module18_reactive_signals`)  
**Classification:** Beta (Milestone)  

## 1. Project Objective
Implement createSignal, createEffect, and createMemo in TypeScript with automatic DAG tracking.

## 2. Mental Model & Physical Analogy
User interfaces are derived from state: UI = f(State). Fine-grained signals operate like spreadsheet cells: when a base value changes, only dependent downstream cells recompute.

## 3. Bill of Materials / Tools
Modern browser DevTools with performance profiler & DOM timeline.
