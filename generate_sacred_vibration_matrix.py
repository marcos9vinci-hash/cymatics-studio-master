import bpy
import math
import json
import os

print("=== INICIANDO GERADOR BLENDER 5.3 DE MATRIZ SAGRADA DE VIBRAÇÃO ===")

output_dir = r"C:\Users\Pc\Downloads\Cimatic\assets"
os.makedirs(output_dir, exist_ok=True)

phi = (1.0 + math.sqrt(5.0)) / 2.0  # 1.6180339887

# Dicionário de Cruzamentos Nodais Sagrados (Normalizados em [-1, 1] e coordenadas de excitação)
sacred_matrices = {}

# 1. PONTO CENTRAL ÚNICO (Modo Padrão CymaScope Jenny / Lauterwasser)
sacred_matrices["ponto_central_1"] = {
    "name": "Ponto Central Único (1 Ponto - CymaScope Puro)",
    "description": "Foco único central no transdutor piezoelétrico. Onda concêntrica pura sem interferência espúria.",
    "points": [
        {"x": 0.0, "z": 0.0, "weight": 1.0, "phase": 0.0}
    ]
}

# 2. VESICA PISCIS (2 Focos Sagrados + 2 Cruzamentos da Mandorla)
R_vp = 0.32
sacred_matrices["vesica_piscis"] = {
    "name": "Vesica Piscis (Dualidade & Mandorla Sagrada)",
    "description": "Dois focos circulares entrelaçados e os cruzamentos da lente cósmica.",
    "points": [
        {"x": -R_vp / 2.0, "z": 0.0, "weight": 0.85, "phase": 0.0},
        {"x": R_vp / 2.0, "z": 0.0, "weight": 0.85, "phase": 0.0},
        {"x": 0.0, "z": R_vp * math.sqrt(3) / 2.0, "weight": 0.50, "phase": math.pi / 2},
        {"x": 0.0, "z": -R_vp * math.sqrt(3) / 2.0, "weight": 0.50, "phase": math.pi / 2}
    ]
}

# 3. TRIQUETRA SAGRADA (3 Vértices a 120° + 3 Cruzamentos Internos)
R_tri = 0.38
tri_pts = []
for k in range(3):
    ang = math.radians(90 + k * 120)
    tri_pts.append({"x": round(R_tri * math.cos(ang), 4), "z": round(R_tri * math.sin(ang), 4), "weight": 0.75, "phase": k * math.pi / 3})
# Cruzamentos internos
for k in range(3):
    ang = math.radians(30 + k * 120)
    tri_pts.append({"x": round(R_tri * 0.45 * math.cos(ang), 4), "z": round(R_tri * 0.45 * math.sin(ang), 4), "weight": 0.45, "phase": 0.0})

sacred_matrices["triquetra"] = {
    "name": "Triquetra / Trindade Sagrada (3 Centros a 120°)",
    "description": "Geometria triangular trina com 3 vértices acústicos e cruzamento central.",
    "points": tri_pts
}

# 4. CRUZ HARMÔNICA / TETRAEDRO 2D (4 Eixos Cardeais + Centro)
R_cruz = 0.40
sacred_matrices["cruz_harmonica"] = {
    "name": "Cruz Harmônica / Tetraedro (4 Quadrantes)",
    "description": "Equilíbrio de 4 quadrantes cardeais com centro de gravidade neutro.",
    "points": [
        {"x": 0.0, "z": 0.0, "weight": 0.90, "phase": 0.0},
        {"x": R_cruz, "z": 0.0, "weight": 0.65, "phase": math.pi / 4},
        {"x": -R_cruz, "z": 0.0, "weight": 0.65, "phase": math.pi / 4},
        {"x": 0.0, "z": R_cruz, "weight": 0.65, "phase": math.pi / 4},
        {"x": 0.0, "z": -R_cruz, "weight": 0.65, "phase": math.pi / 4}
    ]
}

