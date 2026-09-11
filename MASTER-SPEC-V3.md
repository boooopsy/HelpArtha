================================================================================
WHETSTONE MASTER ARCHITECTURE SPECIFICATION & REPOSITORY HANDOFF
================================================================================
Document Version : 3.0.0-PROD
Classification   : Technical Systems & Curriculum Engineering Blueprint
Target Audience  : Cognitive Progression from Age 8 to L8/Fellow Distinguished
                   Systems & Hardware Engineer
Status           : Production Specification for Antigravity Ingestion
Target Baseline  : Zero Leaky Abstractions, First-Principles Verifiability
================================================================================


--------------------------------------------------------------------------------
TABLE OF CONTENTS
--------------------------------------------------------------------------------
1. Core Learning Science & Pedagogical Invariants
2. UI/UX Critical Audit & Redesign Specification
3. Standardized Repository Architecture & Directory Scaffold
4. Master Syllabus: Complete 29-Module Matrix (Tiers 0 through 4)
5. Comprehensive Module Breakdown (Modules 00 through 28)
   - Module 00: The Concrete On-Ramp
   - Module 01: Switching Mechanics, Digital Logic & Clocks
   - Module 02: Machine Representation, Bitwise Engines & IEEE 754
   - Module 03: Discrete Mathematics, Invariant Logic & Asymptotic Bounds
   - Module 04: Linear Algebra, Coordinate Systems & Affine Transforms
   - Module 05: Calculus of Rates, Gradients & Computational DAGs
   - Module 06: Discrete Probability, Information Theory & Entropy
   - Module 07: POSIX OS Mechanics, System Streams & Shell Tools
   - Module 08: Systems C Programming, Memory Topology & Pointers
   - Module 09: Computer Architecture & Assembly (RISC-V RV32I)
   - Module 10: Hardware Prototyping: Breadboarding & PCB Layout
   - Module 11: Industrial CAD, Parametric Modeling & 3D Printing
   - Module 12: Embedded Firmware, Microcontrollers & Hardware Buses
   - Module 13: Pipelined Microarchitecture, Hazards & Branch Prediction
   - Module 14: Virtual Memory, MMUs & Bare-Metal OS Kernel Development
   - Module 15: Concurrency, Atomics & Memory Consistency Models
   - Module 16: Rust Systems Programming, Affine Types & Memory Safety
   - Module 17: Compiler Construction, Lexing, ASTs & Code Generation
   - Module 18: Reactive Client Runtimes, State DAGs & Fine-Grained Signals
   - Module 19: 3D Spatial Modeling & Asset Pipelines (Blender to glTF)
   - Module 20: WebGL, Compute Shaders & Three.js Telemetry Panels
   - Module 21: Industrial Control Panel UX/UI & Tactile Micro-Interactions
   - Module 22: Network Sockets, TCP/IP & Custom RPC Protocols
   - Module 23: Cache-Conscious Data Structures, B-Trees & Locality
   - Module 24: Storage Engines, Write-Ahead Logs & LSM-Trees
   - Module 25: Distributed Consensus, Logical Clocks & Raft
   - Module 26: Cryptography, Identity & Web3 State Machines
   - Module 27: GPU Silicon Architecture, SIMD/SIMT & Parallel Kernels
   - Module 28: Edge AI Devices, Quantized Transformers & Silicon Inference
6. Total Curriculum Footprint Metrics
7. Antigravity Ingestion & Operational Execution Protocol


================================================================================
1. CORE LEARNING SCIENCE & PEDAGOGICAL INVARIANTS
================================================================================

1.1 THE INVARIANT RETRIEVAL WINDOW (60% - 85%)
Every drill, test battery, and milestone project must maintain a first-attempt
retrieval success rate strictly between 60% and 85%.
* Below 50% Failure State: Working memory crashes under excessive intrinsic
  cognitive load (> 4 +/- 1 chunks). The testing effect drops to zero (g = 0.03),
  active recall degrades into random guessing, and learned helplessness occurs.
* Above 90% Saturation State: Retrieval difficulty is insufficient to trigger
  durable synaptic plasticity, leading to rapid temporal decay.
* Desirable Difficulty Zone: When errors occur within the 15% - 40% band,
  corrective feedback triggers test-potentiated learning, stabilizing schemas
  into long-term memory via the FSRS-6 scheduler.

1.2 THE CONCRETE PRECURSOR MANDATE (PIAGETIAN SEQUENCING)
An 8-year-old child operates in Piaget's Concrete Operational Stage (working
memory capacity = 2 - 3 chunks; formal abstract manipulation does not mature
until ages 11 - 14).
* Axiom: No formal mathematical notation, type system invariant, or software
  syntax may be introduced without a prior physical, mechanical, or visual-
  spatial substrate.
* Execution Ladder:
  1. Physical / Tactile: Rolling marbles, mechanical relay coils, physical
     DIP switches, wooden grids.
  2. Interactive Deterministic Simulation: Digital logic simulators (Falstad,
     Digital), step-by-step CPU instruction scrubbers.
  3. Zero-Magic Code Implementation: Pure, dependency-free C, Python, or Rust.
  4. Symbolic Invariant Verification: Proving correctness, edge states, and
     race conditions without running code.

1.3 STANDARDIZED ASSESSMENT FRAMEWORK (4 x 10 MICRO-SPRINTS)
Monolithic 40-question test batteries exhaust an 8-year-old's 15 - 20 minute
sustained attention window. Every 40-question module battery is split into
four 10-question micro-sprints:
* Level 1 (Mechanics & Recognition - 40 Qs): Rapid binary/ternary property
  identification, circuit pinouts, syntax mechanics, and definitions.
  Target: ~80% first-pass success.
* Level 2 (Procedural Execution & State Tracing - 40 Qs): Step-by-step manual
  execution (cycle-by-cycle, pointer-by-pointer, byte-by-byte) with zero
  guessing. Target: ~70% first-pass success.
* Level 3 (Symbolic Invariants & Failure Proofs - 40 Qs): Spotting race
  conditions, memory leaks, bounds violations, and mathematical counterexamples
  without executing code. Target: ~60% - 65% first-pass success.


================================================================================
2. UI/UX CRITICAL AUDIT & REDESIGN SPECIFICATION
================================================================================

2.1 CRITICAL UX FAILURE MODES (WHY THE CURRENT SYSTEM FAILS AN 8-YEAR-OLD)
1. Text-Dense Prompt Overhead: Multi-clause declarative prose overwhelms
   working memory before the student interacts with the logic.
2. Cold, Opaque Terminal Diffs: Dumping raw stack traces
   ("AssertionError: 0x12 != 0x14") triggers anxiety and guessing instead
   of structural diagnosis.
3. Monolithic Progress Tracking: Linear progress bars ("Question 17 of 40")
   induce executive fatigue around question 12.
4. Abstract Directory & File Friction: Forcing a child to type file paths or
   navigate complex trees wastes cognitive energy on shell mechanics rather
   than algorithms.
5. Project Directory Inconsistency: Projects previously appeared as loose
   markdown notes without consistent test harnesses, inputs, or invariant
   checklists.

2.2 WORKSPACE LAYOUT & COMPONENT SPECIFICATION

+------------------------------------------------------------------------------+
| TOP UTILITY HUD: [Workspace Root] | [FSRS: 94.2%] | [Apprentice] | [Cmd+K]   |
+------------------------------------------------------------------------------+
| SIDEBAR NAV      | MAIN WORKSPACE (Split Panel)                              |
|                  | +--------------------------+----------------------------+ |
| * Cluster Tree   | | SPECIFICATION / PROMPT   | INTERACTIVE WORKBENCH      | |
| * 10-Slot Buffer | | * Visual Schematic       | * Falstad / Digital Engine | |
| * Mode Switch    | | * Plain Objective        | * Monaco Editor (Zero-Dep) | |
|   (Learn / Test) | | * Invariant Checklist    | * Apple Pencil / Stylus    | |
| * Hardware HUD   | +--------------------------+----------------------------+ |
|   (COM4: RP2040) | LOWER INSPECTION DOCK: Dual-State Time-Travel Scrubber    |
|                  | [<< Cycle 12] [PC=0x04] [Cycle 14 >>] | FAIL: Reg x5      |
+------------------------------------------------------------------------------+

2.3 THE FIVE MANDATORY UI UPGRADES
1. Tactile 10-Slot Sprint Buffer:
   - Replaces the linear 40-question bar with a circular, mechanical-style
     10-slot register.
   - Completing a sprint plays a mechanical relay audio cue, triggers a
     30-second sensory reset animation, and saves state to the FSRS-6 scheduler.
2. Interactive Bidirectional Time-Travel Scrubber:
   - For all Level 2 trace drills (circuits, CPU registers, pointer addresses).
   - Sliders and arrow keys scrub backwards and forwards across clock cycles or
     execution steps, visually highlighting state mutations.
