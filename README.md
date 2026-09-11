# WHETSTONE (v3.0.0-PROD)

> **First-Principles Systems, Hardware & Software Engineering Mastery**  
> Cognitive Progression from Concrete Operational (Age 8) to L8/Fellow Distinguished Systems & Hardware Engineer.  
> **100% Standalone · Zero External Dependencies · Zero Leaky Abstractions · Offline First**

---

## ⚡ Quick Start (Run Locally in Seconds)

Whetstone requires **no server processes, no Node.js backend, no PHP, no databases, and no external API keys**.

Simply open the application entrypoint in any modern web browser:

```bash
# macOS
open index.html

# Linux
xdg-open index.html

# Windows
start index.html
```

Or double-click `index.html` directly in your file explorer. All curriculum assets, KaTeX math formulas, interactive simulators, audio synthesizers, and test runners operate under the `file:///` protocol.

---

## 🏛️ Master Architecture & Syllabus Matrix (29 Modules)

Whetstone is organized into a 5-tier pedagogical continuum designed around Piagetian Concrete Precursor invariants: **Physical / Tactile $\to$ Interactive Simulation $\to$ Zero-Magic Code $\to$ Symbolic Invariants**.

```
+-----------------------------------------------------------------------------------+
| TIER 0: Foundations & Mechanical On-Ramp       (Modules 00-07 | 24 Projects)       |
| -> Tactile typing, marble logic, IEEE 754, discrete maths, POSIX system streams   |
+-----------------------------------------------------------------------------------+
| TIER 1: Core Systems, Silicon & Industrial     (Modules 08-17 | 30 Projects)       |
| -> Transistors, RISC-V CPU, cache coherency, RTOS kernels, bare-metal C          |
+-----------------------------------------------------------------------------------+
| TIER 2: Client Engines, Graphics & Reactive UX (Modules 18-22 | 15 Projects)       |
| -> Software renderers, GPU pipelines, reactivity engines, WebAssembly runtimes   |
+-----------------------------------------------------------------------------------+
| TIER 3: Infrastructure, Cloud & Applied Crypto (Modules 23-26 | 12 Projects)       |
| -> Raft consensus, query planners, zero-knowledge proofs, distributed tracing   |
+-----------------------------------------------------------------------------------+
| TIER 4: Frontier AI & Neural Accelerators      (Modules 27-28 |  6 Projects)       |
| -> FlashAttention kernels, quantized inference engines, systolic tensor arrays   |
+-----------------------------------------------------------------------------------+
TOTAL: 29 Standardized Modules · 87 Milestone Projects · 3,480 Sprint Questions
```

### Module Directory Index
- **Tier 0: Foundations & Mechanical On-Ramp**
  - `M00`: The Concrete On-Ramp (Tactile Typing, Marble Logic, Grid Machines)
  - `M01`: Switching Mechanics, Digital Logic & Clocks
  - `M02`: Machine Representation, Bitwise Engines & IEEE 754
  - `M03`: Discrete Mathematics, Invariant Logic & Asymptotic Bounds
  - `M04`: Linear Algebra, Coordinate Systems & Affine Transforms
  - `M05`: Calculus of Rates, Gradients & Computational DAGs
  - `M06`: Discrete Probability, Information Theory & Entropy
  - `M07`: POSIX OS Mechanics, System Streams & Shell Tools
- **Tier 1: Core Systems, Silicon & Industrial Design**
  - `M08`: Systems C Programming, Memory Topology & Pointers
  - `M09`: Computer Architecture & Assembly (RISC-V RV32I)
  - `M10`: Hardware Prototyping: Breadboarding, Schematic Design & PCB Layout
  - `M11`: Industrial CAD, Parametric Modeling & 3D Printing
  - `M12`: Embedded Firmware, Microcontrollers & Hardware Buses (I2C/SPI/UART)
  - `M13`: Pipelined Microarchitecture, Hazards & Branch Prediction
  - `M14`: Virtual Memory, MMUs & Bare-Metal OS Kernel Development
  - `M15`: Concurrency, Atomics & Memory Consistency Models
  - `M16`: Rust Systems Programming, Affine Types & Memory Safety
  - `M17`: Compiler Construction, Lexing, ASTs & Code Generation
- **Tier 2: Client Engines, Spatial Graphics & Industrial UX**
  - `M18`: Reactive Client Runtimes, State DAGs & Fine-Grained Signals
  - `M19`: 3D Spatial Modeling & Asset Pipelines (Blender to glTF)
  - `M20`: WebGL, Compute Shaders & Three.js 3D Telemetry Panels
  - `M21`: Industrial Control Panel UX/UI Design & Tactile Micro-Interactions
  - `M22`: Network Sockets, TCP/IP, Event Demultiplexing & Custom RPC
- **Tier 3: Applied Infrastructure, Crypto & Decentralized State**
  - `M23`: Cache-Conscious Data Structures, B-Trees & Memory Locality
  - `M24`: Storage Engines, Write-Ahead Logs & LSM-Trees
  - `M25`: Distributed Consensus, Logical Clocks & Raft
  - `M26`: Cryptography, Identity & Web3 Decentralized State Machines
