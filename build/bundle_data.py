#!/usr/bin/env python3
"""
bundle_data.py - Bundles all domains, concepts, projects, and the complete
v3.0.0-PROD 29-module matrix, 87 projects, and 4x10 micro-sprints into whetstone-data.js.
"""
import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT = os.path.join(ROOT, "content")
CURRICULUM = os.path.join(ROOT, "curriculum")
CONFIG = os.path.join(ROOT, "config")
OUT_FILE = os.path.join(ROOT, "whetstone-data.js")

CANONICAL_DOMAIN_RANKS = {
    # Phase 1: Physical, Numerical & Mechanical Foundations
    "00b": 1,   # Literacy: The Computer, the File, the Terminal
    "00a": 2,   # Numeracy: School Mathematics at Pace
    "00c": 3,   # Mathematics: Discrete, Linear Algebra, Calculus
    "00":  4,   # Foundations: Machine Model, Python & C, Toolchain

    # Phase 2: Core Engineering, Silicon & Single-Machine Systems
    "06":  5,   # The Command Line & POSIX Tools
    "01":  6,   # Languages & Runtimes (Memory Models, Type Systems)
    "02":  7,   # Algorithms & Data Structures (Systems Perspective)
    "17":  8,   # Digital Design & RTL (Gates, Flip-Flops, Verilog)
    "04":  9,   # Architecture & Performance (CPU, Caches, SIMD)
    "18": 10,   # Chip Architecture & Co-Design (Accelerators, PPA)
    "05": 11,   # Operating Systems (Kernels, Virtual Memory, Concurrency)

    # Phase 3: Networks, Storage, Databases & Distributed Systems
    "19": 12,   # Networking & Interconnect (TCP/IP, Sockets, Fabrics)
    "08": 13,   # Databases & Storage (B-Trees, LSM, Transactions)
    "09": 14,   # Caching & Delivery (Eviction, CDNs, Redis)
    "07": 15,   # Distributed Systems (Consensus, Raft, Fault Tolerance)
    "10": 16,   # Data Engineering (Pipelines, Streaming, Columnar)
    "11": 17,   # System Design in Practice (End-to-End Reliability)
    "20": 18,   # Security (Applied Cryptography, Exploits, Threat Models)

    # Phase 4: Numerics, Frontier AI & Technical Leadership
    "15": 19,   # Numerics & Precision (IEEE 754, Quantization, fp8)
    "12": 20,   # Machine Learning Foundations (Optimization, Backprop)
    "16": 21,   # GPU Kernels & Compilers (CUDA, Warps, Triton)
    "13": 22,   # LLMs & Frontier Models (Transformers, Pretraining, RLHF)
    "21": 23,   # Research Practice & Public Artifacts (Reproducing Papers)
    "14": 24,   # The Level Itself (Distinguished Engineer / Fellow Leadership)
}

def sort_order_of(n: str) -> int:
    n_clean = str(n).strip()
    return CANONICAL_DOMAIN_RANKS.get(n_clean, 999)

