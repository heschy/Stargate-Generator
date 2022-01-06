from bpy import context as C
from bpy import data    as D
from bpy import types   as T
import bpy

bsdf = {
    'BaseColor':0,
    'Roughness':7,
    
}


class STARGATE_PT_SHADER(T.Panel):
    """StarGate Creator AddOn by Henry Schynol"""
    bl_label       = "Material"
    bl_idname      = "STARGATE_PT_SHADER"
    bl_space_type  = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_category    = "StarGate"

    def draw(self, context):
        layout = self.layout

        layout.operator('stargate.addnaquadah_operator')
        
class STARGATE_OT_add_naquadah(T.Operator):
    bl_label       = "Add Naquadah-Shader"
    bl_idname      = "stargate.addnaquadah_operator"
    
    def execute(self, context):
        
        bpy.ops.mesh.primitive_cylinder_add(vertices=64, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(4, 4, 1))

        
        mat_naquadah = D.materials.new(name='Naquadah')
        mat_naquadah.use_nodes = True
        
        C.object.active_material = mat_naquadah
        
        main_shader = mat_naquadah.node_tree.nodes.get('Principled BSDF')
        
        main_shader.inputs[0]
        
        
        
        return{'FINISHED'}

classes = [STARGATE_OT_add_naquadah, STARGATE_PT_SHADER]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
        
if __name__ == '__main__':
    register()