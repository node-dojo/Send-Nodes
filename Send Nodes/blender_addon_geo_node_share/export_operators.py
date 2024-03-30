import bpy
import json

class ExportGeoNodeGroup(bpy.types.Operator):
    """Export Selected Geometry Node Group to JSON"""
    bl_idname = "node.export_geo_node_group"
    bl_label = "Export Geo Node Group"
    
    def execute(self, context):
        selected_nodes = context.selected_nodes
        nodes_data = []
        for node in selected_nodes:
            node_info = {
                "name": node.name,
                "type": node.type,
                "properties": {k: getattr(node, k, '') for k in dir(node) if not k.startswith('__') and not callable(getattr(node, k))}
            }
            nodes_data.append(node_info)
        
        filepath = bpy.path.abspath('//geo_node_group.json')
        with open(filepath, 'w') as file:
            json.dump(nodes_data, file, indent=4)
        
        self.report({'INFO'}, f"Geo Node Group exported to {filepath}")
        return {'FINISHED'}
    
def register():
    bpy.utils.register_class(ExportGeoNodeGroup)

def unregister():
    bpy.utils.unregister_class(ExportGeoNodeGroup)