def load_v3_curriculum():
    tiers = [
        {"id": "tier0_foundations", "title": "Tier 0: Expanded Foundations & Mechanical On-Ramp"},
        {"id": "tier1_core_systems", "title": "Tier 1: Core Systems, Silicon & Industrial Design"},
        {"id": "tier2_client_graphics_ux", "title": "Tier 2: Client Runtimes, Spatial Graphics & Industrial UX"},
        {"id": "tier3_infrastructure_crypto", "title": "Tier 3: Applied Infrastructure, Crypto & Decentralized State"},
        {"id": "tier4_frontier_accelerators", "title": "Tier 4: Frontier Accelerators, On-Device AI & Embedded Silicon"}
    ]

    tier_map = {}
    all_modules = []
    all_projects = []

    for t in tiers:
        t_id = t["id"]
        t_path = os.path.join(CURRICULUM, t_id)
        t_mods = []
        if os.path.exists(t_path):
            mod_dirs = sorted(os.listdir(t_path))
            for md in mod_dirs:
                m_path = os.path.join(t_path, md)
                if not os.path.isdir(m_path):
                    continue

                spec_path = os.path.join(m_path, "spec.md")
                spec_content = ""
                if os.path.exists(spec_path):
                    with open(spec_path, "r", encoding="utf-8") as sf:
                        spec_content = sf.read()

                # Extract title from spec.md
                m_title = md
                title_match = re.search(r"^#\s*Module\s*(\d+):\s*(.+)$", spec_content, re.MULTILINE)
                if title_match:
                    m_title = title_match.group(2).strip()

                # Load drills
                drills = {}
                drills_path = os.path.join(m_path, "drills")
                if os.path.exists(drills_path):
                    for df in ["L1_mechanics.json", "L2_execution.json", "L3_invariants.json"]:
                        dp = os.path.join(drills_path, df)
                        if os.path.exists(dp):
                            with open(dp, "r", encoding="utf-8") as jf:
                                drills[df.replace(".json", "")] = json.load(jf)

                # Load projects
                mod_projects = []
                p_path = os.path.join(m_path, "projects")
                if os.path.exists(p_path):
                    for pd in sorted(os.listdir(p_path)):
                        proj_dir = os.path.join(p_path, pd)
                        if not os.path.isdir(proj_dir):
                            continue
                        
                        readme_txt = ""
                        spec_txt = ""
                        vectors = []
                        starter_code = ""

                        readme_p = os.path.join(proj_dir, "README.md")
                        if os.path.exists(readme_p):
                            with open(readme_p, "r", encoding="utf-8") as f:
                                readme_txt = f.read()

                        spec_p = os.path.join(proj_dir, "SPEC.md")
                        if os.path.exists(spec_p):
                            with open(spec_p, "r", encoding="utf-8") as f:
                                spec_txt = f.read()

                        vec_p = os.path.join(proj_dir, "harness", "vectors.json")
                        if os.path.exists(vec_p):
                            with open(vec_p, "r", encoding="utf-8") as f:
                                vectors = json.load(f)

                        starter_p = os.path.join(proj_dir, "starter", "solution.py")
                        if os.path.exists(starter_p):
                            with open(starter_p, "r", encoding="utf-8") as f:
                                starter_code = f.read()

                        p_obj = {
                            "slug": pd,
                            "tier": t_id,
                            "module": md,
                            "title": pd.replace("_", " ").title(),
                            "readme": readme_txt,
                            "spec": spec_txt,
                            "starter": starter_code,
                            "vectors": vectors
                        }
                        mod_projects.append(p_obj)
                        all_projects.append(p_obj)

                mod_obj = {
                    "dir": md,
                    "tier": t_id,
                    "title": m_title,
                    "spec": spec_content,
                    "drills": drills,
                    "projects": mod_projects
                }
                t_mods.append(mod_obj)
                all_modules.append(mod_obj)

        tier_map[t_id] = {
            "id": t_id,
            "title": t["title"],
            "modules": t_mods
        }

    # Load config
    fsrs_params = {}
    fp_path = os.path.join(CONFIG, "fsrs_params.json")
    if os.path.exists(fp_path):
        with open(fp_path, "r", encoding="utf-8") as f:
            fsrs_params = json.load(f)

    workspace_rules = {}
    wr_path = os.path.join(CONFIG, "workspace_rules.json")
    if os.path.exists(wr_path):
        with open(wr_path, "r", encoding="utf-8") as f:
            workspace_rules = json.load(f)

    return {
        "tiers": tiers,
        "tierMap": tier_map,
        "allModules": all_modules,
        "allProjects": all_projects,
        "fsrsParams": fsrs_params,
        "workspaceRules": workspace_rules
    }

