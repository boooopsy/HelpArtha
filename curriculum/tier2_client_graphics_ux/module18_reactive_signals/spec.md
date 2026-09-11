# Module 18: Reactive Client Runtimes, State DAGs & Fine-Grained Signals

**Tier:** `tier2_client_graphics_ux`  
**Status:** Verified Master Specification  

## 1. Concrete Mental Model
>User interfaces are derived from state: UI = f(State). Fine-grained signals operate like spreadsheet cells: when a base value changes, only dependent downstream cells recompute.

## 2. Core Primitives
Fine-grained reactivity: Signals, getters, setters, subscriber tracking, automatic dependency tracking DAGs, update batching; DOM architecture: Document Object Model, browser rendering pipeline (JS -> Style -> Layout -> Paint -> Composite), surgical DOM modification vs VDOM diffing; component encapsulation, lifecycle hooks.

## 3. Physical & Virtual Workbenches (BOM)
Modern browser DevTools with performance profiler & DOM timeline.

## 4. Primary Literature & Canonical Links
- **[Course]** [Ryan Carniato - A Hands-on Introduction to Fine-Grained Reactivity and Signals](https://www.solidjs.com/)
- **[Specification]** [Dan Abramov et al. - React Fiber Architecture & Incremental Reconciliation](https://github.com/acdlite/react-fiber-architecture)
- **[Seminal Paper]** [Ingar Arvidsson - Functional Reactive Animation and Declarative Temporal Behavior (1997)](https://dl.acm.org/doi/10.1145/258948.258973)

## 5. Standardized Milestone Projects
- **P18_1 (Alpha (Tactile))**: DOM Tree Visualizer — Interactive tool illustrating layout reflows and paint boundaries when modifying DOM elements.
- **P18_2 (Beta (Milestone))**: Zero-Dependency Reactive Signal Engine — Implement createSignal, createEffect, and createMemo in TypeScript with automatic DAG tracking.
- **P18_3 (Gamma (Capstone))**: Fine-Grained UI Component Engine — Build a component library that compiles template literals directly into surgical DOM update instructions.
