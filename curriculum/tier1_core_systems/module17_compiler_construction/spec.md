# Module 17: Compiler Construction, Lexing, ASTs & Code Generation

**Tier:** `tier1_core_systems`  
**Status:** Verified Master Specification  

## 1. Concrete Mental Model
>A compiler translates human intent into machine execution by converting text into a stream of tokens, structuring tokens into a syntax tree, and flattening that tree into assembly.

## 2. Core Primitives
Lexical analysis: Token streams, lexemes, regular grammars, DFAs, source position tracking; syntactic analysis: CFGs, BNF, recursive descent parsing, Pratt parsing (operator precedence climbing), ASTs; code generation: Symbol tables, lexical scope analysis, instruction emission targeting RV32I.

## 3. Physical & Virtual Workbenches (BOM)
Text editor, Graphviz for AST visualization, Python/C build environment.

## 4. Primary Literature & Canonical Links
- **[Textbook]** [Alfred V. Aho, Monica S. Lam, Ravi Sethi, Jeffrey D. Ullman - Compilers: Principles, Techniques, & Tools (Dragon Book)](https://www.pearson.com/en-us/subject-catalog/p/compilers-principles-techniques-and-tools/P200000003299)
- **[Textbook]** [Bob Nystrom - Crafting Interpreters (A Bytecode VM and Tree-Walk Interpreter)](https://craftinginterpreters.com/)
- **[Workbench]** [Matt Godbolt - Compiler Explorer Interactive Disassembly Workbench](https://godbolt.org/)
- **[Textbook]** [Andrew W. Appel - Modern Compiler Implementation in C (Cambridge University Press)](https://www.cs.princeton.edu/~appel/modern/c/)

## 5. Standardized Milestone Projects
- **P17_1 (Alpha (Tactile))**: Regex-to-DFA Lexer Engine — Build a tokenizer that compiles regex patterns into state transition tables with line tracking.
- **P17_2 (Beta (Milestone))**: Pratt Expression Parser — Hand-craft a parser that converts mathematical expressions with mixed operator precedence into an AST.
- **P17_3 (Gamma (Capstone))**: Mini-Lang Compiler — Build an end-to-end compiler for a custom imperative language compiling directly to valid RISC-V assembly.
