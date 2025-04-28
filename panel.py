import bpy

class LPRockGeneratorPanel(bpy.types.Panel):
    bl_label = "Low Poly Rock Generator"
    bl_idname = "VIEW3D_PT_lp_rock_generator"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'LPRocks'

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        layout.label(text="Settings", icon='TOOL_SETTINGS')
        layout.prop(scene, "lprock_apply_modifiers", text="Apply Modifiers", toggle=True)

        if scene.lprock_apply_modifiers:
            layout.prop(scene, "lprock_seed", text="Random Seed")

        layout.prop(scene, "lprock_decimate_ratio", text="Decimate Ratio")
        layout.prop(scene, "lprock_smooth", text="Smooth Shading")

        layout.separator()
        layout.operator("lprock.generate", text="Generate New Rock", icon='MESH_ICOSPHERE')

        obj = context.active_object
        if obj and any(mod.type == 'DISPLACE' for mod in obj.modifiers):
            layout.separator()
            layout.label(text="Displace Modifier", icon='MOD_DISPLACE')
            layout.operator("lprock.edit_displace", text="Edit Displace", icon='EDITMODE_HLT')
            layout.operator("lprock.apply_modifiers", text="Apply Modifiers", icon='CHECKMARK')


def register():
    bpy.utils.register_class(LPRockGeneratorPanel)


def unregister():
    bpy.utils.unregister_class(LPRockGeneratorPanel)