def main():
    files = sorted(glob.glob(os.path.join(CONTENT, "[0-9]*.json")))
    domains = []
    concepts_by_uid = {}
    concepts_by_title = {}

    for f in files:
        with open(f, "r", encoding="utf-8") as fp:
            d = json.load(fp)
            dom_meta = d.get("domain", d)
            n_str = str(dom_meta.get("n", "0"))
            
            domain_obj = {
                "id": dom_meta.get("id", ""),
                "slug": dom_meta.get("slug", dom_meta.get("id", "")),
                "n": n_str,
                "title": dom_meta.get("title") or dom_meta.get("t", ""),
                "why": dom_meta.get("why", ""),
                "color": dom_meta.get("color", ""),
                "tag": dom_meta.get("tag", ""),
                "uid": dom_meta.get("uid", ""),
                "sort_order": sort_order_of(n_str),
                "sections": d.get("sections", []),
                "people": d.get("people", [])
            }
            domains.append(domain_obj)

    domains.sort(key=lambda x: x["sort_order"])

    total_concepts = 0
    total_templates = 0

    for dom in domains:
        dom_id = dom["id"]
        dom_slug = dom["slug"]
        dom_title = dom["title"]
        dom_n = dom["n"]

        for s_idx, sec in enumerate(dom.get("sections", [])):
            sec_title = sec.get("title") or sec.get("t", "")
            sec["title"] = sec_title
            sec_uid = sec.get("uid", "")
            for c_idx, c in enumerate(sec.get("concepts", [])):
                total_concepts += 1
                c_uid = c.get("uid", "")
                c_title = c.get("title") or c.get("t", "")
                c["title"] = c_title

                c["domain_id"] = dom_id
                c["domain_slug"] = dom_slug
                c["domain_n"] = dom_n
                c["domain_title"] = dom_title
                c["section_title"] = sec_title
                c["section_uid"] = sec_uid

                templates = c.get("L4") or c.get("templates") or []
                c["templates"] = templates
                total_templates += len(templates)

                if c_uid:
                    concepts_by_uid[c_uid] = c
                if c_title:
                    concepts_by_title[f"{dom_id}:{c_title}"] = c_uid
                    if c_title not in concepts_by_title:
                        concepts_by_title[c_title] = c_uid

    # Projects & Tracks
    projects_file = os.path.join(CONTENT, "projects.json")
    projects_data = {}
    if os.path.exists(projects_file):
        with open(projects_file, "r", encoding="utf-8") as fp:
            projects_data = json.load(fp)

    tracks_file = os.path.join(CONTENT, "tracks.json")
    tracks_data = {}
    if os.path.exists(tracks_file):
        with open(tracks_file, "r", encoding="utf-8") as fp:
            tracks_data = json.load(fp)

    # Load v3.0.0-PROD complete matrix
    v3_data = load_v3_curriculum()

    bundle = {
        "domains": domains,
        "projects": projects_data,
        "tracks": tracks_data,
        "conceptsByUid": concepts_by_uid,
        "conceptsByTitle": concepts_by_title,
        "v3": v3_data,
        "stats": {
            "totalDomains": len(domains),
            "totalConcepts": total_concepts,
            "totalTemplates": total_templates,
            "totalV3Modules": len(v3_data["allModules"]),
            "totalV3Projects": len(v3_data["allProjects"])
        }
    }

    print(f"Bundling {len(domains)} legacy domains, {total_concepts} concepts...")
    print(f"Bundling v3: {len(v3_data['allModules'])} modules across 5 tiers, {len(v3_data['allProjects'])} projects...")

    with open(OUT_FILE, "w", encoding="utf-8") as fp:
        fp.write("// Whetstone offline curriculum bundle v3.0.0-PROD\n")
        fp.write("// Generated by build/bundle_data.py\n")
        fp.write("window.WHETSTONE_DATA = ")
        json.dump(bundle, fp, separators=(",", ":"), ensure_ascii=False)
        fp.write(";\n")

    size_mb = os.path.getsize(OUT_FILE) / (1024 * 1024)
    print(f"Written {OUT_FILE} ({size_mb:.2f} MB)")

if __name__ == "__main__":
    main()
