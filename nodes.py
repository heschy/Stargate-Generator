import bpy

# This Dictionarys are used to find Nodes easily, instead of using the NodeID (e.g: 'MixRGB' instad of 'ShaderNodeMixRGB')
nodenames = {
	'join':      "GeometryNodeJoinGeometry",
    'math':      'ShaderNodeMath',
    'cylinder':  "GeometryNodeMeshCylinder",
    'boolean':   'GeometryNodeMeshBoolean',
    'material':  'GeometryNodeSetMaterial',
    'transform': 'GeometryNodeTransform'
}
