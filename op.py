import bpy
from bpy import context as C
from bpy import data as D
from bpy import types as T

operators = {
  'mknaquadah': 'stargate_generator.createnaquadah_material',
  'mkchevron':  'stargate_generator.createchevron_material'
}

class CREATEGATE_OT_createnaquadahshader(T.Operator):
  bl_label = ''  
  bl_idname =
