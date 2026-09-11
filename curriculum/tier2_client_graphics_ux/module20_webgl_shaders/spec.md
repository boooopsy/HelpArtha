# Module 20: WebGL, Compute Shaders & Three.js 3D Telemetry Panels

**Tier:** `tier2_client_graphics_ux`  
**Status:** Verified Master Specification  

## 1. Concrete Mental Model
>WebGL exposes graphics hardware directly inside the browser. Arrays of 3D coordinates are uploaded to GPU buffers, where vertex and fragment shaders render them in parallel.

## 2. Core Primitives
WebGL state machine, buffers (VBO, EBO), Vertex Shaders (clip space), Fragment Shaders (colors), uniforms, attributes, varyings; Three.js architecture: Scene graphs, cameras, meshes, PBR shaders, shadow maps, lighting; real-time render loops (requestAnimationFrame), raycasting.

## 3. Physical & Virtual Workbenches (BOM)
WebGL 2.0 compatible browser, GPU with WebGL hardware acceleration.

## 4. Primary Literature & Canonical Links
- **[Specification]** [Khronos Group - WebGL 2.0 Specification & OpenGL ES 3.0 Reference Manual](https://www.khronos.org/webgl/)
- **[Workbench]** [Ricardo Cabello (Mr.doob) et al. - Three.js Documentation and Scene Graph Architecture](https://threejs.org/)
- **[Course]** [Patricio Gonzalez Vivo & Jen Lowe - The Book of Shaders: A Gentle Guide to Fragment Shaders](https://thebookofshaders.com/)

## 5. Standardized Milestone Projects
- **P20_1 (Alpha (Tactile))**: Raw WebGL Lighted Prism — Render an interactive 3D prism in raw WebGL without external libraries, compiling custom shaders.
- **P20_2 (Beta (Milestone))**: 3D Digital-Twin Telemetry Dashboard — Build a Three.js interface that renders the 3D enclosure from M11, rotating with live sensor data.
- **P20_3 (Gamma (Capstone))**: Thermal Heatmap Surface Shader — Write a custom GLSL fragment shader projecting a dynamic thermal gradient across the 3D mesh.