- **Tier 4: Frontier Accelerators, On-Device AI & Embedded Silicon**
  - `M27`: GPU Silicon Architecture, SIMD/SIMT & Parallel Compute Kernels
  - `M28`: Edge AI Devices, Quantized Transformer Engines & Silicon Inference

---

## 🛠️ 87 Shipped Milestone Projects & Test Harnesses

Every module features 3 production projects: **Alpha (Tactile Physical)**, **Beta (Milestone Core)**, and **Gamma (Capstone Verification)**.

Each project contains:
- `README.md`: Physical build guide, schematic circuit diagram, and component Bill of Materials (BOM).
- `SPEC.md`: Formal invariant contracts, preconditions, and postconditions.
- `sandbox/scratchpad.py`: Interactive exploratory playground.
- `starter/solution.py`: Clean, type-annotated reference implementations.
- `harness/vectors.json`: 8 calibrated deterministic edge-case test vectors.
- `harness/test_runner.py`: Zero-dependency test runner with static AST verification.

### Running Project Verification
To verify all 87 test runners across the entire curriculum:

```bash
python3 -c "
import glob, subprocess
harnesses = sorted(glob.glob('curriculum/**/harness/test_runner.py', recursive=True))
for h in harnesses:
    res = subprocess.run(['python3', h], capture_output=True, text=True)
    assert res.returncode == 0, f'Failed: {h}'
print(f'All {len(harnesses)} project test harnesses PASSED!')
"
```

You can also execute project test suites interactively inside the web browser via the **Projects** view.

---

## 🕹️ The 5 Mandatory UI Upgrades

1. **Tactile 10-Slot Circular Sprint Buffer**:
   - Replaces linear progress bars with a circular mechanical 10-slot register showing active, filled (conserved), and missed (breached) states.
2. **Web Audio Mechanical Relay Synthesizer**:
   - Synthesizes authentic SPDT mechanical relay clicks on review submission and harmonic confirmation chords upon completing a 10-slot sprint.
3. **30-Second Sensory Reset Screen**:
   - Automatically triggers after each 10-slot sprint with a circular countdown, cognitive breathing cues, and FSRS-6 retention scores.
4. **Interactive Bidirectional Time-Travel Scrubber**:
   - Enables stepping forward and backward through clock cycles (`T0 Setup` $\to$ `T1 Gate Propagate` $\to$ `T2 Clock Edge` $\to$ `T3 State Stabilized`) in Level 2 execution trace drills.
5. **Side-by-Side Dual State Inspector**:
   - Replaces textual stack traces with parallel memory grids: `[Current System State]` vs. `[Required Invariant: Spec Contract]`, highlighting mutated bytes in amber.
6. **Dual-Density Interface Engine**:
   - **Apprentice Mode**: 44px touch targets, mechanical relay cues, and stylus scratchpad.
   - **Master Mode**: Dense 14px layout, terminal inspector styling, and high-speed keyboard shortcuts (`Space` to reveal, `1`–`4` to rate).

---

## 📂 Repository Structure

```
whetstone/
├── assets/
│   └── katex/                  # Offline KaTeX math rendering (CSS, JS, fonts)
├── config/
│   ├── fsrs_params.json        # 21-parameter FSRS-6 scheduler weights
│   └── workspace_rules.json    # Apprentice vs. Master mode specifications
├── content/                    # Raw foundational curriculum domains (1,638 concepts)
├── curriculum/                 # 29 standardized modules across 5 tiers
│   ├── tier0_foundations/      # Modules 00 through 07 (24 projects)
│   ├── tier1_core_systems/     # Modules 08 through 17 (30 projects)
│   ├── tier2_client_graphics_ux/# Modules 18 through 22 (15 projects)
│   ├── tier3_infrastructure_crypto/ # Modules 23 through 26 (12 projects)
│   └── tier4_frontier_accelerators/ # Modules 27 through 28 (6 projects)
├── test_engine/
│   ├── symbolic_evaluator/     # AST invariant verifier
│   ├── execution_sandbox/      # Deterministic sandbox runner
│   └── fsrs_worker/            # Reference FSRS-6 scheduler
├── build/
│   ├── bundle_data.py          # Data compiler -> whetstone-data.js
│   └── scaffold_v3.py          # Master matrix generator
├── index.html                  # Standalone local browser application
├── styles.css                  # Whetstone design system & responsive layout
├── app.js                      # Application controller, router & synthesizers
├── fsrs.js                     # Pure JavaScript FSRS-6 scheduler
├── store.js                    # Local accounts, state & JSON backup/restore
├── whetstone-data.js           # Bundled offline curriculum matrix (34.2 MB)
├── MASTER-SPEC-V3.md           # Canonical v3.0.0-PROD system specification
└── LICENSE                     # Open-source license
```

---

## 🔒 Security & Local Data Management

- **Zero Remote Telemetry**: Your study history, review logs, and passwords never leave your machine.
- **Local Credentials**: Accounts and credentials are stored in local storage for seamless profile switching.
- **One-Click JSON Backup & Restore**: Download your complete study state at any time from the **Settings** view as a JSON file, or restore from a prior backup.
