bl_info = {
    "name": "Low Poly Rock Generator",
    "author": "Sergio Matsak",
    "version": (1, 0),
    "blender": (3, 0, 0),
    "location": "View3D > Sidebar > LPRocks Tab",
    "description": "Simple stylised and low poly rock generator.",
    "category": "Add Mesh",
}

import bpy
from . import operators, panel, properties

def register():
    properties.register()
    operators.register()
    panel.register()

def unregister():
    panel.unregister()
    operators.unregister()
    properties.unregister()

if __name__ == "__main__":
    register()