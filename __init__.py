import re
from bpy import context as C
from bpy import data    as D
from bpy import types   as T
from bpy import ops     as O
from bpy import props   as P
import bpy

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
        #layout.operator('stargate.addatlantisgate_operator', icon='PLUS')
        
class STARGATE_OT_addstargate_milkyway(T.Operator):
    """This Operation adds a milkyway-Stargate to your scene.\nMilkyway-Stargates are the Stargates with orange Chevrons.\nThey can be found in the milkyway-galaxy"""
    bl_label       = "Add Stargate (Milkyway)"
    bl_idname      = "stargate.addmilkygate_operator"
    
    scale : P.FloatVectorProperty(name='Scale',       default=(1,1,1), size=3)
    res   : P.IntProperty(        name='Resolution',  default=2)
    rot   : P.FloatVectorProperty(name='Rotation',    default=(0,0,0), size=3)
    name  : P.StringProperty(     name='Object Name', default='StarGate')
    
    def STARGATE_SUBMETHOD_CREATE_NAQUADAH(self, default_y):
        
        mat_naquadah = D.materials.new(name='Naquadah')
        mat_naquadah = D.materials['Naquadah']
        mat_naquadah.use_nodes = True
        naquadah_nodes = mat_naquadah.node_tree.nodes
        connect = mat_naquadah.node_tree.links.new
        
        for i in naquadah_nodes:
            naquadah_nodes.remove(i)
        
        C.object.active_material = mat_naquadah 
        
        for i in D.materials:
            if re.search(STARGATE_SUBMETHOD_SEARCH_PATTERN('Naquadah'), i.name_full):
                D.materials.remove(i)
                
        mat_out = naquadah_nodes.new('ShaderNodeOutputMaterial')
        mat_out.name = 'STARGATE_MATERIAL:NAQUADAH_NODE:OUT'
        mat_out = naquadah_nodes['STARGATE_MATERIAL:NAQUADAH_NODE:OUT']
        for i in naquadah_nodes:
            if re.search(STARGATE_SUBMETHOD_SEARCH_PATTERN('STARGATE_MATERIAL:NAQUADAH_NODE:OUT'), i.name):
                naquadah_nodes.remove(i)
        mat_out.location = (300, default_y)
            
        bsdf_node = None
        bsdf_node = naquadah_nodes.new('ShaderNodeBsdfPrincipled')
        bsdf_node.name = 'STARGATE_MATERIAL:NAQUADAH_NODE:MAIN'
        bsdf_node = naquadah_nodes['STARGATE_MATERIAL:NAQUADAH_NODE:MAIN']
        for i in naquadah_nodes:
            if re.search(STARGATE_SUBMETHOD_SEARCH_PATTERN('STARGATE_MATERIAL:NAQUADAH_NODE:MAIN'), i.name):
                naquadah_nodes.remove(i)
        bsdf_node.inputs[4].default_value = 1
        bsdf_node.inputs[7].default_value = 0.75
        bsdf_node.location = (0,default_y)
        
        connect(bsdf_node.outputs[0], mat_out.inputs[0])
        
        ao_node = naquadah_nodes.new(type="ShaderNodeAmbientOcclusion")
        ao_node.name = 'STARGATE_MATERIAL:NAQUADAH_NODE:AO'
        ao_node = naquadah_nodes['STARGATE_MATERIAL:NAQUADAH_NODE:AO']
        for i in naquadah_nodes:
            if re.search(STARGATE_SUBMETHOD_SEARCH_PATTERN('STARGATE_MATERIAL:NAQUADAH_NODE:AO'), i.name):
                naquadah_nodes.remove(i)
        ao_node.location = (-200, default_y) 
        connect(ao_node.outputs[0], bsdf_node.inputs[0])
        
        mix_node = naquadah_nodes.new(type="ShaderNodeMixRGB")
        mix_node.name = 'STARGATE_MATERIAL:NAQUADAH_NODE:MIX'
        mix_node = naquadah_nodes['STARGATE_MATERIAL:NAQUADAH_NODE:MIX']
        for i in naquadah_nodes:
            if re.search(STARGATE_SUBMETHOD_SEARCH_PATTERN('STARGATE_MATERIAL:NAQUADAH_NODE:MIX'), i.name):
                naquadah_nodes.remove(i)
        mix_node.location = (-400, default_y)
        mix_node_val_a = 0.632452
        mix_node_val_b = 0.295307
        mix_node.inputs[1].default_value = (mix_node_val_a, mix_node_val_a, mix_node_val_a, 1.000000)
        mix_node.inputs[2].default_value = (mix_node_val_b, mix_node_val_b, mix_node_val_b, 1.000000)
        
        connect(mix_node.outputs[0], ao_node.inputs[0])
        
        noise_node = naquadah_nodes.new(type="ShaderNodeTexNoise")
        noise_node.name = 'STARGATE_MATERIAL:NAQUADAH_NODE:NOISE'
        noise_node = naquadah_nodes['STARGATE_MATERIAL:NAQUADAH_NODE:NOISE']
        for i in naquadah_nodes:
            if re.search(STARGATE_SUBMETHOD_SEARCH_PATTERN('STARGATE_MATERIAL:NAQUADAH_NODE:NOISE'), i.name):
                naquadah_nodes.remove(i)
        noise_node.location = (-600, default_y)
        connect(noise_node.outputs[0], mix_node.inputs[0])
        
        val_node = naquadah_nodes.new(type="ShaderNodeValue")
        val_node.name = 'STARGATE_MATERIAL:NAQUADAH_NODE:VAL'
        val_node = naquadah_nodes['STARGATE_MATERIAL:NAQUADAH_NODE:VAL']
        val_node.label = 'Noise Scale'
        for i in naquadah_nodes:
            if re.search(STARGATE_SUBMETHOD_SEARCH_PATTERN('STARGATE_MATERIAL:NAQUADAH_NODE:VAL'), i.name):
                naquadah_nodes.remove(i)
        val_node.location = (-800, default_y)
        val_node.outputs[0].default_value=2.5
        
        connect(val_node.outputs[0], noise_node.inputs[2])
        
        map_node = naquadah_nodes.new(type="ShaderNodeMapping")
        map_node.name = 'STARGATE_MATERIAL:NAQUADAH_NODE:MAP'
        map_node = naquadah_nodes['STARGATE_MATERIAL:NAQUADAH_NODE:MAP']
        for i in naquadah_nodes:
            if re.search(STARGATE_SUBMETHOD_SEARCH_PATTERN('STARGATE_MATERIAL:NAQUADAH_NODE:MAP'), i.name):
                naquadah_nodes.remove(i)
        map_node.location = (-800, default_y-100) 
        
        connect(map_node.outputs[0], noise_node.inputs[0])
        
        tex_node = naquadah_nodes.new(type="ShaderNodeTexCoord")
        tex_node.name = 'STARGATE_MATERIAL:NAQUADAH_NODE:TEX'
        tex_node = naquadah_nodes['STARGATE_MATERIAL:NAQUADAH_NODE:TEX']
        for i in naquadah_nodes:
            if re.search(STARGATE_SUBMETHOD_SEARCH_PATTERN('STARGATE_MATERIAL:NAQUADAH_NODE:TEX'), i.name):
                naquadah_nodes.remove(i)
        tex_node.location = (-1000, default_y) 
        
        connect(tex_node.outputs[3], map_node.inputs[0])
        
        range_node = naquadah_nodes.new(type="ShaderNodeMapRange")
        range_node.name = 'STARGATE_MATERIAL:NAQUADAH_NODE:RANGE'
        range_node = naquadah_nodes['STARGATE_MATERIAL:NAQUADAH_NODE:RANGE']
        for i in naquadah_nodes:
            if re.search(STARGATE_SUBMETHOD_SEARCH_PATTERN('STARGATE_MATERIAL:NAQUADAH_NODE:RANGE'), i.name):
                naquadah_nodes.remove(i)
        range_node.location = (-1000, default_y-250) 
        range_node.inputs[3].default_value=0.75
        range_node.inputs[4].default_value=1.25
        
        connect(range_node.outputs[0], map_node.inputs[1])
        connect(range_node.outputs[0], map_node.inputs[2])
        
        
        obj_node = naquadah_nodes.new(type="ShaderNodeObjectInfo")
        obj_node.name = 'STARGATE_MATERIAL:NAQUADAH_NODE:OBJ'
        obj_node = naquadah_nodes['STARGATE_MATERIAL:NAQUADAH_NODE:OBJ']
        for i in naquadah_nodes:
            if re.search(STARGATE_SUBMETHOD_SEARCH_PATTERN('STARGATE_MATERIAL:NAQUADAH_NODE:OBJ'), i.name):
                naquadah_nodes.remove(i)
        obj_node.location = (-1200, default_y-250) 
        
        connect(obj_node.outputs[4], range_node.inputs[0])
        
        
        for i in naquadah_nodes:
            i.width =150.0
            i.select = True
            
        bsdf_node.width = 250.0
        mat_out.select = False
    
    def execute(self, context):
        
        STARGATE_SUBMETHOD_CREATEGATE(s=self.scale,v=self.res, r=self.rot, n=self.name)
        self.STARGATE_SUBMETHOD_CREATE_NAQUADAH(200)
        
        return{'FINISHED'}
    
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)
    

classes = [STARGATE_OT_addstargate_milkyway, STARGATE_PT_MAINPANEL]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
        
if __name__ == '__main__':
    register()