# 5. PENTAGRAMA SAGRADO / PROPORÇÃO ÁUREA (5 Pontas a 72° + 5 Cruzamentos Internos)
R_penta = 0.44
r_inner_penta = R_penta / (phi * phi)
penta_pts = []
for k in range(5):
    ang = math.radians(90 + k * 72)
    penta_pts.append({"x": round(R_penta * math.cos(ang), 4), "z": round(R_penta * math.sin(ang), 4), "weight": 0.70, "phase": k * math.pi / 5})
for k in range(5):
    ang = math.radians(90 + 36 + k * 72)
    penta_pts.append({"x": round(r_inner_penta * math.cos(ang), 4), "z": round(r_inner_penta * math.sin(ang), 4), "weight": 0.45, "phase": 0.0})

sacred_matrices["pentagrama"] = {
    "name": "Pentagrama Sagrado (Proporção Áurea Phi = 1.618)",
    "description": "5 vértices e 5 cruzamentos interiores derivados estritamente da Razão Áurea.",
    "points": penta_pts
}

# 6. SEMENTE DA VIDA (7 Centros da Criação a 60° + 6 Cruzamentos de Pétalas)
R_seed = 0.36
seed_pts = [{"x": 0.0, "z": 0.0, "weight": 1.0, "phase": 0.0}]
for k in range(6):
    ang = math.radians(k * 60)
    seed_pts.append({"x": round(R_seed * math.cos(ang), 4), "z": round(R_seed * math.sin(ang), 4), "weight": 0.65, "phase": 0.0})
for k in range(6):
    ang = math.radians(30 + k * 60)
    seed_pts.append({"x": round(R_seed * math.sqrt(3) * 0.5 * math.cos(ang), 4), "z": round(R_seed * math.sqrt(3) * 0.5 * math.sin(ang), 4), "weight": 0.40, "phase": math.pi / 3})

sacred_matrices["semente_vida"] = {
    "name": "Semente da Vida (Gênese Hexagonal - 7 Centros)",
    "description": "A matriz primária de 7 círculos que desdobra a geometria da criação biológica.",
    "points": seed_pts
}

# 7. OCTOGRAMA DE SARACENI (8 Raios a 45° + Centro = 9 Tronos Divinos)
R_oct = 0.42
oct_pts = [{"x": 0.0, "z": 0.0, "weight": 1.0, "phase": 0.0}]
for k in range(8):
    ang = math.radians(k * 45)
    oct_pts.append({"x": round(R_oct * math.cos(ang), 4), "z": round(R_oct * math.sin(ang), 4), "weight": 0.60, "phase": (k % 2) * math.pi / 4})

sacred_matrices["saraceni_8"] = {
    "name": "Octograma de Saraceni (8 Tronos / Estrela 8 Pontas)",
    "description": "O padrão octogonal sagrado que ancora as 7 linhas cósmicas e o trono regente.",
    "points": oct_pts
}

# 8. CUBO DE METATRON / FRUTO DA VIDA (13 Centros Esféricos)
R_m1 = 0.26
R_m2 = 0.52
meta_pts = [{"x": 0.0, "z": 0.0, "weight": 1.0, "phase": 0.0}]
# Anel 1: 6 esferas
for k in range(6):
    ang = math.radians(k * 60)
    meta_pts.append({"x": round(R_m1 * math.cos(ang), 4), "z": round(R_m1 * math.sin(ang), 4), "weight": 0.65, "phase": 0.0})
# Anel 2: 6 esferas externas
for k in range(6):
    ang = math.radians(k * 60)
    meta_pts.append({"x": round(R_m2 * math.cos(ang), 4), "z": round(R_m2 * math.sin(ang), 4), "weight": 0.45, "phase": math.pi / 6})

sacred_matrices["metatron_13"] = {
    "name": "Cubo de Metatron / Fruto da Vida (13 Centros Esféricos)",
    "description": "Os 13 centros nodais esféricos de onde nascem todos os 5 Sólidos Platônicos.",
    "points": meta_pts
}

