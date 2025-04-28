import bpy
import random
from mathutils import Vector

class LPROCK_OT_Generate(bpy.types.Operator):
    bl_idname = "lprock.generate"
    bl_label = "Generate Rock"
    bl_description = "Generate a Low Poly Rock"

    def execute(self, context):
        scene = context.scene

        bpy.ops.mesh.primitive_cube_add()
        obj = context.active_object
        obj.name = f"LPRock_{len(bpy.data.objects)}"

        # Subsurf
        bpy.ops.object.modifier_add(type='SUBSURF')
        subsurf = obj.modifiers["Subdivision"]
        subsurf.levels = 5
        subsurf.render_levels = 5
        bpy.ops.object.modifier_apply(modifier="Subdivision")

        # Displace
        bpy.ops.object.modifier_add(type='DISPLACE')
        displace = obj.modifiers["Displace"]
        displace.texture_coords = 'GLOBAL'

        tex = bpy.data.textures.new(name=f"RockTex_{obj.name}", type='VORONOI')
        tex.noise_scale = 2
        tex.weight_2 = 1
        displace.texture = tex

        if scene.lprock_apply_modifiers:
            random.seed(scene.lprock_seed)
            offset = Vector((
                random.uniform(-10, 10),
                random.uniform(-10, 10),
                random.uniform(-10, 10)
            ))
            obj.location += offset

        if scene.lprock_apply_modifiers:
            bpy.ops.object.modifier_apply(modifier="Displace")
            obj.location = (0, 0, 0)

        # Decimate
        bpy.ops.object.modifier_add(type='DECIMATE')
        decimate = obj.modifiers["Decimate"]
        decimate.use_collapse_triangulate = True
        decimate.ratio = scene.lprock_decimate_ratio

        if scene.lprock_apply_modifiers:
            bpy.ops.object.modifier_apply(modifier="Decimate")

        # Smooth
        if scene.lprock_smooth:
            bpy.ops.object.shade_smooth()

        return {'FINISHED'}


class LPROCK_OT_EditDisplace(bpy.types.Operator):
    bl_idname = "lprock.edit_displace"
    bl_label = "Edit Displace Modifier"

    def execute(self, context):
        obj = context.active_object
        if obj and "Displace" in [m.name for m in obj.modifiers]:
            bpy.ops.object.mode_set(mode='EDIT')
            obj.modifiers["Displace"].show_in_editmode = True
            obj.modifiers["Displace"].show_on_cage = True
        return {'FINISHED'}


class LPROCK_OT_ApplyModifiers(bpy.types.Operator):
    bl_idname = "lprock.apply_modifiers"
    bl_label = "Apply Modifiers"

    def execute(self, context):
        obj = context.active_object
        if obj:
            bpy.ops.object.mode_set(mode='OBJECT')
            for mod in obj.modifiers:
                if mod.name in ["Displace", "Decimate"]:
                    bpy.ops.object.modifier_apply(modifier=mod.name)
        return {'FINISHED'}


def register():
    bpy.utils.register_class(LPROCK_OT_Generate)
    bpy.utils.register_class(LPROCK_OT_EditDisplace)
    bpy.utils.register_class(LPROCK_OT_ApplyModifiers)


def unregister():
    bpy.utils.unregister_class(LPROCK_OT_ApplyModifiers)
    bpy.utils.unregister_class(LPROCK_OT_EditDisplace)
    bpy.utils.unregister_class(LPROCK_OT_Generate)