# Module 19: 3D Spatial Modeling & Asset Pipelines (Blender to glTF)

**Tier:** `tier2_client_graphics_ux`  
**Status:** Verified Master Specification  

## 1. Concrete Mental Model
>3D digital objects are wireframe shells of interconnected triangles. The orientation of their surface normals governs how light interacts with the material.

## 2. Core Primitives
Mesh topology: Vertices, edges, faces, non-manifold geometry, quad modeling vs triangulation, surface normal vectors, smoothing groups; UV unwrapping: UV coordinates (U, V in [0, 1]), seam placement, texture projection, PBR materials (base color, roughness, metallic, normal maps); asset pipelines: glTF/GLB formats, hierarchical scene graphs.

## 3. Physical & Virtual Workbenches (BOM)
Blender 4.x, glTF 2.0 validator, 3-button mouse with scroll wheel.

## 4. Primary Literature & Canonical Links
- **[Tool Manual]** [Blender Foundation - Blender 4.x Reference Manual: Mesh Topology and glTF Export](https://docs.blender.org/manual/en/latest/)
- **[Specification]** [Khronos Group - glTF 2.0 Specification: JSON Scene Representation & Binary Buffers](https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html)
- **[Seminal Paper]** [Brian Karis - Real Shading in Unreal Engine 4 (Physically Based Rendering & Microfacet Theory)](https://blog.selfshadow.com/publications/s2013-shading-course/karis/s2013_pbs_epic_notes.pdf)

## 5. Standardized Milestone Projects
- **P19_1 (Alpha (Tactile))**: Topology Repair Lab — Import a flawed 3D mesh into Blender and clean it into an all-quad manifold surface with consistent normals.
- **P19_2 (Beta (Milestone))**: Parametric Industrial Knob Asset — Model a 3D control knob with grip fluting and set screws, unwrap UVs, and export to glTF.
- **P19_3 (Gamma (Capstone))**: Automated PCB-to-glTF Pipeline — Write a Python script for Blender that parses board dimensions and generates a detailed 3D enclosure.
