bl_info = {
    "name": "GeoNode Share",
    "blender": (2, 80, 0),
    "category": "Node",
    "version": (0, 1, 0),
    "author": "Your Name",
    "description": "Export and Import Geometry Node Groups as Serialized Code Snippets"
}

def register():
    from . import export_operators
    export_operators.register()

def unregister():
    from . import export_operators
    export_operators.unregister()