3. Side-by-Side Dual State Inspector:
   - On Level 3 test failures, eliminate textual stack traces.
   - Display two parallel visual state memory grids: [System State] vs.
     [Required Invariant]. Highlight conflicting bytes or bits in amber.
4. Visual Exploded-View Memory & Circuit Visualizer:
   - Interactive SVG/Canvas rendering of contiguous memory.
   - Struct padding bytes appear cross-hatched; pointers display animated
     curved vectors to target addresses; cache hits glow green; cache misses
     flash amber.
5. Dual-Density Interface Engine:
   - Apprentice Mode (Default for Learners): Large touch targets (44px min),
     16px monospaced typography, integrated relay/switch audio cues, visual
     circuit simulators, stylus canvas active.
   - Master Mode (Adult / L8 Track): High data density, Vim keybindings,
     multi-file side-by-side diffs, raw GDB/LLDB terminal session, assembly
     disassembly inspectors.


================================================================================
3. STANDARDIZED REPOSITORY ARCHITECTURE & DIRECTORY SCAFFOLD
================================================================================

Every project across all 29 modules must be organized using this exact
structural schema:

whetstone/
|-- config/
|   |-- fsrs_params.json                 # Global FSRS-6 scheduler parameters
|   `-- workspace_rules.json             # Apprentice vs. Master UI rules
|-- curriculum/
|   |-- tier0_foundations/
|   |   |-- module00_onramp/
|   |   |   |-- spec.md                  # Conceptual base & physical BOM
|   |   |   |-- drills/
|   |   |   |   |-- L1_mechanics.json    # 40 Recognition Questions (4x10)
|   |   |   |   |-- L2_execution.json    # 40 Step-by-Step Trace Questions
|   |   |   |   `-- L3_invariants.json   # 40 Symbolic Proof Questions
|   |   |   `-- projects/
|   |   |       |-- P00_1_marble_counter/
|   |   |       |   |-- README.md        # Physical build guide, STL, schematic
|   |   |       |   |-- SPEC.md          # Invariant contracts, pre/post states
|   |   |       |   |-- sandbox/         # Interactive playground/simulator
|   |   |       |   |-- starter/         # Clean starter template with types
|   |   |       |   `-- harness/
|   |   |       |       |-- test_runner.py # Zero-dependency verification runner
|   |   |       |       `-- vectors.json # Deterministic edge-case inputs
|   |   |       |-- P00_2_grid_machine/
|   |   |       `-- P00_3_marble_comparator/
|   |   |-- module01_digital_logic/
|   |   `-- ... [module02 through module07]
|   |-- tier1_core_systems/              # Modules 08 through 17
|   |-- tier2_client_graphics_ux/        # Modules 18 through 22
|   |-- tier3_infrastructure_crypto/     # Modules 23 through 26
|   `-- tier4_frontier_accelerators/     # Modules 27 through 28
`-- test_engine/
    |-- symbolic_evaluator/              # Pure AST invariant verification engine
    |-- execution_sandbox/               # QEMU / Bare-metal execution drivers
    `-- fsrs_worker/                     # Interval calculation & stability daemon


================================================================================
4. MASTER SYLLABUS: COMPLETE 29-MODULE MATRIX (TIERS 0 THROUGH 4)
================================================================================

TIER 0: EXPANDED FOUNDATIONS & MECHANICAL ON-RAMP
- M00: The Concrete On-Ramp (Tactile Typing, Marble Logic, Grid Machines)
- M01: Switching Mechanics, Digital Logic & Clocks
- M02: Machine Representation, Bitwise Engines & IEEE 754
- M03: Discrete Mathematics, Invariant Logic & Asymptotic Bounds
- M04: Linear Algebra, Coordinate Systems & Affine Transforms
- M05: Calculus of Rates, Gradients & Computational DAGs
- M06: Discrete Probability, Information Theory & Entropy
- M07: POSIX OS Mechanics, System Streams & Shell Tools

TIER 1: CORE SYSTEMS, SILICON & INDUSTRIAL DESIGN
- M08: Systems C Programming, Memory Topology & Pointers
- M09: Computer Architecture & Assembly (RISC-V RV32I)
- M10: Hardware Prototyping: Breadboarding, Schematic Design & PCB Layout
- M11: Industrial CAD, Parametric Modeling & 3D Printing (MakerBot/FDM)
- M12: Embedded Firmware, Microcontrollers & Hardware Buses (I2C/SPI/UART)
- M13: Pipelined Microarchitecture, Hazards & Branch Prediction
- M14: Virtual Memory, MMUs & Bare-Metal OS Kernel Development
- M15: Concurrency, Atomics & Memory Consistency Models
- M16: Rust Systems Programming, Affine Types & Memory Safety
- M17: Compiler Construction, Lexing, ASTs & Code Generation

TIER 2: CLIENT RUNTIMES, SPATIAL GRAPHICS & INDUSTRIAL UX
- M18: Reactive Client Runtimes, State DAGs & Fine-Grained Signals
- M19: 3D Spatial Modeling & Asset Pipelines (Blender Mesh Topology to glTF)
- M20: WebGL, Compute Shaders & Three.js 3D Hardware Telemetry Panels
- M21: Industrial Control Panel UX/UI Design & Tactile Micro-Interactions
- M22: Network Sockets, TCP/IP, Event Demultiplexing & Custom RPC

TIER 3: APPLIED INFRASTRUCTURE, CRYPTO & DECENTRALIZED STATE
- M23: Cache-Conscious Data Structures, B-Trees & Memory Locality
- M24: Storage Engines, Write-Ahead Logs & LSM-Trees
- M25: Distributed Consensus, Logical Clocks & Raft
- M26: Cryptography, Identity & Web3 Decentralized State Machines

TIER 4: FRONTIER ACCELERATORS, ON-DEVICE AI & EMBEDDED SILICON
- M27: GPU Silicon Architecture, SIMD/SIMT & Parallel Compute Kernels
- M28: Edge AI Devices, Quantized Transformer Engines & Silicon Inference


================================================================================
5. COMPREHENSIVE MODULE BREAKDOWN (MODULES 00 THROUGH 28)
================================================================================

--------------------------------------------------------------------------------
MODULE 00: THE CONCRETE ON-RAMP
(Tactile, Mechanical & Spatial Bootstrapping)
--------------------------------------------------------------------------------
* Concrete Mental Model:
  Computation is physical motion. Pointers are positions on a floor grid; logic
  bits are mechanical switches redirected by falling marbles; touch typing is
  procedural muscle memory.