# 9. FLOR DA VIDA (19 Centros Nodais)
R_fl1 = 0.24
R_fl2 = 0.48
flor_pts = [{"x": 0.0, "z": 0.0, "weight": 1.0, "phase": 0.0}]
for k in range(6):
    ang = math.radians(k * 60)
    flor_pts.append({"x": round(R_fl1 * math.cos(ang), 4), "z": round(R_fl1 * math.sin(ang), 4), "weight": 0.60, "phase": 0.0})
for k in range(6):
    ang = math.radians(k * 60)
    flor_pts.append({"x": round(R_fl2 * math.cos(ang), 4), "z": round(R_fl2 * math.sin(ang), 4), "weight": 0.40, "phase": 0.0})
for k in range(6):
    ang = math.radians(30 + k * 60)
    flor_pts.append({"x": round(R_fl1 * math.sqrt(3) * math.cos(ang), 4), "z": round(R_fl1 * math.sqrt(3) * math.sin(ang), 4), "weight": 0.35, "phase": 0.0})

sacred_matrices["flor_vida_19"] = {
    "name": "Flor da Vida Expandida (19 Centros)",
    "description": "Rede completa de 19 centros esféricos de ressonância harmônica total.",
    "points": flor_pts
}

# Salva arquivo JSON de Nós Sagrados
json_path = os.path.join(output_dir, "sacred_vibration_nodes.json")
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(sacred_matrices, f, indent=2, ensure_ascii=False)
print("ARQUIVO DE NÓS SAGRADOS GERADO COM SUCESSO EM:", json_path)

# ==============================================================================
# MODELAGEM BLENDER DOS HOLOGRAMAS SAGRADOS WIREFRAME (EXPORTAÇÃO GLB)
# ==============================================================================
bpy.ops.wm.read_factory_settings(use_empty=True)

# Cria Material Emissivo Holográfico Dourado e Ciano
mat_gold = bpy.data.materials.new(name="Holo_Gold")
mat_gold.use_nodes = True
nodes = mat_gold.node_tree.nodes
nodes.clear()
node_emit = nodes.new(type="ShaderNodeEmission")
node_emit.inputs['Color'].default_value = (0.83, 0.68, 0.21, 1.0) # Dourado sagrado
node_emit.inputs['Strength'].default_value = 2.5
node_out = nodes.new(type="ShaderNodeOutputMaterial")
mat_gold.node_tree.links.new(node_emit.outputs['Emission'], node_out.inputs['Surface'])

# Gera Círculo Central + Anéis da Semente da Vida
bpy.ops.curve.primitive_bezier_circle_add(radius=1.8, location=(0, 0, 0.05))
c_main = bpy.context.active_object
c_main.name = "Holo_Seed_Center"
c_main.data.bevel_depth = 0.015
c_main.data.materials.append(mat_gold)

for k in range(6):
    ang = math.radians(k * 60)
    cx = 1.8 * math.cos(ang)
    cy = 1.8 * math.sin(ang)
    bpy.ops.curve.primitive_bezier_circle_add(radius=1.8, location=(cx, cy, 0.05))
    c_petal = bpy.context.active_object
    c_petal.name = f"Holo_Seed_Petal_{k}"
    c_petal.data.bevel_depth = 0.012
    c_petal.data.materials.append(mat_gold)

# Anel Circunscrito Externo
bpy.ops.curve.primitive_bezier_circle_add(radius=3.6, location=(0, 0, 0.05))
c_outer = bpy.context.active_object
c_outer.name = "Holo_Outer_Circle"
c_outer.data.bevel_depth = 0.02
c_outer.data.materials.append(mat_gold)

# Exporta GLB
glb_path = os.path.join(output_dir, "sacred_seed_hologram.glb")
bpy.ops.export_scene.gltf(filepath=glb_path, export_format='GLB')
print("EXPORTADO SACRED SEED HOLOGRAM GLB PARA:", glb_path)
print("=== PROCESSO BLENDER CONCLUÍDO COM SUCESSO! ===")
