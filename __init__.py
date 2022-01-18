from bpy import data
from bpy import context as con
from bpy.types import Panel, Operator
from bpy import ops

opids = { # opid = Operator ID
    'naquadah':'stargatematerials.addnaquadah',
    'chevron': 'stargatematerials.addchevron',
    'wormhole':'stargatematerials.addwormhole',
    'kawoosh': 'stargatematerials.addkawoosh'
}

bl_info = {
    "name": "StarGate Material Generator",
    "description": "This addon creates the materials wich are used by StarGateGenerator.",
    "author": "Henry Schynol",
    "version": (1, 0),
    "blender": (2, 60, 0),
    "location": "View3D > Toolbar > Create > StarGate",
    "warning": "This AddOn is still under development!", # used for warning icon and text in addons panel
    "doc_url": "https://github.com/heschy/Stargate-Generator/wiki",
    "support": "TESTING",
    "category": "Nodes",
}

class STARGATEMATERIALS_PT_main(Panel):
    """StarGate Creator AddOn by Henry Schynol"""
    bl_label       = "Materials"
    bl_idname      = "STARGATEMATERIALS_PT_main"
    bl_space_type  = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category    = "StarGate"

    
    def draw(self, context):
        layout = self.layout
        layout.operator(opids['naquadah'])
        
        return {'FINISHED'}

def STARGATEMATERIALS_OT_naquadah(Operator):
    """This Operation creates a Naquadah Material"""
    bl_label = 'Add Naquadah'
    bl_idname = opids['naquadah']
    
    onexec = bpy.props.EnumProperty(name='Def')
    
### Register ###

classes = [STARGATEMATERIALS_PT_main, STARGATEMATERIALS_OT_naquadah]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
        
def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
        
if __name__ == '__main__':
    register()