* Core Primitives:
  Home-row alphanumeric touch-typing; symbol automation (sub-second recall on
  {}[]()<>:;"'/\~|!@#$%^&*-_+=); mechanical ramps, crossovers, bistable rocker
  bits, gear-bit synchronizers, interceptors; discrete address cells, instruction
  pointers, loop unrolling.
* Physical & Virtual Workbenches:
  - Turing Tumble board (turingtumble.com)
  - Turing Tumble Web Simulator (turingtumble.org)
  - Keybr (keybr.com) & TypingClub (typingclub.com)
  - 8x8 numbered wooden token grid with colored markers
* Standardized Assessment Battery:
  - L1 (Mechanics): 40 Qs. Rapid binary symbol identification, key combinations.
  - L2 (Trace): 40 Qs. Cycle-by-cycle manual trace of gear-bit orientations.
  - L3 (Invariants): 40 Qs. Identify configurations producing infinite marble loops.
* Shipped Milestone Projects:
  - P00.1 (Alpha - Tactile): Marble 3-Bit Counter. Assemble a mechanical 3-bit
    binary up-counter using interlocked gear bits on Turing Tumble.
  - P00.2 (Beta - Milestone): Token Grid State Machine. Build an ASCII 2D grid
    runner in Python executing an in-place bubble sort on an array of 8 cells
    with explicit pointer tracking.
  - P00.3 (Gamma - Capstone): Mechanical Stream Comparator. Construct a physical
    Turing Tumble logic circuit that halts (triggers an interceptor) when two
    sequential inputs differ.

--------------------------------------------------------------------------------
MODULE 01: SWITCHING MECHANICS, DIGITAL LOGIC & CLOCKS
--------------------------------------------------------------------------------
* Concrete Mental Model:
  Current flows or is blocked. A NOT gate is an electromagnet pulling an iron
  contact away from an output line. A clock is an oscillator driving the
  heartbeat of silicon.
* Core Primitives:
  SPDT relays, electromagnets, flyback diodes, pull-up/pull-down resistors,
  push-pull stages; TTL 7400-series gates (AND, OR, NOT, XOR); universal NAND
  logic; half-adders (S = A ^ B, C = A & B), ripple-carry 4-bit adders,
  propagation delay (t_pd); SR-latches, race conditions, edge-triggered
  D-Flip-Flops, setup/hold times (t_su, t_h), metastability.
* Physical & Virtual Workbenches:
  - Breadboard, 5V supply, Songle SRD-05VDC relays, 1N4148 diodes, 74HC08,
    74HC32, 74HC04, 74HC86, 74HC74, NE555P timer, LEDs, resistors.
  - Falstad Circuit Simulator (falstad.com/circuit)
  - Digital Logic Simulator (github.com/hneemann/Digital)
* Primary Literature:
  - Charles Petzold, "CODE: The Hidden Language of Computer Hardware and Software"
  - Ben Eater 8-bit Computer Series (eater.net/8bit)
* Standardized Assessment Battery:
  - L1 (Mechanics): 40 Qs. Gate truth tables, relay terminal pinning, IC pinouts.
  - L2 (Trace): 40 Qs. Tracing logic levels across 5-deep gate cascades.
  - L3 (Invariants): 40 Qs. Spotting setup/hold violations & latch race conditions.
* Shipped Milestone Projects:
  - P01.1 (Alpha - Tactile): Relay Oscillator & Buzzer. Wire a physical relay
    feedback loop with a capacitor and flyback diode to create an audible oscillator.
  - P01.2 (Beta - Milestone): 4-Bit TTL Ripple-Carry Adder. Wire a discrete
    4-bit adder on a breadboard with LED bus outputs and an overflow flag.
  - P01.3 (Gamma - Capstone): Edge-Triggered 8-Bit Register Bank. Construct an
    8-bit register with manual tactile clocking, reset controls, and bus isolation.

--------------------------------------------------------------------------------
MODULE 02: MACHINE REPRESENTATION, BITWISE ENGINES & IEEE 754
--------------------------------------------------------------------------------
* Concrete Mental Model:
  An n-bit register is a circular odometer. Overflow cycles back to zero. Negative
  numbers are defined by shifting perspective on this wheel (Two's Complement).
  Floating point is scientific notation encoded in bitfields.
* Core Primitives:
  Positional bases (2, 10, 16); Two's complement integer wheel, MSB as -2^(N-1),
  sign extension, overflow/underflow, arithmetic vs. logical shifts; bitwise
  operations (&, |, ^, ~), clearing bits (x & ~(1 << n)), toggling bits
  (x ^ (1 << n)), power-of-two checks (x && !(x & (x - 1))); IEEE 754 single
  precision: 1-bit sign, 8-bit biased exponent (E - 127), 23-bit mantissa,
  subnormals, infinities, NaNs.
* Physical & Virtual Workbenches:
  - 8-position DIP switch module with LED indicators.
  - IEEE-754 Interactive Float Converter (h-schmidt.net/FloatConverter/IEEE754.html)
* Standardized Assessment Battery:
  - L1 (Mechanics): 40 Qs. Hex-binary conversions, two's complement sign checks.
  - L2 (Trace): 40 Qs. Step-by-step bit shifts, mask propagation, float multiplication.
  - L3 (Invariants): 40 Qs. Identifying edge cases: signed overflow UB, NaN comparisons.
* Shipped Milestone Projects:
  - P02.1 (Alpha - Tactile): Radial Two's Complement Dial. Interactive visualizer
    mapping integer overflows and sign flips on a circular dial.
  - P02.2 (Beta - Milestone): Software IEEE 754 Engine. Parse 32 raw hex bits
    into sign, exponent, and mantissa in pure Python without float casting.
  - P02.3 (Gamma - Capstone): Binary Telemetry Bit-Packer. Implement a packed
    telemetry serializer in C encoding 3 sensor channels into a single 32-bit
    unsigned integer using bitfields.

--------------------------------------------------------------------------------
MODULE 03: DISCRETE MATHEMATICS, INVARIANT LOGIC & ASYMPTOTIC BOUNDS
--------------------------------------------------------------------------------
* Concrete Mental Model:
  Code without mathematical proofs is guess-and-check. Discrete math supplies the
  formal verification tools to prove software will never break before compiling.
* Core Primitives:
  Propositional logic, truth-table satisfiability (SAT), tautologies, set
  operations, Cartesian products, equivalence relations, DAGs; mathematical
  induction, modular congruences (a = b mod m), GCD, Euclidean algorithm,
  Extended Euclidean algorithm, modular inverse; loop invariants (Initialization,
  Maintenance, Termination), pre/post-conditions, asymptotic notation (O, Omega, Theta).
* Standardized Assessment Battery:
  - L1 (Mechanics): 40 Qs. Set operations, modular congruences, truth table reductions.
  - L2 (Trace): 40 Qs. Manual execution of the Euclidean algorithm & induction steps.
  - L3 (Invariants): 40 Qs. Formulate loop invariants proving binary search correctness.
* Shipped Milestone Projects:
  - P03.1 (Alpha - Tactile): Truth-Table Tautology SAT Solver. Write an automated
    CLI engine evaluating propositional satisfiability for N boolean variables.
  - P03.2 (Beta - Milestone): 16-Bit RSA Cryptosystem. Implement textbook RSA from
    scratch in Python: prime generation, modular inverse, and encryption/decryption.
  - P03.3 (Gamma - Capstone): Topological DAG Cycle Detector. Build a dependency
    resolution engine that detects circular references and emits linear orders.

--------------------------------------------------------------------------------
MODULE 04: LINEAR ALGEBRA, COORDINATE SYSTEMS & AFFINE TRANSFORMS
--------------------------------------------------------------------------------
* Concrete Mental Model:
  A vector is a physical arrow on a grid; a matrix is a dynamic transformation
  that stretches, rotates, or shears space itself.
* Core Primitives:
  Vector spaces, L1 and L2 norms, dot products as projections (A . B = |A||B|cos theta),
  cosine similarity, cross products; matrices as linear coordinate transformers,
  matrix multiplication as composition, determinants as area/volume scaling
  factors, rank, Gaussian elimination with partial pivoting.
* Primary Resource:
  - 3Blue1Brown: Essence of Linear Algebra (youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)
* Standardized Assessment Battery:
  - L1 (Mechanics): 40 Qs. Vector addition, dot product computation, matrix sizing.
  - L2 (Trace): 40 Qs. Multiply 4x4 transformation matrices by hand; trace Gaussian steps.
  - L3 (Invariants): 40 Qs. Prove non-invertibility when det(A) = 0; identify dependencies.
* Shipped Milestone Projects:
  - P04.1 (Alpha - Tactile): 2D Vector Space Sandbox. Interactive canvas showing
    vector additions, basis shifts, and dot product projections.
  - P04.2 (Beta - Milestone): ASCII 3D Wireframe Spinning Cube. Render a 3D
    wireframe cube in the terminal using 4x4 projection and rotation matrices.
  - P04.3 (Gamma - Capstone): Bare Gaussian Linear System Solver. Build a linear
    solver in C implementing Gaussian elimination with partial pivoting.

--------------------------------------------------------------------------------
MODULE 05: CALCULUS OF RATES, GRADIENTS & COMPUTATIONAL DAGS
--------------------------------------------------------------------------------
* Concrete Mental Model:
  A derivative is an optical zoom into a curve until it becomes a straight line.
  Multi-dimensional gradients point in the direction of steepest ascent.
* Core Primitives:
  Difference quotients, limits, instantaneous rates of change, power rule,
  product rule, quotient rule, scalar chain rule; partial derivatives (df/dx),
  gradient vector grad(f), directional derivatives, contour plots, saddle points;
  forward evaluation passes and reverse-mode chain rule accumulation over DAGs.
* Primary Resources:
  - 3Blue1Brown: Essence of Calculus (youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr)
  - Andrej Karpathy: Building Micrograd (github.com/karpathy/micrograd)
* Standardized Assessment Battery:
  - L1 (Mechanics): 40 Qs. Power and product rule symbolic calculations.
  - L2 (Trace): 40 Qs. Trace forward/backward values across a 6-node computational graph.
  - L3 (Invariants): 40 Qs. Spot vanishing and exploding gradients in deep graphs.
* Shipped Milestone Projects:
  - P05.1 (Alpha - Tactile): Difference Quotient Visualizer. Interactive slider
    showing the secant line converging to a tangent line as delta_x -> 0.
  - P05.2 (Beta - Milestone): Scalar Reverse-Mode Autograd Engine. Implement a
    Python Value class supporting arithmetic operations, DAG building, and .backward().
  - P05.3 (Gamma - Capstone): 2D Gradient Descent Visualizer. Plot optimization
    trajectories over non-convex functions across varying learning rates.

--------------------------------------------------------------------------------
MODULE 06: DISCRETE PROBABILITY, INFORMATION THEORY & ENTROPY
--------------------------------------------------------------------------------
* Concrete Mental Model:
  Information is the measure of surprise. If an event is guaranteed, its
  information content is zero. Probability measures expectation; entropy
  quantifies average system-wide uncertainty.
* Core Primitives:
  Sample spaces, mutually exclusive events, conditional probability (P(A|B)),
  Bayes' Theorem; random variables, PMFs, Bernoulli and Binomial distributions,
  expected value, variance; information surprisal (I(x) = -log2 P(x)), Shannon
  entropy (H(X) = -sum P(x)log2 P(x)), prefix-free codes, Kraft's inequality,
  Huffman trees.
* Primary Literature:
  - Claude Shannon, "A Mathematical Theory of Communication" (1948)
* Standardized Assessment Battery:
  - L1 (Mechanics): 40 Qs. Conditional probability calculations, expected values.
  - L2 (Trace): 40 Qs. Construct Huffman frequency trees by hand from distributions.
  - L3 (Invariants): 40 Qs. Prove optimality of Huffman coding via prefix-tree balance.
* Shipped Milestone Projects:
  - P06.1 (Alpha - Tactile): Galton Board Marble Simulator. Virtual marble drop
    simulation demonstrating binomial distribution converging to a bell curve.
  - P06.2 (Beta - Milestone): Bit-Level Huffman Codec. Build a complete file
    compressor and decompressor with custom binary tree serialization.
  - P06.3 (Gamma - Capstone): Pure-Python Naive Bayes Classifier. Build a text
    classification engine computing log-likelihood probabilities over text files.

--------------------------------------------------------------------------------
MODULE 07: POSIX OS MECHANICS, SYSTEM STREAMS & SHELL TOOLS
--------------------------------------------------------------------------------
* Concrete Mental Model:
  In Unix, everything is a stream of bytes accessible via an integer file
  descriptor. Software programs are modular components connected with pipes.
* Core Primitives:
  Standard streams (stdin 0, stdout 1, stderr 2), file descriptor tables,
  redirection (>, >>, <), pipes (|); process lifecycle, fork() address cloning,
  execve() replacement, waitpid() status collection, zombies/orphans, POSIX
  signals (SIGINT, SIGTERM, SIGKILL); inodes, file offsets, system calls
  (open, read, write, close, lseek).
* Standardized Assessment Battery:
  - L1 (Mechanics): 40 Qs. File descriptor numbers, signal actions, syntax.
  - L2 (Trace): 40 Qs. Trace process execution, fork branches, and FD tables.
  - L3 (Invariants): 40 Qs. Identify FD leaks, signal race conditions, zombies.
* Shipped Milestone Projects:
  - P07.1 (Alpha - Tactile): Stream Redirection Sandbox. CLI workbench visualizing
    data flowing through file descriptors and kernel pipe buffers.
  - P07.2 (Beta - Milestone): Custom POSIX Command-Line Shell. Build a Unix shell
    in C supporting execution, multi-stage pipelines (cmd1 | cmd2), and redirects.
  - P07.3 (Gamma - Capstone): Streaming Grep & WC Clone. Build a high-throughput
    stream processing tool using low-level POSIX system calls.

--------------------------------------------------------------------------------
MODULE 08: SYSTEMS C PROGRAMMING, MEMORY TOPOLOGY & POINTERS
--------------------------------------------------------------------------------
* Concrete Mental Model:
  Memory is a single-dimensional array of 8-bit cubbies. A pointer is an index
  into that array. Dereferencing is opening the cubby at that index to read or
  write its contents.
* Core Primitives:
  Flat byte address space, pointer dereferencing (*p), address-of (&x), void
  pointers, typed pointer arithmetic (p + 1 moves by sizeof(*p) bytes), function
  pointers; stack frame layouts (base pointer rbp, stack pointer rsp), dynamic
  heap allocation (malloc/free), chunk headers, fragmentation; struct padding,
  natural word alignment boundaries, cache lines (64 bytes), undefined behavior
  (UB), use-after-free, double-free.
* Primary Literature:
  - Beej's Guide to C Programming (beej.us/guide/bgc)
  - Computer Systems: A Programmer's Perspective (CS:APP) (csapp.cs.cmu.edu)
* Standardized Assessment Battery:
  - L1 (Mechanics): 40 Qs. Pointer syntax, sizeof calculations with padding.
  - L2 (Trace): 40 Qs. Step-by-step memory pointer dereferencing and stack frames.
  - L3 (Invariants): 40 Qs. Identify buffer overflows, off-by-one errors, misalignments.
* Shipped Milestone Projects:
  - P08.1 (Alpha - Tactile): Visual Memory Hex Dumper. Build a C debugging utility
    that inspects memory blocks, printing hex representations and endianness.
  - P08.2 (Beta - Milestone): Byte-Aligned Slab/Arena Allocator. Write a custom
    arena allocator in C featuring out-of-memory guards and reset capabilities.
  - P08.3 (Gamma - Capstone): Cache-Stride Latency Benchmark. Build a diagnostic
    harness in C measuring latency cliffs as stride lengths exceed 64-byte lines.

--------------------------------------------------------------------------------
MODULE 09: COMPUTER ARCHITECTURE & ASSEMBLY (RISC-V RV32I)
--------------------------------------------------------------------------------
* Concrete Mental Model:
  A CPU is a finite state machine: it reads a 32-bit number pointed to by a
  program counter, flips internal routing switches based on that number, passes
  values through an ALU, and increments the counter.
* Core Primitives:
  Program Counter (PC), Register File (x0 hardwired to ground, x1 to x31), ALU,
  Control Unit, Fetch-Decode-Execute cycle; RV32I ISA instruction formats
  (R, I, S, B, U, J-types), arithmetic operations (add, sub, addi), memory
  operations (lw, sw), conditional branches (beq, bne), jumps (jal, jalr),
  standard ABI conventions (a0-a7, ra, sp).
* Simulators:
  - Venus RISC-V Simulator (venus.kvakil.me)
  - RARS Assembler & Simulator (github.com/TheThirdOne/rars)
* Primary Literature:
  - Patterson & Waterman, "The RISC-V Reader: An Open Architecture Atlas"
* Standardized Assessment Battery:
  - L1 (Mechanics): 40 Qs. Register roles, instruction bitfields, immediate signs.
  - L2 (Trace): 40 Qs. Cycle-by-cycle register file changes across an assembly loop.
  - L3 (Invariants): 40 Qs. Detect calling convention bugs (clobbering saved regs).
* Shipped Milestone Projects:
  - P09.1 (Alpha - Tactile): Step-by-Step Register Visualizer. Interactive tool
    showing register transformations and PC jumps during assembly execution.
  - P09.2 (Beta - Milestone): Cycle-Accurate RV32I Software CPU Emulator. Build an
    emulator in C supporting the 37 base RV32I instructions and 64KB of RAM.
  - P09.3 (Gamma - Capstone): Hand-Coded Assembly Quicksort. Write an in-place
    quicksort in pure RISC-V assembly and verify execution on your emulator.

--------------------------------------------------------------------------------
MODULE 10: HARDWARE PROTOTYPING: BREADBOARDING & PCB LAYOUT
--------------------------------------------------------------------------------
* Concrete Mental Model:
  Code requires physical housing. Traces on a printed circuit board are zero-
  resistance wires; decoupling capacitors are local energy reservoirs placed
  adjacent to IC power pins to absorb switching noise.
* Core Primitives:
  Schematic capture, power nets, decoupling capacitor placement (0.1uF ceramics
  adjacent to VDD pins), pull-ups on open-drain lines; PCB track widths vs.
  current capacity, copper weight (1 oz/ft^2), continuous ground planes to avoid
  antennas, trace impedance, DRC rules (clearances, via sizes), soldering technique.
* Tools & Hardware:
  - KiCad EDA Suite (kicad.org)
  - Digital multimeter, temperature-controlled soldering station (Pinecil/TS101),
    lead-free solder, flux pen, copper braid, ESD mat; RP2040 / ESP32-S3 breakouts.
* Standardized Assessment Battery:
  - L1 (Mechanics): 40 Qs. Schematic symbol definitions, PCB footprint recognition.
  - L2 (Trace): 40 Qs. Trace net connectivity across multi-sheet schematics.
  - L3 (Invariants): 40 Qs. Identify ground loops, missing caps, and DRC violations.
* Shipped Milestone Projects:
  - P10.1 (Alpha - Tactile): LED Flashlight PCB. Design a simple 2-layer PCB in
    KiCad with switch, resistors, LEDs, and power routing; generate Gerbers.
  - P10.2 (Beta - Milestone): Custom Microcontroller Breakout Board. Lay out a
    custom board in KiCad for an RP2040/ESP32-S3 with USB-C, LDO, and ESD diodes.
  - P10.3 (Gamma - Capstone): Physical Assembly & Solder Smoke-Test. Solder and
    assemble your custom PCB, verify rail voltages, and flash a blink firmware.

--------------------------------------------------------------------------------
MODULE 11: INDUSTRIAL CAD, PARAMETRIC MODELING & 3D PRINTING
--------------------------------------------------------------------------------
* Concrete Mental Model:
  Physical circuits need robust enclosures to manage thermal dissipation, protect
  against mechanical stress, and provide user-facing controls.
* Core Primitives:
  Parametric sketch constraints (coincident, horizontal, vertical, tangent),
  extrusions, pockets, fillets, chamfers; Design for Additive Manufacturing (DFAM),
  print layer orientation vs. shear strength, the 45-degree overhang rule,
  bridging spans, infill geometry, shell thickness; mechanical fit tolerances
  (dynamic fit 0.3 - 0.4mm, press-fit 0.1mm), snap-fit joints, heat-set brass
  threaded inserts (M2, M3).
* Tools & Hardware:
  - FreeCAD (freecad.org) or Onshape (onshape.com)
  - PrusaSlicer (prusa3d.com/page/prusaslicer_424) or MakerBot Print
  - FDM 3D printer (MakerBot, Bambu Lab, Prusa), calipers, brass insert iron tip.
* Standardized Assessment Battery:
  - L1 (Mechanics): 40 Qs. 2D geometric constraints, slicer settings, glass temps.
  - L2 (Trace): 40 Qs. Step-by-step feature dependency tree rollbacks in CAD.
  - L3 (Invariants): 40 Qs. Identify unconstrained sketches and shear failure risks.
* Shipped Milestone Projects:
  - P11.1 (Alpha - Tactile): Caliper Tolerance Test Array. Model and print a
    precision test gauge with varying pin/hole offsets to benchmark tolerances.
  - P11.2 (Beta - Milestone): Snap-Fit Breadboard Desk Cradle. Design and print a
    screwless snap-fit desk enclosure for an 830-point breadboard and battery.
  - P11.3 (Gamma - Capstone): Custom Enclosure with Brass Inserts. Design, print,
    and assemble a two-piece enclosure for your M10 PCB with brass M3 inserts.

--------------------------------------------------------------------------------
MODULE 12: EMBEDDED FIRMWARE, MICROCONTROLLERS & HARDWARE BUSES
--------------------------------------------------------------------------------
* Concrete Mental Model:
  A microcontroller is a CPU connected directly to physical pins via Memory-Mapped
  I/O (MMIO). Writing to a specific address toggles an external pin between 0V and 3.3V.
* Core Primitives:
  MMIO registers, volatile pointers in C, direction registers, data registers;
  UART (asynchronous, start/stop framing, baud rates); I2C (synchronous, 2-wire
  SDA/SCL, open-drain pull-ups, 7-bit addressing, ACK/NACK, clock stretching);
  SPI (synchronous, 4-wire MOSI/MISO/SCK/CS, full-duplex, CPOL/CPHA modes);
  hardware Interrupt Service Routines (ISRs), latency, reentrancy.
* Standardized Assessment Battery:
  - L1 (Mechanics): 40 Qs. Protocol pinouts, max bus speeds, pull-up math for I2C.
  - L2 (Trace): 40 Qs. Trace logic analyzer oscilloscope waveforms for SPI/I2C.
  - L3 (Invariants): 40 Qs. Identify ISR race conditions and missing volatile keywords.
* Shipped Milestone Projects:
  - P12.1 (Alpha - Tactile): Bit-Banged I2C Sensor Driver. Read environmental
    sensor data by manually driving GPIO pins high/low in C without libraries.
  - P12.2 (Beta - Milestone): Interrupt-Driven Circular UART Driver. Build a UART
    driver using ring buffers streaming command packets without dropping bytes.
  - P12.3 (Gamma - Capstone): SPI OLED Graphics Engine. Build a bare-metal display
    driver in C drawing shapes, text, and bitmaps to an SSD1306 OLED over SPI.

--------------------------------------------------------------------------------
MODULE 13: PIPELINED MICROARCHITECTURE, HAZARDS & BRANCH PREDICTION
--------------------------------------------------------------------------------
* Concrete Mental Model:
  Pipelining is a car assembly line. If a worker downstream waits for a part being
  manufactured upstream, the line stalls unless parts are forwarded across stations.
* Core Primitives:
  Classic 5-stage RISC pipeline: Instruction Fetch (IF), Instruction Decode (ID),
  Execute (EX), Memory Access (MEM), Write Back (WB); hazards: Structural hazards,
  Data hazards (Read-After-Write RAW, Write-After-Read WAR), Control hazards
  (branches); pipeline stalls (NOP bubbles), data forwarding/bypassing; branch
  prediction: 1-bit/2-bit saturating counters, branch target buffers (BTB).
* Standardized Assessment Battery:
  - L1 (Mechanics): 40 Qs. Pipeline stages, hazard classes, branch counter states.
  - L2 (Trace): 40 Qs. Trace multi-stage pipeline timing diagrams with stalls.
  - L3 (Invariants): 40 Qs. Spot RAW dependency stalls and branch flush cycles.
* Shipped Milestone Projects:
  - P13.1 (Alpha - Tactile): Pipeline Hazard Visualizer. Interactive diagram
    illustrating instruction bubbles and data forwarding paths across cycles.
  - P13.2 (Beta - Milestone): 5-Stage Pipelined RV32I Simulator. Extend the M09
    emulator into a 5-stage pipelined simulator with hazard forwarding.
  - P13.3 (Gamma - Capstone): Branch Prediction Performance Harness. Implement a
    2-bit saturating counter simulator and demonstrate throughput collapse.

--------------------------------------------------------------------------------
MODULE 14: VIRTUAL MEMORY, MMUS & BARE-METAL OS KERNEL DEVELOPMENT
--------------------------------------------------------------------------------
* Concrete Mental Model:
  Virtual memory gives each application the illusion that it has exclusive access
  to the entire RAM space. The MMU dynamically translates these virtual addresses.
* Core Primitives:
  Virtual vs. physical addresses, 4KB page frames, multi-level page tables
  (RISC-V Sv39, x86-64 4-level paging), page table entries (PTE) with valid, read,
  write, execute flags; Memory Management Unit (MMU), Translation Lookaside
  Buffer (TLB), TLB shootdowns, page faults, demand paging; privilege rings
  (User vs. Supervisor/Kernel mode), system call traps (ecall), context switching,
  thread control blocks (TCBs).
* Primary Literature:
  - Arpaci-Dusseau, "Operating Systems: Three Easy Pieces (OSTEP)" (ostep.org)
  - OSDev Wiki (wiki.osdev.org)
* Standardized Assessment Battery:
  - L1 (Mechanics): 40 Qs. Page offset math, bit field extraction for page indexes.
  - L2 (Trace): 40 Qs. Trace a multi-level page table walk by hand to physical RAM.
  - L3 (Invariants): 40 Qs. Identify double-fault conditions and privilege escalation.
* Shipped Milestone Projects:
  - P14.1 (Alpha - Tactile): Page Table Walker & TLB Cache. Build a standalone
    address translation engine in C parsing multi-level page tables with TLB.
  - P14.2 (Beta - Milestone): QEMU Bare-Metal Kernel. Write a minimal OS kernel in
    C and assembly running on QEMU that configures MMU and timer interrupts.
  - P14.3 (Gamma - Capstone): Demand-Paging Fault Handler. Implement a page-fault
    exception handler that dynamically allocates and maps physical pages.

--------------------------------------------------------------------------------
MODULE 15: CONCURRENCY, ATOMICS & MEMORY CONSISTENCY MODELS
--------------------------------------------------------------------------------
* Concrete Mental Model:
  Without coordination, multiple CPU cores accessing shared memory will overwrite
  each other's data. Memory consistency models define the rules for when writes
  by one core become visible to others.
* Core Primitives:
  Critical sections, race conditions, mutual exclusion, deadlocks, livelocks,
  priority inversion; atomic instructions: Test-and-Set (TAS), Compare-and-Swap
  (CAS), Fetch-and-Add (FAA); memory consistency models: Sequential consistency,
  relaxed consistency, acquire-release semantics, memory barriers/fences,
  compiler and hardware out-of-order reordering.
* Standardized Assessment Battery:
  - L1 (Mechanics): 40 Qs. Atomic built-in syntax, memory order classifications.
  - L2 (Trace): 40 Qs. Trace interleaved multi-thread operations showing stale reads.
  - L3 (Invariants): 40 Qs. Prove correctness of lock-free queues using acquire-release.
* Shipped Milestone Projects:
  - P15.1 (Alpha - Tactile): Race Condition Stress Lab. Multi-threaded program
    demonstrating data corruption on shared balances without synchronization.
  - P15.2 (Beta - Milestone): Ticket Lock & Spinlock in C. Implement fair mutual-
    exclusion locks using GCC atomic built-ins (__atomic_compare_exchange_n).
  - P15.3 (Gamma - Capstone): Lock-Free SPSC Ring Buffer. Build a single-producer
    single-consumer queue utilizing explicit acquire-release memory fences.

--------------------------------------------------------------------------------
MODULE 16: RUST SYSTEMS PROGRAMMING, AFFINE TYPES & MEMORY SAFETY
--------------------------------------------------------------------------------
* Concrete Mental Model:
  Every resource has a single owner. Ownership can be moved or temporarily lent
  out, but data cannot be mutated while shared references exist.
* Core Primitives:
  Affine type systems, linear logic, ownership, move semantics, copy semantics,
  the Drop trait, RAII; the borrow checker: Aliasing XOR Mutability theorem:
    (Shared AND NOT Mutable) OR (NOT Shared AND Mutable)
  lexical vs. non-lexical lifetimes, lifetime annotations ('a); safe vs. unsafe
  Rust, raw pointers (*const T, *mut T), thread marker traits (Send and Sync).
* Primary Literature:
  - The Rust Programming Language Book (doc.rust-lang.org/book)
  - The Rustonomicon: Unsafe Rust (doc.rust-lang.org/nomicon)
* Standardized Assessment Battery:
  - L1 (Mechanics): 40 Qs. Borrow checker errors, trait bounds, lifetime syntax.
  - L2 (Trace): 40 Qs. Trace ownership transfer trees and reference lifetimes.
  - L3 (Invariants): 40 Qs. Prove data-race freedom using Send and Sync invariants.
* Shipped Milestone Projects:
  - P16.1 (Alpha - Tactile): Borrow Checker Matrix. Resolve 20 intentionally
    broken Rust programs without resorting to .clone() or reference counting.
  - P16.2 (Beta - Milestone): Memory-Safe Doubly-Linked List. Implement a doubly-
    linked list comparing safe abstraction patterns against raw unsafe pointers.
  - P16.3 (Gamma - Capstone): Multi-Threaded Worker Pool. Build a thread pool in
    Rust that dispatches jobs over crossbeam channels with panic recovery.

--------------------------------------------------------------------------------
MODULE 17: COMPILER CONSTRUCTION, LEXING, ASTS & CODE GENERATION
--------------------------------------------------------------------------------
* Concrete Mental Model:
  A compiler translates human intent into machine execution by converting text
  into a stream of tokens, structuring tokens into a syntax tree, and flattening
  that tree into assembly.
* Core Primitives:
  Lexical analysis: Token streams, lexemes, regular grammars, DFAs, source position
  tracking; syntactic analysis: Context-Free Grammars (CFG), BNF, recursive descent
  parsing, Pratt parsing (operator precedence climbing), Abstract Syntax Trees (AST);
  code generation: Symbol tables, lexical scope analysis, instruction emission
  targeting your RISC-V RV32I emulator.
* Primary Literature:
  - Bob Nystrom, "Crafting Interpreters" (craftinginterpreters.com)
* Standardized Assessment Battery:
  - L1 (Mechanics): 40 Qs. Regular grammar definitions, AST node types, precedence.
  - L2 (Trace): 40 Qs. Trace Pratt parsing call stacks through nested expressions.
  - L3 (Invariants): 40 Qs. Detect ambiguity in grammars and unhandled syntax errors.
* Shipped Milestone Projects:
  - P17.1 (Alpha - Tactile): Regex-to-DFA Lexer Engine. Build a tokenizer that
    compiles regex patterns into state transition tables with line tracking.
  - P17.2 (Beta - Milestone): Pratt Expression Parser. Hand-craft a parser that
    converts mathematical expressions with mixed operator precedence into an AST.
  - P17.3 (Gamma - Capstone): Mini-Lang Compiler. Build an end-to-end compiler for
    a custom imperative language compiling directly to valid RISC-V assembly.

--------------------------------------------------------------------------------
MODULE 18: REACTIVE CLIENT RUNTIMES, STATE DAGS & FINE-GRAINED SIGNALS
--------------------------------------------------------------------------------
* Concrete Mental Model:
  User interfaces are derived from state: UI = f(State). Fine-grained signals
  operate like spreadsheet cells: when a base value changes, only dependent
  downstream cells recompute.
* Core Primitives:
  Fine-grained reactivity: Signals, getters, setters, subscriber tracking,
  automatic dependency tracking DAGs, update batching; DOM architecture:
  Document Object Model, the browser rendering pipeline (JS -> Style -> Layout
  -> Paint -> Composite), direct surgical DOM modification vs. virtual DOM
  diffing; component encapsulation, lifecycle hooks, event delegation.
* Standardized Assessment Battery:
  - L1 (Mechanics): 40 Qs. Signal primitive signatures, DOM node traversal properties.
  - L2 (Trace): 40 Qs. Trace reactive dependency registration across a computed DAG.
  - L3 (Invariants): 40 Qs. Identify infinite update loops and DOM layout thrashing.
* Shipped Milestone Projects:
  - P18.1 (Alpha - Tactile): DOM Tree Visualizer. Interactive tool illustrating
    layout reflows and paint boundaries when modifying DOM elements.
  - P18.2 (Beta - Milestone): Zero-Dependency Reactive Signal Engine. Implement
    createSignal, createEffect, and createMemo in TypeScript with automatic DAG tracking.
  - P18.3 (Gamma - Capstone): Fine-Grained UI Component Engine. Build a component
    library that compiles template literals directly into surgical DOM update instructions.

--------------------------------------------------------------------------------
MODULE 19: 3D SPATIAL MODELING & ASSET PIPELINES (BLENDER TO GLTF)
--------------------------------------------------------------------------------
* Concrete Mental Model:
  3D digital objects are wireframe shells of interconnected triangles. The
  orientation of their surface normals governs how light interacts with the material.
* Core Primitives:
  Mesh topology: Vertices, edges, faces, non-manifold geometry, quad modeling vs.
  triangulation, surface normal vectors, smoothing groups; UV unwrapping: UV
  coordinates (U, V in [0, 1]), seam placement, texture projection, PBR materials
  (base color, roughness, metallic, normal maps); asset pipelines: glTF/GLB
  formats, hierarchical scene graphs, transform nodes.
* Software Tools:
  - Blender (blender.org)
  - glTF 2.0 validators
* Standardized Assessment Battery:
  - L1 (Mechanics): 40 Qs. Vertex coordinate formats, normal vector orientations.
  - L2 (Trace): 40 Qs. Trace coordinate space transitions (Object -> World -> Camera).
  - L3 (Invariants): 40 Qs. Identify non-manifold geometry and inverted surface normals.
* Shipped Milestone Projects:
  - P19.1 (Alpha - Tactile): Topology Repair Lab. Import a flawed 3D mesh into
    Blender and clean it into an all-quad manifold surface with consistent normals.
  - P19.2 (Beta - Milestone): Parametric Industrial Knob Asset. Model a 3D control
    knob with grip fluting and set screws, unwrap UVs, and export to glTF.
  - P19.3 (Gamma - Capstone): Automated PCB-to-glTF Pipeline. Write a Python script
    for Blender that parses board dimensions and generates a detailed 3D enclosure.

--------------------------------------------------------------------------------
MODULE 20: WEBGL, COMPUTE SHADERS & THREE.JS 3D TELEMETRY PANELS
--------------------------------------------------------------------------------
* Concrete Mental Model:
  WebGL exposes graphics hardware directly inside the browser. Arrays of 3D
  coordinates are uploaded to GPU buffers, where vertex and fragment shaders
  render them in parallel.
* Core Primitives:
  WebGL state machine, buffers (VBO, EBO), Vertex Shaders (transforming vertices
  into clip space), Fragment Shaders (calculating pixel colors), uniforms,
  attributes, varyings; Three.js architecture: Scene graphs, perspective/
  orthographic cameras, meshes, PBR shaders (MeshStandardMaterial), shadow maps,
  lighting; real-time render loops (requestAnimationFrame), raycasting.
* Standardized Assessment Battery:
  - L1 (Mechanics): 40 Qs. GLSL shader syntax, Three.js class hierarchies.
  - L2 (Trace): 40 Qs. Trace raycasting intersections through bounding spheres.
  - L3 (Invariants): 40 Qs. Spot WebGL context loss vulnerabilities and shader precision leaks.
* Shipped Milestone Projects:
  - P20.1 (Alpha - Tactile): Raw WebGL Lighted Prism. Render an interactive 3D
    prism in raw WebGL without external libraries, compiling custom shaders.
  - P20.2 (Beta - Milestone): 3D Digital-Twin Telemetry Dashboard. Build a Three.js
    interface that renders the 3D enclosure from M11, rotating with live sensor data.
  - P20.3 (Gamma - Capstone): Thermal Heatmap Surface Shader. Write a custom GLSL
    fragment shader projecting a dynamic thermal gradient across the 3D mesh.

--------------------------------------------------------------------------------
MODULE 21: INDUSTRIAL CONTROL PANEL UX/UI & TACTILE MICRO-INTERACTIONS
--------------------------------------------------------------------------------
* Concrete Mental Model:
  Professional industrial interfaces prioritize clarity, safety, and rapid error
  identification over decorative flourishes. Controls must provide immediate,
  unambiguous feedback.
* Core Primitives:
  Industrial interface design: Tactical high-contrast themes, information density
  hierarchies, dedicated alarm priority states (nominal, warning, critical),
  zero-layout-shift architecture; micro-interactions: Skeuomorphic lighting cues,
  brushed-metal styling, physical switch resistance, synthesized relay-click
  audio, 44x44px minimum touch targets; dual-modality ergonomics (keyboard + stylus).
* Standardized Assessment Battery:
  - L1 (Mechanics): 40 Qs. Industrial color coding standards (ISO/IEC), touch targets.
  - L2 (Trace): 40 Qs. Trace state transitions through multi-stage confirmation dialogs.
  - L3 (Invariants): 40 Qs. Identify ambiguous alarm states and dangerous unconfirmed controls.
* Shipped Milestone Projects:
  - P21.1 (Alpha - Tactile): Tactile Audio Synthesizer. Use the Web Audio API to
    synthesize low-latency mechanical relay clicks and switch clunks for UI interactions.
  - P21.2 (Beta - Milestone): Industrial Switch & Gauge Component Library. Build an
    industrial UI component library in TypeScript featuring switches, dials, and meters.
  - P21.3 (Gamma - Capstone): Digital Twin Instrument Dashboard. Build a full-screen
    industrial control panel with alarm state handling, audio, and live telemetry graphs.

--------------------------------------------------------------------------------
MODULE 22: NETWORK SOCKETS, TCP/IP & CUSTOM RPC PROTOCOLS
--------------------------------------------------------------------------------
* Concrete Mental Model:
  Network programming connects systems via data streams. The OS handles buffering,
  packet ordering, and retransmissions under the hood.
* Core Primitives:
  Transport layer fundamentals: TCP 3-way handshake (SYN, SYN-ACK, ACK), sequence
  numbers, sliding-window flow control, congestion control; I/O multiplexing:
  Non-blocking sockets (O_NONBLOCK), kernel event demultiplexing (select, poll,
  epoll); binary framing protocols: Length-prefixed payloads, magic bytes,
  checksums, zero-copy serialization.
* Primary Literature:
  - Beej's Guide to Network Programming (beej.us/guide/bgnet)
  - W. Richard Stevens, "TCP/IP Illustrated, Volume 1"
* Standardized Assessment Battery:
  - L1 (Mechanics): 40 Qs. Socket API function sequences, TCP header layouts.
  - L2 (Trace): 40 Qs. Trace TCP sequence and acknowledgement numbers through transfers.
  - L3 (Invariants): 40 Qs. Identify socket handle leaks and framing boundary bugs.
* Shipped Milestone Projects:
  - P22.1 (Alpha - Tactile): Raw Packet Hex Decoder. Build a CLI utility that parses
    Ethernet, IPv4, and TCP headers from raw socket captures.
  - P22.2 (Beta - Milestone): High-Throughput Linux Epoll Server. Build an event-
    driven server in C using Linux epoll capable of handling 10,000 idle connections.
  - P22.3 (Gamma - Capstone): Binary RPC Wire Protocol & Engine. Design a binary
    protocol with varint encoding and CRC32 checks connecting your web panel to hardware.

--------------------------------------------------------------------------------
MODULE 23: CACHE-CONSCIOUS DATA STRUCTURES, B-TREES & LOCALITY
--------------------------------------------------------------------------------
* Concrete Mental Model:
  Pointer chasing across RAM introduces significant memory latency. Cache-
  conscious data structures group contiguous data together into blocks sized to
  match CPU cache lines.
* Core Primitives:
  Hardware caching dynamics: Spatial locality, temporal locality, cache line
  invalidations, structs of arrays (SoA) vs. arrays of structs (AoS); B-Trees vs.
  Binary Search Trees: Node sizing aligned to 64-byte cache lines and 4KB page
  boundaries, fan-out mechanics, node splitting, key search via SIMD vectorization.
* Standardized Assessment Battery:
  - L1 (Mechanics): 40 Qs. Cache line sizing rules, B-Tree order and height equations.
  - L2 (Trace): 40 Qs. Trace B-Tree insertions, node splits, and key rebalancing by hand.
  - L3 (Invariants): 40 Qs. Prove maximum tree height invariants under worst-case deletes.
* Shipped Milestone Projects:
  - P23.1 (Alpha - Tactile): Cache-Line Access Visualizer. Visual tool mapping
    memory traversals and displaying cache hits vs. cache misses in real time.
  - P23.2 (Beta - Milestone): 64-Byte Cache-Conscious B-Tree. Implement a B-Tree
    in C/Rust with node sizing matched to 64-byte cache lines; benchmark vs. binary trees.
  - P23.3 (Gamma - Capstone): SIMD-Accelerated Vector Scanner. Write a search engine
    in C using AVX2/NEON intrinsics scanning 8 keys per clock cycle without branching.

--------------------------------------------------------------------------------
MODULE 24: STORAGE ENGINES, WRITE-AHEAD LOGS & LSM-TREES
--------------------------------------------------------------------------------
* Concrete Mental Model:
  Data stored only in memory will be lost if power fails. To guarantee durability,
  modifications must be written sequentially to a disk log before updating memory.
* Core Primitives:
  Durability mechanics: Flash block erase physics, sequential vs. random I/O,
  write amplification, kernel buffering and fsync(); LSM-Tree architecture:
  MemTable (in-memory sorted buffer), Write-Ahead Log (WAL for crash recovery),
  SSTables (Sorted String Tables on disk), Bloom filters, multi-way merge
  background compaction.
* Primary Literature:
  - O'Neil et al., "The Log-Structured Merge-Tree (LSM-Tree)" (1996)
* Standardized Assessment Battery:
  - L1 (Mechanics): 40 Qs. LSM-Tree component roles, Bloom filter false-positive math.
  - L2 (Trace): 40 Qs. Trace a crash-recovery replay from a WAL; trace SSTable compaction.
  - L3 (Invariants): 40 Qs. Identify data-loss vulnerabilities when fsync is omitted.
* Shipped Milestone Projects:
  - P24.1 (Alpha - Tactile): Append-Only WAL Crash Recovery Engine. Build a logging
    system that recovers an in-memory database state after a SIGKILL.
  - P24.2 (Beta - Milestone): Slotted-Page Storage Manager. Implement a binary page
    manager in C with tuple slot offsets, frame pinning, and LRU page eviction.
  - P24.3 (Gamma - Capstone): Zero-Dependency LSM-Tree Database. Build a complete
    LSM-Tree engine featuring MemTables, SSTables, Bloom filters, and compaction.

--------------------------------------------------------------------------------
MODULE 25: DISTRIBUTED CONSENSUS, LOGICAL CLOCKS & RAFT
--------------------------------------------------------------------------------
* Concrete Mental Model:
  Physical clocks drift across independent network nodes. Distributed systems must
  establish ordering using sequence numbers (logical clocks) and require majority
  quorums before confirming state.
* Core Primitives:
  Distributed time: Clock drift, network partitions, split-brain conditions,
  Lamport Timestamps, Vector Clocks (causal tracking); Raft consensus protocol:
  Roles (Follower, Candidate, Leader), randomized election timeouts, term numbers,
  log replication (AppendEntries), log matching invariant, commit index
  advancement, safety invariants.
* Primary Literature:
  - Ongaro & Ousterhout, "In Search of an Understandable Consensus Algorithm (Raft)" (2014)
  - The Secret Lives of Data: Raft Visualization (thesecretlivesofdata.com/raft)
* Standardized Assessment Battery:
  - L1 (Mechanics): 40 Qs. Raft term rules, quorum calculation equations (N/2 + 1).
  - L2 (Trace): 40 Qs. Trace election terms, split votes, and log conflict resolutions.
  - L3 (Invariants): 40 Qs. Prove Leader Completeness: committed entries persist in leaders.
* Shipped Milestone Projects:
  - P25.1 (Alpha - Tactile): Network Chaos Simulation Workbench. Build a simulated
    distributed test harness injecting configurable latency, packet drops, and partitions.
  - P25.2 (Beta - Milestone): Vector Clock Causal Message Broker. Implement a
    multi-node messaging system tracking causal history and detecting write conflicts.
  - P25.3 (Gamma - Capstone): Full Raft Consensus Engine. Implement the Raft
    protocol from scratch in Go or Rust, maintaining consistency through network splits.

--------------------------------------------------------------------------------
MODULE 26: CRYPTOGRAPHY, IDENTITY & WEB3 STATE MACHINES
--------------------------------------------------------------------------------
* Concrete Mental Model:
  A decentralized state machine is a shared virtual computer. Cryptographic keys
  authenticate identity, digital signatures validate transactions, and
  cryptographic hashes secure the shared ledger.
* Core Primitives:
  Cryptographic primitives: Symmetric ciphers (AES-GCM), cryptographic hash
  functions (SHA-256, Keccak-256), public-key cryptography, asymmetric digital
  signatures (ECDSA on secp256k1, Ed25519); Merkle trees: Cryptographic inclusion
  proofs, tamper-evident logs, authenticated dictionaries; decentralized
  execution: State transitions, account models vs. UTXO, gas accounting systems,
  peer-to-peer state synchronization.
* Standardized Assessment Battery:
  - L1 (Mechanics): 40 Qs. Key lengths, hash properties, signature verification steps.
  - L2 (Trace): 40 Qs. Trace a Merkle proof path from leaf hash up to root hash.
  - L3 (Invariants): 40 Qs. Identify reentrancy vulnerabilities and signature malleability.
* Shipped Milestone Projects:
  - P26.1 (Alpha - Tactile): Merkle Tree Proof Engine. Build an engine in
    TypeScript/Rust that generates and verifies cryptographic inclusion proofs.
  - P26.2 (Beta - Milestone): Pure-Python AES-128 GCM Engine. Implement AES
    authenticated encryption in Galois/Counter Mode from first principles.
  - P26.3 (Gamma - Capstone): Decentralized State Machine Engine. Build a replicated
    ledger engine processing Ed25519-signed transactions and validating state roots.

--------------------------------------------------------------------------------
MODULE 27: GPU SILICON ARCHITECTURE, SIMD/SIMT & PARALLEL KERNELS
--------------------------------------------------------------------------------
* Concrete Mental Model:
  A CPU core is a fast, versatile processor handling complex serial tasks. A GPU
  consists of thousands of lightweight execution units operating in lock-step to
  process large arrays of data in parallel.
* Core Primitives:
  GPU hardware topology: Latency vs. throughput architectures, streaming
  multiprocessors (SMs), high-bandwidth memory (HBM), PCIe transfer bottlenecks;
  the SIMT model: Grids, thread blocks, warps (32 threads running lock-step),
  warp divergence, coalesced memory access; GEMM optimization: The naive O(N^3)
  matmul memory wall, 2D shared-memory tiling, register reuse, arithmetic
  intensity, and the Roofline Model.
* Primary Resource:
  - Simon Boehm: How to Optimize a CUDA Matmul Kernel (siboehm.com/articles/22/CUDA-MMM)
* Standardized Assessment Battery:
  - L1 (Mechanics): 40 Qs. Thread/block indexing formulas, warp size conventions.
  - L2 (Trace): 40 Qs. Trace thread index mappings and 2D tile coordinates in shared RAM.
  - L3 (Invariants): 40 Qs. Identify warp divergence branches and uncoalesced memory reads.
* Shipped Milestone Projects:
  - P27.1 (Alpha - Tactile): Warp Divergence Simulator. Build a cycle simulator
    demonstrating execution serialization when threads take divergent branch paths.
  - P27.2 (Beta - Milestone): Hardware Roofline Benchmark Engine. Build a tool
    measuring arithmetic intensity determining compute vs. memory bounds.
  - P27.3 (Gamma - Capstone): 2D Tiled Shared-Memory GEMM Kernel. Write an optimized
    matrix multiplication kernel in CUDA/WebGPU achieving 8x speedup over naive baselines.

--------------------------------------------------------------------------------
MODULE 28: EDGE AI DEVICES, QUANTIZED TRANSFORMERS & SILICON INFERENCE
--------------------------------------------------------------------------------
* Concrete Mental Model:
  A transformer model is a sequence of matrix operations. Text generation
  involves multiplying input vectors by weight matrices. By quantizing weights
  from 32-bit floats to 8-bit integers, models can run on microcontrollers.
* Core Primitives:
  Transformer mechanics: Scaled dot-product attention (softmax(QK^T / sqrt(d_k))V),
  multi-head attention, Rotary Position Embeddings (RoPE), RMSNorm, residual
  connections; quantization systems: Converting 32-bit floats to 8-bit signed
  integers (r = S * (q - Z)), symmetric quantization, dynamic range scaling,
  outlier channel preservation; inference optimization: Autoregressive token
  generation loops, KV caches, streaming tokens directly to hardware displays.
* Primary Literature:
  - Vaswani et al., "Attention Is All You Need" (1947)
  - Dao et al., "FlashAttention: Fast and Memory-Efficient Attention" (2022)
* Standardized Assessment Battery:
  - L1 (Mechanics): 40 Qs. Attention equation dimensions, quantization scale math.
  - L2 (Trace): 40 Qs. Trace a complete forward pass of a single-layer transformer.
  - L3 (Invariants): 40 Qs. Spot numeric underflow in softmax layers and KV-cache bugs.
* Shipped Milestone Projects:
  - P28.1 (Alpha - Tactile): Standalone Transformer Inference Engine. Write an
    inference engine in pure C that loads raw binary weights and executes forward passes.
  - P28.2 (Beta - Milestone): INT8 Tensor Quantization Tool. Build a converter that
    quantizes FP32 transformer weights into INT8 with per-channel scaling factors.
  - P28.3 (Gamma - Capstone - The Physical Mini-AI Device): Flash your quantized
    transformer engine onto an embedded microcontroller (ESP32-S3 / RP2040) housed
    in your custom 3D-printed enclosure from M11, running real-time on-device
    inference displayed on an integrated OLED screen.


================================================================================
6. TOTAL CURRICULUM FOOTPRINT METRICS
================================================================================

--------------------------------------------------------------------------------
Tier     Domain Area                Modules   Tests (40 Qs)  Total Qs   Projects
--------------------------------------------------------------------------------
Tier 0   Foundations, Math, POSIX   M00 - M07 258 Tests      10,320 Qs  24 Shipped
Tier 1   Systems C, Silicon, CAD    M08 - M17 344 Tests      13,760 Qs  30 Shipped
Tier 2   Client UI, 3D, UX, RPC     M18 - M22 160 Tests       6,400 Qs  15 Shipped
Tier 3   Storage, Raft, Crypto      M23 - M26 134 Tests       5,360 Qs  12 Shipped
Tier 4   GPU Silicon, Edge AI       M27 - M28  64 Tests       2,560 Qs   6 Shipped
--------------------------------------------------------------------------------
TOTALS   Complete Vertical Stack    29 Modules 960 Tests     38,400 Qs  87 Shipped
--------------------------------------------------------------------------------

Key Curriculum Proportions:
- Total Standardized 40-Question Tests : 960 tests (administered as 3,840 sprints)
- Total Question Inventory             : 38,400 unique automated verification questions
- Total Milestone Shipped Projects     : 87 end-to-end verified builds
- Hardware Fabrication Artifacts       : 4 custom PCBs, 3 parametric enclosures
- Embedded Physical Devices            : 1 autonomous Edge AI running transformer weights


================================================================================
7. ANTIGRAVITY INGESTION & OPERATIONAL EXECUTION PROTOCOL
================================================================================

When executing this specification inside Antigravity against the live
repository files, follow this strict operational phase sequence:

PHASE 1: REPOSITORY REFACTORING & DIRECTORY CLEANUP
1. Execute a directory realignment script ensuring that all 29 modules
   (module00_onramp through module28_edge_ai) exist under their respective
   tier folders:
   - curriculum/tier0_foundations/
   - curriculum/tier1_core_systems/
   - curriculum/tier2_client_graphics_ux/
   - curriculum/tier3_infrastructure_crypto/
   - curriculum/tier4_frontier_accelerators/
2. Inside each module directory, create three subdirectories:
   - spec.md
   - drills/
   - projects/
3. Purge all ad-hoc markdown mentions of projects embedded within conceptual
   notes; project specifications must live exclusively within their project
   subdirectories.

PHASE 2: PROJECT SCAFFOLD INITIALIZATION
1. Generate the standardized subdirectories for all 87 projects:
   `curriculum/tierX/moduleYY/projects/PYY_N_slug/`
2. Every project directory must contain the four universal files:
   - README.md: Visual diagrams, physical parts list, conceptual mental model.
   - SPEC.md: Invariants, mathematical contracts, forbidden libraries, bounds.
   - sandbox/: Scratchpad file for rapid student experimentation.
   - starter/: Type-annotated zero-dependency boilerplate code.
   - harness/test_runner.py: Automated deterministic test runner.
   - harness/vectors.json: Edge-case inputs (overflows, zero states, race traps).

PHASE 3: QUESTION BATTERY POPULATION
1. Populate each module's drills/ directory with:
   - L1_mechanics.json (40 questions partitioned into 4 sprints of 10)
   - L2_execution.json (40 questions partitioned into 4 sprints of 10)
   - L3_invariants.json (40 questions partitioned into 4 sprints of 10)
2. Ensure every question includes an explanation field highlighting the
   underlying physical or mathematical invariant.

PHASE 4: WORKBENCH UI FRONTEND INTEGRATION
1. Mount the 10-Slot Circular Sprint Buffer to replace linear progress bars.
2. Bind the Time-Travel Scrubber component to Level 2 execution trace drills.
3. Wire the Side-by-Side Dual State Inspector to display memory diffs on
   Level 3 invariant failures.
4. Verify that Apprentice Mode defaults are active: 44px hit targets, audio
   relay clicks enabled, and Apple Pencil stylus canvas unhidden.
5. Connect local execution drivers to evaluate C, Rust, Python, and Verilog
   submissions without network dependencies.

================================================================================
END OF WHETSTONE MASTER ARCHITECTURE SPECIFICATION (3.0.0-PROD)
================================================================================
