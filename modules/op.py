import bpy
from bpy import context as C
from bpy import data as D
from bpy import types as T

#
operators = {
    'mknaquadah': 'stargate_generator.createnaquadah_material',
    'mkchevron':  'stargate_generator.createchevron_material',
    'mkwormhole': 'stargate_generator.createwormhole_material',
    'mkgeonodes': 'stargate_gererator.creategeometrynode_modifier'
}

class CREATEGATE_OT_creategeometrynodes(T.Operator):
    bl_label = 'Create Basic Stargate'
    bl_idname = operators['mkgeonodes']

    def execute(self, context):
        obj = C.object
        obj.modifiers.new(name='Stargate', type='NODES')
        

        return {'FINSISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

class CREATEGATE_OT_createnaquadahshader(T.Operator):
    bl_label = 'Create Naquadah Shader'
    bl_idname = operators['mknaquadah']

    def execute(self, context):
    # TODO Create the Operator
    return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)
