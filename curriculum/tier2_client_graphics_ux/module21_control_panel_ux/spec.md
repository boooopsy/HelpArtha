# Module 21: Industrial Control Panel UX/UI & Tactile Micro-Interactions

**Tier:** `tier2_client_graphics_ux`  
**Status:** Verified Master Specification  

## 1. Concrete Mental Model
>Professional industrial interfaces prioritize clarity, safety, and rapid error identification over decorative flourishes. Controls must provide immediate, unambiguous feedback.

## 2. Core Primitives
Industrial interface design: High-contrast themes, information hierarchies, alarm priority states (nominal, warning, critical), zero-layout-shift architecture; micro-interactions: Skeuomorphic lighting cues, brushed-metal styling, physical switch resistance, synthesized relay-click audio, 44x44px min touch targets; dual-modality ergonomics.

## 3. Physical & Virtual Workbenches (BOM)
Touchscreen monitor / tablet with stylus, high-fidelity headphones for Web Audio testing.

## 4. Primary Literature & Canonical Links
- **[Textbook]** [Donald A. Norman - The Design of Everyday Things (Revised & Expanded Edition, Basic Books)](https://jnd.org/books/the-design-of-everyday-things-revised-and-expanded-edition/)
- **[Textbook]** [Edward R. Tufte - The Visual Display of Quantitative Information (Graphics Press, 2nd Edition)](https://www.edwardtufte.com/tufte/books_vdqi)
- **[Textbook]** [Jef Raskin - The Humane Interface: New Directions for Designing Interactive Systems](https://www.amazon.com/Humane-Interface-Directions-Designing-Interactive/dp/0201379376)
- **[Guide]** [Dieter Rams - Ten Principles for Good Industrial Design (Braun/Vitsœ)](https://www.vitsoe.com/us/about/good-design)

## 5. Standardized Milestone Projects
- **P21_1 (Alpha (Tactile))**: Tactile Audio Synthesizer — Use the Web Audio API to synthesize low-latency mechanical relay clicks and switch clunks for UI interactions.
- **P21_2 (Beta (Milestone))**: Industrial Switch & Gauge Component Library — Build an industrial UI component library in TypeScript featuring switches, dials, and meters.
- **P21_3 (Gamma (Capstone))**: Digital Twin Instrument Dashboard — Build a full-screen industrial control panel with alarm state handling, audio, and live telemetry graphs.
