import bpy

def register():
    bpy.types.Scene.lprock_seed = bpy.props.IntProperty(
        name="Random Seed",
        description="Randomize shape",
        default=0
    )
    bpy.types.Scene.lprock_decimate_ratio = bpy.props.FloatProperty(
        name="Output Resolution",
        description="Decimate ratio",
        min=0.01,
        max=1.0,
        default=0.015
    )
    bpy.types.Scene.lprock_smooth = bpy.props.BoolProperty(
        name="Smooth Shading",
        description="Apply smooth shading",
        default=True
    )
    bpy.types.Scene.lprock_apply_modifiers = bpy.props.BoolProperty(
        name="Apply All Modifiers",
        description="Apply Displace and Decimate",
        default=True
    )

def unregister():
    del bpy.types.Scene.lprock_seed
    del bpy.types.Scene.lprock_decimate_ratio
    del bpy.types.Scene.lprock_smooth
    del bpy.types.Scene.lprock_apply_modifiers