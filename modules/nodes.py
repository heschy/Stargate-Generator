import bpy
from .submethods import removeold as cleanup

# This Dictionary is used to find Nodes easily, instead of using the NodeID (e.g: 'MixRGB' instad of 'ShaderNodeMixRGB')
# Usage: nodenames['node'][0] - To get the NodeID
# Usage: nodenames['node'][1] - To get information about the Node (Geometrynode or Shadernode)
# Building: Dictionary {Tuple {0 = ID ; 1 = NodeType} }
nodenames = {
	'join':      ("GeometryNodeJoinGeometry",'Geometry'),
    'cylinder':  ("GeometryNodeMeshCylinder",'Geometry'),
    'boolean':   ('GeometryNodeMeshBoolean','Geometry'),
    'circle':    ('GeometryNodeMeshCircle','Geometry'),
    'icosphere': ('GeometryNodeMeshIcoSphere','Geometry'),
    'subdivide': ('GeometryNodeSubdivideMesh','Geometry'),
    'material':  ('GeometryNodeSetMaterial','Geometry'),
    'transform': ('GeometryNodeTransform','Geometry'),
    'intance':   ('GeometryNodeInstanceOnPoints','Geometry'),
    'combineXYZ':('ShaderNodeCombineXYZ','Shader'),
    'math':      ('ShaderNodeMath','Shader'),
    'range':     ('ShaderNodeMapRange','Shader'),

}

class MyNodeTree():
    tree = None
	nodes = None

    def __init__(self, nodetree):
        self.tree = nodetree
		self.nodes = self.tree.nodes

    def addnode(name,type,location,width=100.0): # Arg types: name=str type=str location=tuple(x,y) width=float
        node = self.nodes.new(nodenames[type])
        node.name = name
        cleanup(name,self.nodes)
        node.location = location
