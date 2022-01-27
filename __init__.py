import re
from bpy import context as C
from bpy import data    as D
from bpy import types   as T
from bpy import ops     as O
from bpy import props   as P
import bpy
import .modules.nodes as sgg_nodes
import .modules.op as sgg_ops
import .modukes.submethods as sgg_submethods

bl_info = {
    "name": "StarGate Generator",
    "description": "This addon creates StarGates.",
    "author": "Henry Schynol",
    "version": (1, 0),
    "blender": (3, 0, 0),
    "location": "View3D > Toolbar > Create > StarGate",
    "warning": "This AddOn is still under development!", # used for warning icon and text in addons panel
    "doc_url": "https://github.com/heschy/Stargate-Generator/wiki",
    "support": "COMMUNITY",
    "category": "Add Mesh",
}



class STARGATE_PT_MAINPANEL(T.Panel):
    """StarGate Creator AddOn by Henry Schynol"""
    bl_label       = "StarGate"
    bl_idname      = "STARGATE_PT_mainPanel"
    bl_space_type  = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category    = "Create"

    def draw(self, context):
        layout = self.layout


	row = layout.row()
        row.operator('stargate.addmilkygate_operator', icon='PLUS')
	#row = layout.row()                                              # Uncomment when Atlantis is Ready
	#row.operator('stargate.addatlantisgate_operator', icon='PLUS')  # Uncomment when Atlantis Is Ready
	row = layout.row()
        row.operator('stargate.addshader_operator'   , icon='MATERIAL')

	return {'FINISHED'}

classes = [STARGATE_PT_MAINPANEL]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__ == '__main__':
    register()
