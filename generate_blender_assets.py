import bpy
import math
import os

assets_dir = r"C:\Users\Pc\Downloads\Cimatic\assets"
os.makedirs(assets_dir, exist_ok=True)

def reset_scene():
    bpy.ops.wm.read_factory_settings(use_empty=True)

# 1. GENERATE CYMASCOPE RIM / BASIN (Cubeta Física)
reset_scene()

bpy.ops.mesh.primitive_cylinder_add(radius=9.4, depth=1.0, vertices=64, location=(0, 0, -0.4))
outer_ring = bpy.context.active_object
outer_ring.name = "CymaScope_Outer_Rim"

bpy.ops.mesh.primitive_cylinder_add(radius=9.0, depth=0.8, vertices=64, location=(0, 0, -0.2))
inner_cut = bpy.context.active_object
inner_cut.name = "Inner_Cutter"

mod = outer_ring.modifiers.new(name="RimHollow", type='BOOLEAN')
mod.object = inner_cut
mod.operation = 'DIFFERENCE'
bpy.context.view_layer.objects.active = outer_ring
bpy.ops.object.modifier_apply(modifier="RimHollow")
bpy.data.objects.remove(inner_cut, do_unlink=True)

bpy.ops.mesh.primitive_cylinder_add(radius=0.8, depth=0.3, vertices=32, location=(0, 0, -0.6))
exciter = bpy.context.active_object
exciter.name = "VoiceCoil_Mount"

mat_metal = bpy.data.materials.new(name="Brushed_Dark_Titanium")
bsdf = mat_metal.node_tree.nodes.get("Principled BSDF")
if bsdf:
    bsdf.inputs['Base Color'].default_value = (0.05, 0.06, 0.08, 1.0)
    bsdf.inputs['Metallic'].default_value = 0.95
    bsdf.inputs['Roughness'].default_value = 0.25

outer_ring.data.materials.append(mat_metal)
exciter.data.materials.append(mat_metal)

rim_path = os.path.join(assets_dir, "cymascope_basin.glb")
bpy.ops.export_scene.gltf(filepath=rim_path, export_format='GLB')
print("EXPORTED CYMASCOPE BASIN TO:", rim_path)

# 2. GENERATE MERKABAH (ESTRELA TETRAÉDRICA) & HOLOGRAMA TRIPLO
reset_scene()

r = 2.2
h = r * math.sqrt(2/3) * 2
bpy.ops.mesh.primitive_cone_add(vertices=3, radius1=r, radius2=0, depth=h, location=(0, 0, 0))
tetra_sun = bpy.context.active_object
tetra_sun.name = "Tetrahedron_Sun"

bpy.ops.mesh.primitive_cone_add(vertices=3, radius1=r, radius2=0, depth=h, location=(0, 0, 0))
tetra_earth = bpy.context.active_object
tetra_earth.name = "Tetrahedron_Earth"
tetra_earth.rotation_euler = (math.pi, 0, math.pi / 3)

bpy.ops.mesh.primitive_torus_add(major_radius=3.2, minor_radius=0.03, major_segments=48, minor_segments=12, location=(0, 0, 0))
ring_gold = bpy.context.active_object
ring_gold.name = "Ring_Gold_Outer"

bpy.ops.mesh.primitive_torus_add(major_radius=2.7, minor_radius=0.025, major_segments=48, minor_segments=12, location=(0, 0, 0))
ring_silver = bpy.context.active_object
ring_silver.name = "Ring_Silver_Mid"

bpy.ops.mesh.primitive_uv_sphere_add(radius=0.35, segments=32, ring_count=16, location=(0, 0, 0))
core_sun = bpy.context.active_object
core_sun.name = "Core_Solar_White"

mat_gold = bpy.data.materials.new(name="Sacred_Gold")
b_gold = mat_gold.node_tree.nodes.get("Principled BSDF")
if b_gold:
    b_gold.inputs['Base Color'].default_value = (1.0, 0.78, 0.15, 1.0)
    b_gold.inputs['Metallic'].default_value = 0.9
    b_gold.inputs['Roughness'].default_value = 0.2

mat_silver = bpy.data.materials.new(name="Sacred_Silver")
b_silver = mat_silver.node_tree.nodes.get("Principled BSDF")
if b_silver:
    b_silver.inputs['Base Color'].default_value = (0.85, 0.90, 0.98, 1.0)
    b_silver.inputs['Metallic'].default_value = 0.95
    b_silver.inputs['Roughness'].default_value = 0.15

mat_core = bpy.data.materials.new(name="Solar_Core")
b_core = mat_core.node_tree.nodes.get("Principled BSDF")
if b_core:
    b_core.inputs['Base Color'].default_value = (1.0, 1.0, 1.0, 1.0)
    b_core.inputs['Emission Color'].default_value = (1.0, 1.0, 0.9, 1.0)
    b_core.inputs['Emission Strength'].default_value = 3.0

tetra_sun.data.materials.append(mat_gold)
tetra_earth.data.materials.append(mat_silver)
ring_gold.data.materials.append(mat_gold)
ring_silver.data.materials.append(mat_silver)
core_sun.data.materials.append(mat_core)

merkabah_path = os.path.join(assets_dir, "merkabah_hologram.glb")
bpy.ops.export_scene.gltf(filepath=merkabah_path, export_format='GLB')
print("EXPORTED MERKABAH TO:", merkabah_path)

# 3. GENERATE PLATONIC ICOSAHEDRON (Water Element)
reset_scene()

bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=1, radius=2.2, location=(0, 0, 0))
ico = bpy.context.active_object
ico.name = "Platonic_Icosahedron"

mat_water = bpy.data.materials.new(name="Icosahedron_Cyan")
b_water = mat_water.node_tree.nodes.get("Principled BSDF")
if b_water:
    b_water.inputs['Base Color'].default_value = (0.0, 0.85, 1.0, 1.0)
    b_water.inputs['Metallic'].default_value = 0.8
    b_water.inputs['Roughness'].default_value = 0.1

ico.data.materials.append(mat_water)

ico_path = os.path.join(assets_dir, "platonic_icosahedron.glb")
bpy.ops.export_scene.gltf(filepath=ico_path, export_format='GLB')
print("EXPORTED ICOSAHEDRON TO:", ico_path)

print("ALL BLENDER PROCEDURAL ASSETS GENERATED SUCCESSFULLY!")
