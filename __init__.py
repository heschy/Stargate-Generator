import re
from bpy import context as C
from bpy import data    as D
from bpy import types   as T
from bpy import ops     as O
from bpy import props   as P
import bpy
from . import *

bl_info = {
    "name": "StarGate Generator",
    "description": "This addon creates StarGates.",
    "author": "Henry Schynol",
    "version": (1, 0),
    "blender": (3, 0, 0),
    "location": "View3D > Toolbar > Create > StarGate",
    "warning": "This AddOn is still under development!", # used for warning icon and text in addons panel
    "doc_url": "https://github.com/heschy/Stargate-Generator/wiki",
    "support": "TESTING",
    "category": "Add Mesh",
}

#    'BaseColor':0,
#    'Metallic':4,
#    'Rougness':7,
#    'Emission':17,
#    'EmissionStrength':18


class STARGATE_PT_MAINPANEL(T.Panel):
    """StarGate Creator AddOn by Henry Schynol"""
    bl_label       = "StarGate"
    bl_idname      = "STARGATE_PT_mainPanel"
    bl_space_type  = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category    = "Create"

    def draw(self, context):
        layout = self.layout

        layout.operator('stargate.addmilkygate_operator', icon='PLUS')
        layout.operator('stargate.addshader_operator'   , icon='MATERIAL')
        #layout.operator('stargate.addatlantisgate_operator', icon='PLUS')
        
classes = [STARGATE_PT_MAINPANEL]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
        
if __name__ == '__main__':
    register()
