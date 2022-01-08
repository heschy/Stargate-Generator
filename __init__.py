import re
from bpy import context as C
from bpy import data    as D
from bpy import types   as T
from bpy import ops     as O
from bpy import props   as P
import bpy

#    'BaseColor':0,
#    'Metallic':4,
#    'Rougness':7,
#    'Emission':17,
#    'EmissionStrength':18

def STARGATE_SUBMETHOD_SEARCH_PATTERN(name):
    return "^" + name + "*\\..{3}$"

def STARGATE_SUBMETHOD_CREATEGATE(v, r, s, n): # v:vertices r:rotation s:scale n:name
    
    v *= 8
    
    r = tuple(r)
    s = list(s)
    
    s[0] *= 4.0
    s[1] *= 4.0
    s[2] *= 0.5
    
    s = tuple(s)
    
    O.mesh.primitive_cylinder_add(vertices=v, enter_editmode=False, align='WORLD', scale=s, rotation=r)
    C.object.name = n
    objname = C.object.name_full
    C.object.data.use_auto_smooth = True
    O.object.shade_smooth()
    
    O.node.new_geometry_nodes_modifier()
    C.object.modifiers['GeometryNodes'].name = 'Stargate'
    
    geonodes = C.object.modifiers['Stargate']
    
    geonodename = geonodes.node_group.name_full
    
    newname = 'MilkyWay Stargate'
    
    D.node_groups[geonodename].name = newname
    
    geonodename = geonodes.node_group.name_full

    geonodes.node_group = D.node_groups[newname] # To be sure that the first Material with this name is used.
        
    for i in D.node_groups:
        if re.search(STARGATE_SUBMETHOD_SEARCH_PATTERN('MilkyWay Stargate'), i.name_full):
            D.node_groups.remove(i)
    

    
    return {'FINISHED'}
    

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
        layout.operator('stargate.addmilkygate_operator', icon='PLUS')
        
class STARGATE_OT_addstargate_milkyway(T.Operator):
    """This Operation adds a milkyway-Stargate to your scene.\nMilkyway-Stargates are the Stargates with orange Chevrons.\nThey can be found in the milkyway-galaxy"""
    bl_label       = "Add Stargate (Milkyway)"
    bl_idname      = "stargate.addmilkygate_operator"
    
    def execute(self, context):
        
        STARGATE_SUBMETHOD_CREATEGATE(s=(1,1,1),v=4, r=(0,0,0), n='sg')
        
        default_y = 300
        
        mat_naquadah = D.materials.new(name='Naquadah')
        mat_naquadah = D.materials['Naquadah']
        mat_naquadah.use_nodes = True
        naquadah_tree  = mat_naquadah.node_tree
        naquadah_nodes = naquadah_tree.nodes
        
        C.object.active_material = mat_naquadah 
        
        for i in D.materials:
            if re.search(STARGATE_SUBMETHOD_SEARCH_PATTERN('Naquadah'), i.name_full):
                D.materials.remove(i)
        
        main_shader = mat_naquadah.node_tree.nodes.get('Principled BSDF')
        
        main_shader.inputs[7].default_value = 0.75
        main_shader.location = (0,default_y)
        
        for i in D.materials:
            if re.search("^Ambient Occlusion*\\..{3}$", i.name_full):
                D.materials.remove(i)
        
        ao_node = naquadah_nodes.new(type="ShaderNodeAmbientOcclusion")
        ao_node = naquadah_nodes['Ambient Occlusion']
        for i in naquadah_nodes:
            if re.search(STARGATE_SUBMETHOD_SEARCH_PATTERN('Ambient Occlusion'), i.name):
                naquadah_nodes.remove(i)
        ao_node.location = (-200, default_y) 
        
        connect = naquadah_tree.links.new
        
        connect(ao_node.outputs[0], main_shader.inputs[0])
        
        mix_node = naquadah_nodes.new(type="ShaderNodeMixRGB")
        mix_node.name = 'STARGATE_MATERIAL:NAQUADAH_NODE:MIX'
        mix_node = naquadah_nodes['STARGATE_MATERIAL:NAQUADAH_NODE:MIX']
        for i in naquadah_nodes:
            if re.search(STARGATE_SUBMETHOD_SEARCH_PATTERN('STARGATE_MATERIAL:NAQUADAH_NODE:MIX'), i.name):
                naquadah_nodes.remove(i)
        mix_node.location = (-400, default_y)
        
        mix_node.inputs[1].default_value = (0.332452, 0.332452, 0.332452, 1.000000)
        mix_node.inputs[2].default_value = (0.095307, 0.095307, 0.095307, 1.000000)
        
        connect(mix_node.outputs[0], ao_node.inputs[0])
        
        return{'FINISHED'}
    
    #def invoke(self, context, event):
    #    return context.window_manager.invoke_props_dialog(self)
    

classes = [STARGATE_OT_addstargate_milkyway, STARGATE_PT_MAINPANEL]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
        
if __name__ == '__main__':
    register()