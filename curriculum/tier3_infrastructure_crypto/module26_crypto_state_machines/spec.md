# Module 26: Cryptography, Identity & Web3 State Machines

**Tier:** `tier3_infrastructure_crypto`  
**Status:** Verified Master Specification  

## 1. Concrete Mental Model
>A decentralized state machine is a shared virtual computer. Cryptographic keys authenticate identity, digital signatures validate transactions, and cryptographic hashes secure the shared ledger.

## 2. Core Primitives
Cryptographic primitives: Symmetric ciphers (AES-GCM), hash functions (SHA-256, Keccak-256), public-key crypto, digital signatures (ECDSA secp256k1, Ed25519); Merkle trees: Inclusion proofs, tamper-evident logs; decentralized execution: State transitions, account models vs UTXO, gas accounting, peer-to-peer state sync.

## 3. Physical & Virtual Workbenches (BOM)
Local blockchain node simulator, hardware security key / smartcard.

## 4. Primary Literature & Canonical Links
- **[Textbook]** [Dan Boneh & Victor Shoup - A Graduate Course in Applied Cryptography (v0.6)](http://toc.cryptobook.us/)
- **[Seminal Paper]** [Satoshi Nakamoto - Bitcoin: A Peer-to-Peer Electronic Cash System (2008)](https://bitcoin.org/bitcoin.pdf)
- **[Seminal Paper]** [Whitfield Diffie & Martin E. Hellman - New Directions in Cryptography (IEEE 1976)](https://ieeexplore.ieee.org/document/1055638)
- **[Seminal Paper]** [Eli Ben-Sasson et al. - SNARKs for C: Verifying Program Executions with Succinct Arguments (CRYPTO 2013)](https://eprint.iacr.org/2013/507.pdf)

## 5. Standardized Milestone Projects
- **P26_1 (Alpha (Tactile))**: Merkle Tree Proof Engine — Build an engine in TypeScript/Rust that generates and verifies cryptographic inclusion proofs.
- **P26_2 (Beta (Milestone))**: Pure-Python AES-128 GCM Engine — Implement AES authenticated encryption in Galois/Counter Mode from first principles.
- **P26_3 (Gamma (Capstone))**: Decentralized State Machine Engine — Build a replicated ledger engine processing Ed25519-signed transactions and validating state roots.
